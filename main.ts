let LightsOn = false
input.onSound(DetectedSound.Loud, function () {
    LightsOn = !(LightsOn)
    if (LightsOn) {
        basic.showLeds(`
            # . . . #
            # . . . #
            # # # # #
            # . . . #
            # . . . #
            `)
        basic.showLeds(`
            # # # # #
            # . . . .
            # # # . .
            # . . . .
            # # # # #
            `)
    } else {
        basic.clearScreen()
    }
})
