from hub import port
import runloop
import motor_pair
import color_sensor
import color

obs = 0
THRESHOLD = 75# reflection value below this = "on a bar" — tune on your mat
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


""""
i
"""

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
    elif x==5:
        await forhin5(x)


runloop.run(grå_linje(obs))