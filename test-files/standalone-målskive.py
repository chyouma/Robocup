from hub import port, motion_sensor
import runloop
import color_sensor
import distance_sensor

THRESHOLD = 75  # Reflection-value under value is concidered a Dark Line

DISTANCE_PORT = port.E  # <-- SÆT DEN RIGTIGE PORT for afstandssensoren her
DISTANCE_THRESHOLD_MM = 100  # hvor tæt på flasken skal være før vi stopper med at dreje

ANTAL_RINGE = 2  # antal tynde grå ringe der skal krydses for at nå midten af målskiven


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


async def test_forhin9_logic():

    print("=== TEST: forhin9 (no motors) ===")

    hastighed = 150
    hastighed_dreje = 100

    # --- 2a: reset yaw, "drive" straight while counting rings ---
    print("-- Fase 2a: tæller ringe, hold sensor D over lys/mørk for at simulere --")
    motion_sensor.reset_yaw(0)
    await runloop.sleep_ms(200)

    count = 0
    on_ring = False

    while count < ANTAL_RINGE:
        reflection = color_sensor.reflection(port.D)
        currently_on_ring = reflection < THRESHOLD

        if currently_on_ring and not on_ring:
            count += 1
            print("Ring talt:", count)

        on_ring = currently_on_ring

        yaw = motion_sensor.tilt_angles()[0]
        korrektion = int(yaw * 0.3)

        print("would-drive | reflection:", reflection, "yaw:", yaw,
              "L/R:", hastighed - korrektion, hastighed + korrektion)

        await runloop.sleep_ms(200)  # slowed down for readable test output

    print("Fase 2a færdig, nået 'midten'")
    await runloop.sleep_ms(500)

    # --- 2b: "turn left" until distance sensor sees the bottle ---
    print("-- Fase 2b: hold en hånd/genstand foran afstandssensoren --")
    while True:
        afstand = distance_sensor.distance(DISTANCE_PORT)  # -1 if nothing in view

        print("would-turn | afstand:", afstand,
              "L/R:", -hastighed_dreje, hastighed_dreje)

        if afstand != -1 and afstand < DISTANCE_THRESHOLD_MM:
            print("Flaske 'fundet' (afstand under threshold)")
            break

        await runloop.sleep_ms(200)

    await runloop.sleep_ms(500)

    # --- 2c: soft curve bias values (no actual driving) ---
    print("-- Fase 2c: simulerer blød kurve --")
    varighed_ms = 1500
    hastighed_lav = 100
    kurve_styrke = 60
    steps = max(varighed_ms // 50, 1)

    for i in range(steps):
        t = i / max(steps - 1, 1)
        smooth = 3 * t**2 - 2 * t**3
        bias = int(kurve_styrke * (1 - smooth))
        print("curve step", i, "| L/R:", hastighed_lav - bias, hastighed_lav + bias)
        await runloop.sleep_ms(50)

    print("Fase 2c færdig")
    await runloop.sleep_ms(500)

    # --- 2d: "turn" using yaw until reaching target, then "drive" until line found ---
    print("-- Fase 2d: rotér hub i hånden for at simulere drejning til MÅL_YAW --")
    MÅL_YAW = 1800

    while abs(motion_sensor.tilt_angles()[0]) < MÅL_YAW:
        yaw_now = motion_sensor.tilt_angles()[0]
        print("would-turn | yaw:", yaw_now, "target:", MÅL_YAW,
              "L/R:", hastighed_dreje, -hastighed_dreje)
        await runloop.sleep_ms(200)

    print("Nåede MÅL_YAW")
    await runloop.sleep_ms(500)

    print("-- Fase 2d del 2: hold sensor D/C over sort/grå for at simulere kant --")
    while True:
        venstre = color_sensor.reflection(port.D)
        højre = color_sensor.reflection(port.C)

        if venstre < THRESHOLD or højre < THRESHOLD:
            print("Kant fundet (venstre:", venstre, "højre:", højre, ")")
            break

        yaw_afvigelse = motion_sensor.tilt_angles()[0] - MÅL_YAW
        korrektion = int(yaw_afvigelse * 0.3)

        print("would-drive | venstre:", venstre, "højre:", højre,
              "L/R:", hastighed - korrektion, hastighed + korrektion)

        await runloop.sleep_ms(200)

    print("=== TEST forhin9 færdig ===")


runloop.run(test_forhin9_logic())