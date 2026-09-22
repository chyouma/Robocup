from hub import port
import motor_pair
import runloop
import color_sensor

async def grå_linje():
    motor_pair.pair(motor_pair.PAIR_1, port.B, port.A)
    motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 90, 100, -50)
    await runloop.sleep_ms(1000)
    motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 90, 100, 100)
    await runloop.sleep_ms(1000)

    while True:
        if 20 < color_sensor.reflection(port.C) < 40 or 20 < color_sensor.reflection(port.D) < 40:
            motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 90, 100, -50)
            await runloop.sleep_ms(1000)
            motor_pair.stop(motor_pair.PAIR_1)
            break
        else:
            motor_pair.move_tank(motor_pair.PAIR_1, 100, 150)
            print("Venstre", color_sensor.reflection(port.C), "Højre", color_sensor.reflection(port.D))


runloop.run(grå_linje())