LightsOn = False

def on_sound_loud():
    global LightsOn
    LightsOn = not (LightsOn)
    if LightsOn:
        basic.show_leds("""
            # . . . #
                        # . . . #
                        # # # # #
                        # . . . #
                        # . . . #
        """)
        basic.show_leds("""
            # # # # #
                        # . . . .
                        # # # . .
                        # . . . .
                        # # # # #
        """)
    else:
        basic.clear_screen()
input.on_sound(DetectedSound.LOUD, on_sound_loud)
