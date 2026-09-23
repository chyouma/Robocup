from hub import port, motion_sensor, sound
import runloop
import motor_pair
import color_sensor
import color






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

PITCH_THRESHOLD = 25  # pitch value that triggers "stop"

motor_pair.pair(motor_pair.PAIR_1, port.B, port.A) # Motor A and B (from port a and b) is paired as PAIR_1



# Gider ikke at ændre alle comments der er skrevet på engelsk til dansk eller omvendt, lev med det lol.

async def forhin1():

    """
     FORHINDRING 1
     Brudt streg 1/2
    """

    print("Starter opgave 1")
    
    
    # Stop robotten kort
    motor_pair.stop(motor_pair.PAIR_1)
    await runloop.sleep_ms(300)
    
    
    # Drej til højre
    await motor_pair.move_tank_for_degrees(
        motor_pair.PAIR_1,
        45,     # Grader
        100,    # Hastighed venstre
        0       # Hastighed Højre
    )

    #   Turn left to go right, type shit.
    #
    #   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿
    #   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣉⣁⣤⣤⣶⣾⣿⣿⣶⡄⢲⣯⢍⠁⠄⢀⢹⣿
    #   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⢯⣾⣿⣿⣏⣉⣹⠿⠇⠄⠽⠿⢷⡈⠿⠇⣀⣻⣿⡿⣻
    #   ⣿⣿⡿⠿⠛⠛⠛⢛⡃⢉⢣⡤⠤⢄⡶⠂⠄⠐⣀⠄⠄⠄⠄⠄⡦⣿⡿⠛⡇⣼
    #   ⡿⢫⣤⣦⠄⠂⠄⠄⠄⠄⠄⠄⠄⠄⠠⠺⠿⠙⠋⠄⠄⠄⠢⢄⠄⢿⠇⠂⠧⣿
    #   ⠁⠄⠈⠁⠄⢀⣀⣀⣀⣀⣠⣤⡤⠴⠖⠒⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⢠⡞⠄⣸
    #   ⡀⠄⠄⠄⠄⠄⠤⠭⠦⠤⠤⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣂⣿
    #   ⣷⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢳⠄⠄⢀⠈⣠⣤⣤⣼⣿
    #   ⣿⣿⣷⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣴⣶⣶⣶⣄⡀⠄⠈⠑⢙⣡⣴⣿⣿⣿⣿⣿
    #   ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    #   
        
    
    # Kør frem indtil en sensor finder den grå streg
    while True:
        venstre = color_sensor.reflection(port.D)
        højre = color_sensor.reflection(port.C)
        # Når den grå streg findes:
        if venstre < THRESHOLD or højre < THRESHOLD:
            break
        # Ellers fortsæt lige frem
        motor_pair.move_tank(
            motor_pair.PAIR_1,
            200,
            200
        )
    
        await runloop.sleep_ms(10)
    
        
    # i har fundet stregen
    motor_pair.stop(motor_pair.PAIR_1)
    await runloop.sleep_ms(200)
    
    # Ryk lidt længere frem, så robotten kommer hen på stregen
    await motor_pair.move_tank_for_degrees(
        motor_pair.PAIR_1,
        30,
        200,
        200
    )
    
    print("Opgave 1 færdig")


async def forhin2():

    """
     FORHINDRING 2
     Brudt streg 2/2
    """

    print("Starter opgave 2")

    motor_pair.stop(motor_pair.PAIR_1)
    await runloop.sleep_ms(300)
    # Vitterligt det samme fra opgaven før, bare venstre istedet for højre

    # Drej til venstre
    await motor_pair.move_tank_for_degrees(
        motor_pair.PAIR_1,
        45,
        0,
        100
    )

    while True:
        venstre = color_sensor.reflection(port.D)
        højre = color_sensor.reflection(port.C)

        if venstre < THRESHOLD or højre < THRESHOLD:
            break

        motor_pair.move_tank(
            motor_pair.PAIR_1,
            200,
            200
        )

        await runloop.sleep_ms(10)

    motor_pair.stop(motor_pair.PAIR_1)
    await runloop.sleep_ms(200)

    await motor_pair.move_tank_for_degrees(
        motor_pair.PAIR_1,
        30,
        200,
        200
    )

    print("Opgave 2 færdig")




