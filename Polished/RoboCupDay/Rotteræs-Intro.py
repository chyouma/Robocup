from hub import port
import runloop
import motor_pair
import color_sensor
import color


"""
888b     d888 8888888b.           888888b.    .d88888b.  888b     d888 888888b.         d8888  .d8888b. 88888888888 8888888 .d8888b.  
8888b   d8888 888   Y88b          888  "88b  d88P" "Y88b 8888b   d8888 888  "88b       d88888 d88P  Y88b    888       888  d88P  Y88b 
88888b.d88888 888    888          888  .88P  888     888 88888b.d88888 888  .88P      d88P888 Y88b.         888       888  888    888 
888Y88888P888 888   d88P          8888888K.  888     888 888Y88888P888 8888888K.     d88P 888  "Y888b.      888       888  888        
888 Y888P 888 8888888P"           888  "Y88b 888     888 888 Y888P 888 888  "Y88b   d88P  888     "Y88b.    888       888  888        
888  Y8P  888 888 T88b            888    888 888     888 888  Y8P  888 888    888  d88P   888       "888    888       888  888    888 
888   "   888 888  T88b  d8b      888   d88P Y88b. .d88P 888   "   888 888   d88P d8888888888 Y88b  d88P    888       888  Y88b  d88P 
888       888 888   T88b Y8P      8888888P"   "Y88888P"  888       888 8888888P" d88P     888  "Y8888P"     888     8888888 "Y8888P
"""


"""
SETTINGS
"""
obs = 0 # Cheks for current challenge

motor_pair.pair(motor_pair.PAIR_1, port.B, port.A) # Motor A and B (from port a and b) is paired as PAIR_1

async def forhin1():

    """
    FORHINDRING 1
    Sindssyg hidsig bombastic ashh intro - MR. BOMBASTIC
    """

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 1080, 0, 600)


    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 600, 0)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 0, 600)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 600, 0)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 0, 600)


    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 1080, 600, 0)


    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 600, 0)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 0, 600)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 600, 0)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 0, 600)


    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 1080, 0, 600)


    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 600, 0)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 0, 600)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 600, 0)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 0, 600)


    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 1080, 600, 0)


    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 600, 0)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 0, 600)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 600, 0)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 0, 600)


    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 1080, 0, 600)


    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 600, 0)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 0, 600)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 600, 0)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 0, 600)


    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 1080, 600, 0)


    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 600, 0)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 0, 600)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 600, 0)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 0, 600)


    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 1080, 0, 600)


    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 600, 0)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 0, 600)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 600, 0)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 0, 600)


    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 1080, 600, 0)


    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 600, 0)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 0, 600)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 600, 0)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 0, 600)


    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 1080, 0, 600)


    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 600, 0)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 0, 600)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 600, 0)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 0, 600)


    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 1080, 600, 0)


    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 600, 0)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 0, 600)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 600, 0)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 0, 600)


async def forhin2():

    """
    FORHINDRING 2
    LIGMA
    """
    while True:
        print("LIGMA")

# De forskellige challenges der kører og hvonrår osv.
def grå_linje():

    motor_pair.move_tank(
    motor_pair.PAIR_1,
    color_sensor.reflection(port.C)*18,
    color_sensor.reflection(port.D)*18
    )

    if color_sensor.color(port.D) is color.BLUE and color_sensor.color(port.D) is color.BLUE:
        motor_pair.move_tank(
        motor_pair.PAIR_1,
        800,
        800
        )
        return False

    return(color_sensor.reflection(port.C) < 7
    and color_sensor.reflection(port.D) < 7 and color_sensor.color(port.C) is color.BLACK and color_sensor.color(port.D) is color.BLACK)

async def main():
    """
    KØR FORHINDRING
    """
    print("Forhindring nummer:", obs)

    forhindringer = [
        forhin1,
        forhin2
    ]
    for forhin in forhindringer:
        await runloop.until(grå_linje)
        await forhin()

    else:
        print("Ingen kode til forhindring:", obs)

runloop.run(main()) # Programmet er more or less det hovedprogram der køres, når der ikke er en aktiv challenge.
