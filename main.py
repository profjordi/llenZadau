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
    elif VALOR == 3:
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
DAU1 = 0
basic.show_leds("""
    # . . . #
    . . . . .
    . . . . .
    . . . . .
    # . . . #
    """)

def on_forever():
    global DAU1
    basic.show_leds("""
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        """)
    while False:
        pass
    control.wait_micros(1000)
    while input.is_gesture(Gesture.SHAKE):
        control.wait_micros(500)
        basic.show_leds("""
            . . # . .
            . . # . .
            # # # # #
            . . # . .
            . . # . .
            """)
    basic.show_leds("""
        # # # # #
        # . . . #
        # . . . #
        # . . . #
        # # # # #
        """)
    control.wait_micros(500)
    DAU1 = randint(1, 6)
    _DAU(DAU1)
    control.wait_micros(5000)
basic.forever(on_forever)
