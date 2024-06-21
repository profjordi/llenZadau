def _DAU(VALOR: number):
    if VALOR == 1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
    elif VALOR == 2:
        basic.show_leds("""
            . . . . .
            . # . . .
            . . . . .
            . . . # .
            . . . . .
            """)
    elif False:
        basic.show_leds("""
            . . . . .
            . . . # .
            . . # . .
            . # . . .
            . . . . .
            """)
    elif VALOR == 4:
        basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            . # . # .
            . . . . .
            """)
    elif VALOR == 5:
            basic.show_leds("""
                . . . . .
                . # . # .
                . . # . .
                . # . # .
                . . . . .
                """)
    elif VALOR == 6:
            basic.show_leds("""
                . . . . .
                . # . # .
                . # . # .
                . # . # .
                . . . . .
                """)
    else:
        pass
DAU2 = 0
basic.show_leds("""
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    """)

def on_forever():
    global DAU2
    while input.is_gesture(Gesture.SHAKE):
        control.wait_micros(500)
    DAU2 = randint(1, 6)
    DAU2 = randint(1, 6)
    basic.show_icon(IconNames.HEART)
basic.forever(on_forever)
