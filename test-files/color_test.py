from hub import light_matrix, port
import runloop
import color_sensor
import motor_pair

async def main():
    # write your code here
    while True:

        left = color_sensor.reflection(port.C)
        right = color_sensor.reflection(port.D)

        if left > 75 and right > 75:
            # Both on white → drive straight
            motor_pair.move(motor_pair.PAIR_1, 0, velocity=550)

        elif left <= 75 and right > 75:
            # Left is off white → turn left
            motor_pair.move(motor_pair.PAIR_1, 40, velocity=100)

        elif left > 75 and right <= 75:
            # Right is off white → turn right
            motor_pair.move(motor_pair.PAIR_1, -40, velocity=100)

        else:
            # Both off white → stop
            motor_pair.stop(motor_pair.PAIR_1, stop=motor_pair.BRAKE)

        await runloop.sleep_ms(10)

runloop.run(main())
