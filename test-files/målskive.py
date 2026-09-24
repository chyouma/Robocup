from hub import port, motion_sensor, sound
import runloop
import motor_pair
import color_sensor
import color
import distance_sensor


"""
8888888b.   .d88888b. 88888888888 88888888888 8888888888 8888888b.         d8888 8888888888 .d8888b.  
888   Y88b d88P" "Y88b    888         888     888        888   Y88b       d88888 888       d88P  Y88b 
888    888 888     888    888         888     888        888    888      d88P888 888       Y88b.      
888   d88P 888     888    888         888     8888888    888   d88P     d88P 888 8888888    "Y888b.   
8888888P"  888     888    888         888     888        8888888P"     d88P  888 888           "Y88b. 
888 T88b   888     888    888         888     888        888 T88b     d88P   888 888             "888 
888  T88b  Y88b. .d88P    888         888     888        888  T88b   d8888888888 888       Y88b  d88P 
888   T88b  "Y88888P"     888         888     8888888888 888   T88b d88P     888 8888888888 "Y8888P"                                                                                                    
"""


"""
SETTINGS
"""

obs = 0 # Cheks for current challenge

THRESHOLD = 75 # Reflection-value under value is concidered a Dark Line - Adjust if necessary
BLACK_THRESHOLD = 10

PITCH_THRESHOLD = 25  # pitch value that triggers "stop"

DISTANCE_PORT = port.E  # <-- SÆT DEN RIGTIGE PORT for afstandssensoren her
DISTANCE_THRESHOLD_MM = 100  # hvor tæt på flasken skal være før vi stopper med at dreje - juster ved test

ANTAL_RINGE = 2  # antal tynde grå ringe der skal krydses for at nå midten af målskiven - juster ved test

motor_pair.pair(motor_pair.PAIR_1, port.B, port.A) # Motor A and B (from port a and b) is paired as PAIR_1



def sensor_farve(sensor_port):
    r, g, b, inten = color_sensor.rgbi(sensor_port)
    reflection = color_sensor.reflection(sensor_port)

    if reflection < 10 and b - r < 10:
        return "black"
    elif b - r > 15:
        return "blue"
    elif reflection > 45:
        return "white"
    else:
        return "gray"
   

async def forhin8():

    """
     FORHINDRING 8
     Til målskive (trin "1" på tegningen - lige ned ad stregen og ind til den sorte streg
     der markerer selve målskiven).
    """

    print("Starter forhindring 8")

    # Stop robotten kort
    motor_pair.stop(motor_pair.PAIR_1)
    await runloop.sleep_ms(300)

    await motor_pair.move_tank_for_degrees(
        motor_pair.PAIR_1,
        80,
        100,
        100
    )

    # Drej skarpt til højre
    await motor_pair.move_tank_for_degrees(
        motor_pair.PAIR_1,
        180,
        0,
        100
    )

    # Kør frem indtil en sensor finder den grå/sorte streg ved målskiven.

    while True:
        venstre = color_sensor.reflection(port.D)
        højre = color_sensor.reflection(port.C)

        if sensor_farve(port.C) == "black" or sensor_farve(port.D) == "black":
            break

        motor_pair.move_tank(
            motor_pair.PAIR_1,
            200,
            200
        )

        await runloop.sleep_ms(10)

    motor_pair.stop(motor_pair.PAIR_1)
    await runloop.sleep_ms(200)
    print("Forhindring 8 færdig")