async def forhin3():

    """
     FORHINDRING 3
     Skub Flske
    """

    print("Starter forhindring 3")

    # Stop robotten kort
    motor_pair.stop(motor_pair.PAIR_1)
    await runloop.sleep_ms(300)


    # Drej skarpt til højre
    await motor_pair.move_tank_for_degrees(
        motor_pair.PAIR_1,
        90,
        100,
        0
    )

    # Kør frem indtil en sensor finder den grå streg, og egentligt bare skal fortsætte,
    # Indtil den finder den sorte streg, hvor flasken så vil være på den anden side at stregen.
    while True:
        venstre = color_sensor.reflection(port.D)
        højre = color_sensor.reflection(port.C)
        # Når den grå streg findes:
        if venstre < THRESHOLD or højre < THRESHOLD:
            break

        # Ellers fortsæt lige frem
        motor_pair.move_tank(
            motor_pair.PAIR_1,
            200,
            200
        )

        await runloop.sleep_ms(10)

    motor_pair.stop(motor_pair.PAIR_1)
    await runloop.sleep_ms(200)

    await motor_pair.move_tank_for_degrees(
        motor_pair.PAIR_1,
        30,
        200,
        200
    )

    print("Forhindring 3 færdig")


async def forhin4():

    """
     FORHINDRING 4
     Tilbage fra flaske(/bak)
    """

    print("Starter forhindring 4")

    # Stop robotten kort
    motor_pair.stop(motor_pair.PAIR_1)
    await runloop.sleep_ms(300)


    # Bak kortvarigt
    await motor_pair.move_tank_for_degrees(
        motor_pair.PAIR_1,
        -180,
        100,
        100
        )

    # Vend 180grader eller hvor meget det her kommer til at blive når vi tester den lol
    await motor_pair.move_tank_for_degrees(
        motor_pair.PAIR_1,
        90,
        0,
        200
        )

    # Følg streg til bunds
    venstre_hastighed = color_sensor.reflection(port.D) * 2
    højre_hastighed = color_sensor.reflection(port.C) * 2
    
    motor_pair.move_tank(
        motor_pair.PAIR_1,
        venstre_hastighed,
        højre_hastighed
    )

    # Drej til højre


    # Fortset som normalt


    print("Forhindring 4 færdig")


async def forhin5():

    """
     FORHINDRING 5
     Drej imod vippe
    """

    print("Starter forhindring 5")

    motor_pair.stop(motor_pair.PAIR_1)
    await runloop.sleep_ms(300)

    # Samme kode som flasken, da den bare skal dreje til venstre istedet for højre, og finde stregen

    # Drej skarpt til venstre
    await motor_pair.move_tank_for_degrees(
        motor_pair.PAIR_1,
        90,
        0,
        100
    )

    while True:
        venstre = color_sensor.reflection(port.D)
        højre = color_sensor.reflection(port.C)

        if venstre < THRESHOLD or højre < THRESHOLD:
            break

        motor_pair.move_tank(
            motor_pair.PAIR_1,
            200,
            200
        )

        await runloop.sleep_ms(10)

    motor_pair.stop(motor_pair.PAIR_1)
    await runloop.sleep_ms(200)

    await motor_pair.move_tank_for_degrees(
        motor_pair.PAIR_1,
        30,
        200,
        200
    )

    print("Forhindring 5 færdig")



async def forhin6(base_speed=200, correction_gain=3):

    """
     FORHINDRING 6
     Vippe
    """

    print("Starter forhindring 6")

    motion_sensor.reset_yaw(0)
    await runloop.sleep_ms(200)  # brief pause instead of waiting for motion_sensor.stable()

    while True:
        yaw, pitch, roll = motion_sensor.tilt_angles()
        yaw_deg = yaw * -0.1     
        pitch_deg = pitch / 10

        # steer opposite the drift to correct back to initial yaw
        correction = int(yaw_deg * correction_gain)
        left_speed = base_speed + correction
        right_speed = base_speed - correction

        print("driving | yaw:", yaw_deg, "pitch:", pitch_deg, "L/R:", left_speed, right_speed)
        motor_pair.move_tank(motor_pair.PAIR_1, left_speed, right_speed)

        if pitch_deg >= PITCH_THRESHOLD:
            print("stop")
            motor_pair.stop(motor_pair.PAIR_1)
            break

        await runloop.sleep_ms(10)

    print("Forhindring 6 færdig")



