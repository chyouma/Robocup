from hub import port
import distance_sensor
import motor_pair
import runloop

async def main():
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    # Capture the initial distance
    start_distance = distance_sensor.distance(port.E)

    # Target = half the original distance
    target_distance = start_distance / 2

    print("Starting distance:", start_distance)
    print("Target distance:", target_distance)

    # Drive forward until we're at half the distance
    while distance_sensor.distance(port.E) > target_distance:
        motor_pair.move(motor_pair.PAIR_1, 0, velocity=300)

    # Stop
    motor_pair.stop(motor_pair.PAIR_1)

    print("Final distance:", distance_sensor.distance(port.E))

runloop.run(main())