async def forhin9():

    """
     FORHINDRING 9
     Målskive (flaske i målskive) - strat:

     2a: reset gyro og kør ligeud mens vi tæller de tynde grå ringe, indtil midten.
     2b: drej til venstre indtil afstandssensoren finder flasken på den blå prik.
     2c: kør langsomt ind i den i en blød (bezier-agtig) kurve tilbage mod midten.
     2d: brug yaw til at dreje robotten tilbage og finde vej ud af målskiven igen.
    """

    print("Starter forhindring 9")

    motor_pair.stop(motor_pair.PAIR_1)
    await runloop.sleep_ms(300)

    hastighed = 150       # basishastighed inde i målskiven - lidt lavere end normalt for præcision
    hastighed_dreje = 100  # hastighed når vi drejer på stedet

    # 2a: Reset gyroen og kør ligeud, mens vi tæller de tynde grå ringe
    motion_sensor.reset_yaw(0)
    await runloop.sleep_ms(100)

    count = 0
    on_ring = False # tbh ved ikke engang om vi har brug for den her lol

    while count < ANTAL_RINGE:
        reflection = color_sensor.reflection(port.D)
        currently_on_ring = reflection < THRESHOLD

        # Tæl kun ved overgang fra lyst til mørkt, så samme ring ikke tælles flere gange
        if currently_on_ring and not on_ring:
            count += 1
            print("Ringe talt:", count)

        on_ring = currently_on_ring

        # Simpel yaw-korrektion så vi kører lige ind mod midten
        yaw = motion_sensor.tilt_angles()[0]
        korrektion = int(yaw * 0.3)  # juster gain ved test

        motor_pair.move_tank(
            motor_pair.PAIR_1,
            hastighed - korrektion,
            hastighed + korrektion
        )

        await runloop.sleep_ms(10)

    motor_pair.stop(motor_pair.PAIR_1)
    await runloop.sleep_ms(300)

    print("Nået midten af målskiven... i hope")

    # 2b: Drej til venstre på stedet indtil afstandssensoren ser flasken
    while True:
        afstand = distance_sensor.distance(DISTANCE_PORT)  # -1 hvis intet er i syne

        if afstand != -1 and afstand < DISTANCE_THRESHOLD_MM:
            break

        motor_pair.move_tank(motor_pair.PAIR_1, -hastighed_dreje, hastighed_dreje)
        await runloop.sleep_ms(10)

    motor_pair.stop(motor_pair.PAIR_1)
    await runloop.sleep_ms(200)

    print("Flaske fundet")

    # 2c: Kør langsomt ind i flasken i en blød, bezier-agtig kurve tilbage mod midten
    await kør_blød_kurve(varighed_ms=1500, hastighed_lav=100, kurve_styrke=60)
    await runloop.sleep_ms(300)

    print("Flaske skubbet mod midten")

    # 2d: Brug yaw til at dreje robotten ca. 180 grader og finde tilbage ud af målskiven
    # Yaw blev resat til 0 i 2a mens robotten pegede IND mod midten,
    # så "lige ud af målskiven igen" svarer til at dreje til yaw 1800 (180 grader).
    MÅL_YAW = 1800  # juster fortegn/værdi ved test, afhængig af drejeretning og enheder

    while abs(motion_sensor.tilt_angles()[0]) < MÅL_YAW:
        motor_pair.move_tank(motor_pair.PAIR_1, hastighed_dreje, -hastighed_dreje)
        await runloop.sleep_ms(10)

    motor_pair.stop(motor_pair.PAIR_1)
    await runloop.sleep_ms(200)

    # Kør ligeud igen med yaw-korrektion, indtil vi rammer en sort/grå streg ved kanten af målskiven
    while True:
        venstre = color_sensor.reflection(port.D)
        højre = color_sensor.reflection(port.C)

        if venstre < THRESHOLD or højre < THRESHOLD:
            break

        yaw_afvigelse = motion_sensor.tilt_angles()[0] - MÅL_YAW
        korrektion = int(yaw_afvigelse * 0.3)  # juster gain ved test

        motor_pair.move_tank(
            motor_pair.PAIR_1,
            hastighed - korrektion,
            hastighed + korrektion
        )

        await runloop.sleep_ms(10)

    motor_pair.stop(motor_pair.PAIR_1)
    await runloop.sleep_ms(200)

    print("Forhindring 9 færdig")




async def kør_blød_kurve(varighed_ms=1500, hastighed=100, kurve_styrke=60): # Det er et mirakel hvis dette virker på første forsøg lol

    """
    Ideen her er at lave en blød kurve som gør flasken bliver i hænderne
    """


    steps = max(varighed_ms // 50, 1)

    for i in range(steps):
        t = i / max(steps - 1, 1)

        # Smooth overgang fra 0 -> 1
        smooth = 3 * t**2 - 2 * t**3

        bias = int(kurve_styrke * (1 - smooth))

        motor_pair.move_tank(
            motor_pair.PAIR_1,
            hastighed - bias,
            hastighed + bias
        )

        await runloop.sleep_ms(50)

    motor_pair.stop(motor_pair.PAIR_1)