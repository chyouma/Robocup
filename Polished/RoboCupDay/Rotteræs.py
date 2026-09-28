from hub import port, sound
import runloop
import motor_pair
import color_sensor
import color


"""

8888888b.   .d88888b. 88888888888 88888888888 8888888888 8888888b.         d88888888888 .d8888b.      8888888b. Y88b   d88P 
888   Y88b d88P" "Y88b    888         888     888        888   Y88b       d88888       d88P  Y88b     888   Y88b Y88b d88P  
888    888 888     888    888         888     888        888    888      d88P888       Y88b.          888    888  Y88o88P   
888   d88P 888     888    888         888     8888888    888   d88P     d88P 8888888    "Y888b.       888   d88P   Y888P    
8888888P"  888     888    888         888     888        8888888P"     d88P  888           "Y88b.     8888888P"     888     
888 T88b   888     888    888         888     888        888 T88b     d88P   888             "888     888           888     
888  T88b  Y88b. .d88P    888         888     888        888  T88b   d8888888888       Y88b  d88P d8b 888           888     
888   T88b  "Y88888P"     888         888     8888888888 888   T88b d88P     8888888888 "Y8888P"  Y8P 888           888  

"""

"""
SETTINGS
"""
# Test RGBI og reflektion
#print(color_sensor.reflection(port.D))
#print(color_sensor.reflection(port.C))
#
#print(color_sensor.rgbi(port.D))
#print(color_sensor.rgbi(port.C))
#GRAA = (155, 152, 158, 359)
#GRAA = (126, 125, 128, 288)

obs = 0 # Cheks for current challenge

motor_pair.pair(motor_pair.PAIR_1, port.B, port.A) # Motor A and B (from port a and b) is paired as PAIR_1

async def forhin1():
    """
    FORHINDRING 1
    Brudt streg 1/2
    """
    print("Starter opgave 1")
    # Drej til højre
    await motor_pair.move_tank_for_degrees(
        motor_pair.PAIR_1,
        180,    # Grader, som hjul(et/ene) dreger i alt
        0,    # Hastighed Højre
        200    # Hastighed Venstre
    )
    # Kør hen til streg
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 410, 400, 400)

    # Ryk lidt længere frem, så robotten kommer hen på stregen
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 105, 210, 0)

    print("Opgave 1 færdig")

async def forhin2():
    """
    FORHINDRING 2
    Brudt streg 2/2
    """

    print("Starter opgave 2")

    # Drej til højre
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 180, 200, 0)

    # Kør hen til streg
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 410, 400, 400)

    # Ryk lidt længere frem, så robotten kommer hen på stregen
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 105, 0, 210)

    print("Opgave 2 færdig")


async def forhin3():
    """
    FORHINDRING 3
    Skub Flske
    """

    print("Starter forhindring 3")

    # Kør lidt frem
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 185, 120, 120)

    # Drej skarpt til højre
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 0, 120)

    print("Forhindring 3 færdig")


async def forhin4():
    """
    FORHINDRING 4
    Tilbage fra flaske(/bak)
    """
    print("Starter forhindring 4")

    # Bak
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, -1040, 200, 200)

    # Ret hen, og "SLIP"
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 245, 200, -200)
    print("Forhindring 4 færdig")

    # Ryk lidt frem
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 140, 100, 120)
    print("Forhindring 4 færdig")


async def forhin5():
    """
    FORHINDRING 5
    Drej imod vippe
    """

    print("Starter forhindring 5")
    # Samme kode som flasken, da den bare skal dreje til venstre istedet for højre, og finde stregen

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 185, 120, 120)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 270, 120, 0)
    print("Forhindring 5 færdig")

async def forhin6():
    """
    FORHINDRING 6
    Vippe
    """

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 400, 600, 600)

    røv = 3140
    while røv >= 0:

        await motor_pair.move_tank_for_degrees(
        motor_pair.PAIR_1,
        70,
        color_sensor.reflection(port.C)*18,
        color_sensor.reflection(port.D)*18
        )
        røv -= 70

 
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 250, 180, 0)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 200, 120, 120)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 20, 180, 0)

    print("Forhindring 6 færdig")

async def forhin7():
    """
    FORHINDRING 7
    4-parralelle streger*?
    """
    print("Starter opgave 7")
    # Drej til højre
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 180, 200, 0)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 400, 400, 400)

    # Ryk lidt længere frem, så robotten kommer hen på stregen
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 100, 10, 200)
    print("Forhindring 7 færdig")

async def forhin8():
    """
    FORHINDRING 8
    Skydeskive
    """

    print("Starter forhindring 8")

    #
    # Cirkelkode
    #

    # Robotten springer over cirklen, da koden ikke er skrevet
    await motor_pair.move_tank_for_degrees(
        motor_pair.PAIR_1,
        100,
        200,
        200
    )

    print("Forhindring 8 færdig")


async def forhin9():
    """
    FORHINDRING 9
    Omkring flaske
    """
    print("Starter forhindring 9")
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 180, -20, 200)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 100, 200, 200)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 1450, 430, 300)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 300, 80, 450)
    print("Forhindring 9 færdig")