async def forhin7():
    """
     FORHINDRING 7
     4-parralelle streger*?
    """

    print("Starter forhindring 7")

    # Drej robotten og kør frem
    motor_pair.move_tank_for_degrees(
        motor_pair.PAIR_1,
        45,
        0,
        100
    )

    await runloop.sleep_ms(300)

    motor_pair.move_tank(
        motor_pair.PAIR_1,
        250,
        250
    )

    # Antal streger der er blevet registreret.
    count = 0

    # Tjekker om sensor er på en "mørk streg"
    on_bar = False

    # Kryds antal streger
    while count < 3:

        # Læs reflektionsværdien fra sensor C.
        reflection = color_sensor.reflection(port.C)

        # Hvis reflektionsværdien er under THRESHOLD, er stregen "mørk"
        currently_on_bar = reflection < THRESHOLD


        # Tæl kun når sensoren går FRA lyst TIL mørkt.
        #
        #Ellers bliver samme streg talt flere gange, og det er noget røv
        if currently_on_bar and not on_bar:
            count += 1
            print("Streger talt:", count)


        # Gem om vi er på stregen til næste måling.
        on_bar = currently_on_bar

        # Vent 10 ms før næste måling.
        await runloop.sleep_ms(10)


    # Vi har nu fundet alle 4 streger.
    motor_pair.stop(motor_pair.PAIR_1)

    print("Forhindring 7 færdig")
    print("Antal streger krydset:", count)


async def forhin8():

    """
     FORHINDRING 8
     xxx
    """

    print("Starter forhindring 8")

    # Tilføj kode til forhindring 8 her.

    print("Forhindring 8 færdig")

async def forhin9():

    """
     FORHINDRING 9
     xxx
    """

    print("Starter forhindring 9")

    # Tilføj kode til forhindring 9 her.

    print("Forhindring 9 færdig")

async def forhin10():

    """
     FORHINDRING 10
     xxx
    """

    print("Starter forhindring 10")

    # Tilføj kode til forhindring 10 her.

    print("Forhindring 10 færdig")    



#
#
#
# TILFØJ NU FORHELVEDE FLERE AF DE DER TEMPLATES HVIS DER ER BEHOV FOR DET,
# OG IKKE MINDST ENDNU EN CHALLENGE PÅ DEN DER LISTE UNDER
#
#
#


# De forskellige challenges der kører og hvonrår osv idk

async def kør_forhindring(obs):
    """
     VÆLG FORHINDRING
    """
    print("Forhindring nummer:", obs)

    if obs == 1:
        await forhin1()

    elif obs == 2:
        await forhin2()

    elif obs == 3:
        await forhin3()

    elif obs == 4:
        await forhin4()

    elif obs == 5:
        await forhin5()

    elif obs == 6:
        await forhin6()

    elif obs == 7:
        await forhin7()

    elif obs == 8:
        await forhin8()

    elif obs == 9:
        await forhin8()

    elif obs == 10:
        await forhin8()    

    elif obs == 11:
        await forhin8()

    elif obs == 12:
        await forhin8()

    elif obs == 13:
        await forhin8() 
   
    else:
        print("Ingen kode til forhindring:", obs)









async def grå_linje():

    """
    NORMAL KØRSEL / GRÅ LINJE 
    (Brydes ved sort streg)
    """

    global obs


    # Hoved-loopet kører hele tiden.
    while True:

        # Hvis ENTEN sensor C eller D registrerer sort,
        # er robotten nået til næste forhindring.
        if (
            color_sensor.color(port.C) == color.BLACK
            or color_sensor.color(port.D) == color.BLACK
        ):

            # Stop robotten.
            motor_pair.stop(motor_pair.PAIR_1)


            # Gå videre til næste forhindring.
            obs += 1

            print("--------------------")
            print("Fundet forhindring:", obs)
            print("--------------------")


            # Kør den korrekte forhindring ifølge den der fuckass liste med alle challenges.
            await kør_forhindring(obs)


            # Når forhindringen er færdig, fortsætter while-loopet automatisk.


        else:

            # Robotten følger den grå linje.
            #
            # Sensor D styrer den ene motor.
            # Sensor C styrer den anden motor.
            #
            # "rotten" >:) retter sig op ved at ændre hastighederne på motoren når den kører.

            venstre_hastighed = color_sensor.reflection(port.D) * 2
            højre_hastighed = color_sensor.reflection(port.C) * 2

            motor_pair.move_tank(
                motor_pair.PAIR_1,
                venstre_hastighed,
                højre_hastighed
            )


        # Vent 10 ms før næste sensoraflæsning.
        await runloop.sleep_ms(10)


runloop.run(grå_linje()) # Programmet er more or less det hovedprogram der køres, når der ikke er en aktiv challenge.
