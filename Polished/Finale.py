from hub import port, motion_sensor
from hub import sound
import runloop
import motor_pair
import color_sensor
import color

"""

'sound' is imported.
The wanted music file just needs to be put where the user wants the music to start from.

"""

obs = 0
THRESHOLD = 75# reflection value below this = "on a bar" — tune on your mat
PITCH_THRESHOLD = 25

motor_pair.pair(motor_pair.PAIR_1, port.B, port.A)

async def grå_linje(obs):
    while True:
        if color_sensor.color(port.C) == color.BLACK or color_sensor.color(port.D) == color.BLACK:
            motor_pair.stop(motor_pair.PAIR_1)
            obs = obs + 1
            await forhin5(obs)
            continue
        else:
            motor_pair.move_tank(motor_pair.PAIR_1, color_sensor.reflection(port.D)*2, color_sensor.reflection(port.C)*2)
        await runloop.sleep_ms(10)

# Opgave 1 (brudt strej)
async def forhin1(obs):
    motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 100, 0 ,45)
    await runloop.sleep_tank_ms(500)

    motor_pair.move_tank(motor_pair.PAIR_1, 250, 250)
    count = 0
    on_bar = False

    while count < 1:
        reflection = color_sensor.reflection(port.C)
        currently_on_bar = reflection < THRESHOLD

        if currently_on_bar and not on_bar:
            count += 1
            print("Bars counted:", count)

        on_bar = currently_on_bar
        await runloop.sleep_ms(10)

    motor_pair.stop(motor_pair.PAIR_1)
    print("Done crossing, total bars:", count)
    await grå_linje(obs)


# Opgave 2 (brudt streg)
async def forhin2(obs):
    motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 45, 0 ,100)
    await runloop.sleep_tank_ms(500)

    motor_pair.move_tank(motor_pair.PAIR_1, 250, 250)
    count = 0
    on_bar = False

    while count < 1:
        reflection = color_sensor.reflection(port.C)
        currently_on_bar = reflection < THRESHOLD

        if currently_on_bar and not on_bar:
            count += 1
            print("Bars counted:", count)

        on_bar = currently_on_bar
        await runloop.sleep_ms(10)

    motor_pair.stop(motor_pair.PAIR_1)
    print("Done crossing, total bars:", count)
    await grå_linje(obs)

#Opgave 3 Skub flaske 
async def forhin3(obs):
    motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 45, 0 ,100)
    await runloop.sleep_tank_ms(500)

    motor_pair.move_tank(motor_pair.PAIR_1, 250, 250)
    count = 0
    on_bar = False

    while count < 1:
        reflection = color_sensor.reflection(port.C)
        currently_on_bar = reflection < THRESHOLD

        if currently_on_bar and not on_bar:
            count += 1
            print("Bars counted:", count)

        on_bar = currently_on_bar
        await runloop.sleep_ms(10)

    motor_pair.stop(motor_pair.PAIR_1)
    print("Done crossing, total bars:", count)
    await grå_linje(obs)

# Opgave 4 (vippe)
async def forhin4(base_speed=300, correction_gain=1): # mangler test

    # Starter med at køre ligeud, og korrigerer for yaw drift fra den initiale (nulstillede) yaw.

    print("forhin4 starting...")
    motion_sensor.reset_yaw(0) # nulstilning af yaw til 0 grader
    await runloop.sleep_ms(200)  # brief pause instead of waiting for motion_sensor.stable()

    while True:
        # Splitter vores tuple af (yaw, pitch, roll) ud i tre variabler
        yaw, pitch, roll = motion_sensor.tilt_angles()
        # Convertere decimal grader til grader (1/10) (why tf bruger de decimal grader 😭)
        yaw_deg = yaw * -0.1 # * -0.1 skifter fortegn, da yaw er negativt når robotten drejer til højre, 
        pitch_deg = pitch / 10  

        # Lowk samme som der bliver gjort længere oppe i grå_linje men med base_speed for at kontrollere (tjek med grå linje senere)
        correction = int(yaw_deg * correction_gain)
        left_speed = base_speed + correction
        right_speed = base_speed - correction

        print("driving | yaw:", yaw_deg, "pitch:", pitch_deg, "L/R:", left_speed, right_speed) # testing
        motor_pair.move_tank(motor_pair.PAIR_1, left_speed, right_speed)

        if pitch_deg >= PITCH_THRESHOLD: # mangler buffer melllem dette og tilbagevendelse til normal kørsel
            print("stop")
            motor_pair.stop(motor_pair.PAIR_1) 
            break

        await runloop.sleep_ms(10)



#Opgave "5" (4 streger)
async def forhin5(obs):
    motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 45, 0, 100)
    await runloop.sleep_ms(500)

    motor_pair.move_tank(motor_pair.PAIR_1, 250, 250)
    count = 0
    on_bar = False

    while count < 3:
        reflection = color_sensor.reflection(port.C)
        currently_on_bar = reflection < THRESHOLD

        if currently_on_bar and not on_bar:
            count += 1
            print("Bars counted:", count)

        on_bar = currently_on_bar
        await runloop.sleep_ms(10)

    motor_pair.stop(motor_pair.PAIR_1)
    print("Done crossing, total bars:", count)
    await grå_linje(obs)


async def main(x):
    if x == 1:
        print(1)
    elif x == 2:
        print(2)
    elif x == 3:
        await forhin3(x)
    elif x == 4:
        await forhin4(x)
    elif x==5:
        await forhin5(x)


runloop.run(grå_linje(obs))