async def forhin10():
    """
    FORHINDRING 10
    Vægge
    """
    print("Starter forhindring 10")
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 800, 200, 200)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 180, 200, -20)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 100, 200, 200)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 1360, 290, 460)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 480, 460, 90)
    print("Forhindring 10 færdig")



async def forhin11():
    """
    FORHINDRING 11
    Omkring flaske
    """
    print("Starter forhindring 11")
    await motor_pair.move_tank_for_degrees(
        motor_pair.PAIR_1,
        180,
        200,
        -20
    )

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 100, 200, 200)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 1380, 300, 430)

    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 300, 470, 100)
    print("Forhindring 11 færdig")


async def forhin12():
    """
    FORHINDRING 12
    "Jesus, take the wheel!"
    """
    print("Starter forhindring 12")
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 3200, 420, 420)

    # LA MUSIKA #
    TICKS_PER_BEAT = 384
    TEMPO_US_PER_BEAT = 272727
    VOLUME = 100
    SPEED = 1.0

    SONG = [(71, 96), (69, 288), (67, 96), (64, 288), (62, 96), (64, 192), (-1, 480), (71, 96),
        (69, 288), (67, 96), (64, 288), (62, 96), (64, 192), (-1, 480), (71, 96), (69, 288),
        (67, 96), (64, 288), (62, 96), (64, 192), (-1, 192), (67, 192), (-1, 192), (69, 192),
        (-1, 192), (71, 192), (-1, 192), (69, 192), (-1, 480), (71, 96), (69, 288), (67, 96),
        (64, 288), (62, 96), (64, 192), (-1, 480), (71, 96), (69, 288), (67, 96), (64, 288),
        (62, 96), (64, 192), (-1, 480), (64, 96), (67, 288), (69, 96), (71, 288), (74, 96),
        (76, 192), (-1, 192), (74, 192), (-1, 192), (76, 192), (-1, 192), (79, 192), (-1, 192),
        (81, 192), (-1, 480), (83, 96), (81, 288), (79, 96), (76, 288), (74, 96), (76, 192),
        (-1, 480), (83, 96), (81, 288), (79, 96), (76, 288), (74, 96), (76, 192), (-1, 480),
        (83, 96), (81, 288), (79, 96), (76, 288), (74, 96), (76, 192), (-1, 192), (79, 192),
        (-1, 192), (81, 192), (-1, 192), (83, 192), (-1, 192), (81, 192), (-1, 480), (83, 96),
        (81, 288), (79, 96), (76, 288), (74, 96), (76, 192), (-1, 480), (83, 96), (81, 288),
        (79, 96), (76, 288), (74, 96), (76, 192), (-1, 480), (76, 96), (79, 288), (81, 96),
        (83, 288), (86, 96), (88, 192), (-1, 192), (86, 192), (-1, 192), (88, 192), (-1, 192),
        (91, 192), (-1, 192), (93, 192), (-1, 1248), (74, 96), (76, 192), (-1, 192), (76, 192),
        (-1, 192), (76, 192), (-1, 192), (76, 192), (-1, 96), (74, 96), (76, 288), (79, 96),
        (76, 192), (-1, 192), (74, 192), (-1, 192), (71, 192), (-1, 96), (74, 96), (76, 192),
        (-1, 192), (76, 192), (-1, 192), (76, 192), (-1, 192), (76, 192), (-1, 96), (74, 96),
        (76, 288), (88, 96), (86, 192), (-1, 192), (83, 192), (-1, 192), (81, 192), (-1, 192),
        (83, 192), (-1, 192), (83, 192), (-1, 192), (83, 192), (-1, 192), (83, 192), (-1, 96),
        (81, 96), (83, 288), (86, 96), (83, 192), (-1, 192), (81, 192), (-1, 192), (79, 192),
        (-1, 96), (81, 96), (83, 192), (-1, 192), (83, 192), (-1, 192), (83, 192), (-1, 192),
        (83, 192), (-1, 96), (81, 96), (83, 288), (86, 96), (83, 192), (-1, 192), (81, 192),
        (-1, 192), (79, 192), (-1, 96), (74, 96), (76, 192), (-1, 192), (76, 192), (-1, 192),
        (76, 192), (-1, 192), (76, 192), (-1, 96), (74, 96), (76, 288), (79, 96), (76, 192),
        (-1, 192), (74, 192), (-1, 192), (71, 192), (-1, 96), (74, 96), (76, 192), (-1, 192),
        (76, 192), (-1, 192), (76, 192), (-1, 192), (76, 192), (-1, 96), (74, 96), (76, 288),
        (88, 96), (86, 192), (-1, 192), (83, 192), (-1, 192), (81, 192), (-1, 96), (81, 96),
        (83, 192), (-1, 192), (83, 192), (-1, 192), (83, 288), (81, 96), (79, 288), (81, 96),
        (83, 192), (-1, 192), (83, 192), (-1, 192), (83, 288), (81, 96), (79, 288), (81, 96),
        (83, 192), (-1, 192), (83, 192), (-1, 192), (83, 192), (-1, 192), (83, 192), (-1, 192),
        (83, 192), (-1, 1344), (40, 672), (71, 768), (62, 96), (72, 1440), (62, 96), (66, 384),
        (67, 192), (66, 192), (69, 384), (71, 192), (69, 96), (-1, 96), (69, 192), (61, 480),
        (71, 768), (62, 96), (64, 192), (62, 480), (71, 768), (62, 96), (72, 1440), (74, 96),
        (76, 192), (69, 192), (74, 192), (69, 192), (76, 192), (69, 192), (79, 192), (69, 96),
        (-1, 96), (81, 192), (71, 480), (83, 96), (81, 288), (79, 96), (76, 288), (74, 96),
        (76, 192), (71, 480), (83, 96), (81, 288), (79, 96), (76, 288), (74, 96), (76, 192),
        (72, 480), (83, 96), (81, 288), (79, 96), (76, 288), (74, 96), (76, 192), (69, 192),
        (79, 192), (69, 192), (81, 192), (69, 192), (83, 192), (69, 96), (-1, 96), (81, 192),
        (71, 480), (83, 96), (81, 288), (79, 96), (76, 288), (74, 96), (76, 192), (71, 480),
        (83, 96), (81, 288), (79, 96), (76, 288), (74, 96), (76, 192), (72, 480), (76, 96),
        (79, 288), (81, 96), (83, 288), (86, 96), (88, 192), (69, 192), (86, 192), (69, 192),
        (88, 192), (69, 192), (91, 192), (69, 96), (-1, 96), (93, 192), (71, 1248), (74, 96),
        (76, 192), (72, 192), (76, 192), (72, 192), (76, 192), (72, 192), (76, 192), (72, 96),
        (74, 96), (76, 288), (79, 96), (76, 192), (72, 192), (74, 192), (72, 480), (74, 96),
        (76, 192), (69, 192), (76, 192), (69, 192), (76, 192), (69, 192), (76, 192), (69, 96),
        (74, 96), (76, 288), (88, 96), (86, 192), (69, 192), (83, 192), (69, 192), (81, 192),
        (69, 96), (-1, 96), (83, 192), (71, 192), (83, 192), (71, 192), (83, 192), (71, 192),
        (83, 192), (71, 96), (81, 96), (83, 288), (86, 96), (83, 192), (71, 192), (81, 192),
        (71, 192), (79, 192), (71, 96), (81, 96), (83, 192), (71, 192), (83, 192), (71, 192),
        (83, 192), (71, 192), (83, 192), (71, 96), (81, 96), (83, 288), (86, 96), (83, 192),
        (71, 192), (81, 192), (71, 192), (79, 192), (71, 96), (74, 96), (76, 192), (72, 192),
        (76, 192), (72, 192), (76, 192), (72, 192), (76, 192), (72, 96), (74, 96), (76, 288),
        (79, 96), (76, 192), (72, 192), (74, 192), (72, 480), (74, 96), (76, 192), (73, 192),
        (76, 192), (73, 192), (76, 192), (73, 192), (76, 192), (73, 96), (74, 96), (76, 288),
        (88, 96), (86, 192), (73, 192), (83, 192), (73, 192), (81, 192), (73, 96), (81, 96),
        (83, 192), (71, 192), (83, 192), (71, 192), (83, 288), (81, 96), (79, 288), (81, 96),
        (83, 192), (71, 192), (83, 192), (71, 192), (83, 288), (81, 96), (79, 288), (81, 96),
        (83, 192), (-1, 192), (83, 192), (-1, 192), (83, 192), (-1, 192), (83, 192), (-1, 192),
        (83, 192), (-1, 480), (71, 96), (69, 288), (67, 96), (64, 288), (62, 96)]


    def midi_to_hz(note):
        return round(440 * (2 ** ((note - 69) / 12)))

    def ticks_to_ms(ticks):
        return max(
            1,
            round(ticks * TEMPO_US_PER_BEAT / TICKS_PER_BEAT / 1000 * SPEED)
        )

    async def main2():
        for note, ticks in SONG:
            duration = ticks_to_ms(ticks)
            if note < 0:
                await runloop.sleep_ms(duration)
            else:
                await sound.beep(midi_to_hz(note), duration, VOLUME)
    runloop.run(main2())

    await motor_pair.move_tank_for_degrees(
        motor_pair.PAIR_1,
        9999999999,
        500,
        5
        )

    motor_pair.stop(motor_pair.PAIR_1)

    print("Forhindring 12 færdig")

async def forhin13():

    """
    FORHINDRING 13
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
        forhin2,
        forhin3,
        forhin4,
        forhin5,
        forhin6,
        forhin7,
        forhin8,
        forhin9,
        forhin10,
        forhin11,
        forhin12,
        forhin13
    ]
    for forhin in forhindringer:
        await runloop.until(grå_linje)
        await forhin()

    else:
        print("Ingen kode til forhindring:", obs)

runloop.run(main()) # Programmet er more or less det hovedprogram der køres, når der ikke er en aktiv challenge.
