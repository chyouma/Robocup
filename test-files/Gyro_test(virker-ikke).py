from hub import port, motion_sensor
import runloop
import motor_pair
import color_sensor
import color

motor_pair.pair(motor_pair.PAIR_1, port.B, port.A)

THRESHOLD = 75   # reflection below this = "on a bar"
SPEED = 250
TURN_SPEED = 150
KP = 2.5


async def turn(degrees):
    """Turn in place by a relative angle, using the gyro instead of guessed motor degrees."""
    start = motion_sensor.tilt_angles()[0] / 10
    target = start + degrees

    while True:
        current = motion_sensor.tilt_angles()[0] / 10
        remaining = target - current
        if abs(remaining) < 2:
            break
        speed = TURN_SPEED if remaining > 0 else -TURN_SPEED
        motor_pair.move_tank(motor_pair.PAIR_1, speed, -speed)
        await runloop.sleep_ms(10)

    motor_pair.stop(motor_pair.PAIR_1)


async def drive_straight(obs):
    motion_sensor.reset_yaw(0)

    while True:
        if color_sensor.color(port.C) == color.BLACK:
            motor_pair.stop(motor_pair.PAIR_1)
            obs += 1
            await cross_bars(obs)
            continue

        turn_amount = motion_sensor.tilt_angles()[0] / 10 * KP
        motor_pair.move_tank(motor_pair.PAIR_1, int(SPEED + turn_amount), int(SPEED - turn_amount))
        await runloop.sleep_ms(10)


async def cross_bars(obs):
    await turn(45)
    motion_sensor.reset_yaw(0)  # new heading reference — straight-driving now corrects to THIS direction

    count = 0
    on_bar = False

    while count < 3:
        on_now = color_sensor.reflection(port.C) < THRESHOLD
        if on_now and not on_bar:
            count += 1
            print("Bars counted:", count)
        on_bar = on_now

        turn_amount = motion_sensor.tilt_angles()[0] / 10 * KP
        motor_pair.move_tank(motor_pair.PAIR_1, int(SPEED + turn_amount), int(SPEED - turn_amount))
        await runloop.sleep_ms(10)

    motor_pair.stop(motor_pair.PAIR_1)
    print("Done crossing, total bars:", count)
    await drive_straight(obs)


runloop.run(drive_straight(0))