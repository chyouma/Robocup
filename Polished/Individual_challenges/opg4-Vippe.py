# Test til at komme op på vippen
from hub import port, motion_sensor
import runloop
import motor_pair

PITCH_THRESHOLD = 25  # pitch value that triggers "stop"

motor_pair.pair(motor_pair.PAIR_1, port.B, port.A)

async def forhin3(base_speed=200, correction_gain=3):
    print("forhin3 starting...")
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


runloop.run(forhin3())