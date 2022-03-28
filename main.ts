let strip: neopixel.Strip = null
let Blue = 0
let Green = 0
let Red = 0
basic.forever(function () {
    mbit_Robot.CarCtrlSpeed(mbit_Robot.CarState.Car_Run, 255)
})
basic.forever(function () {
    strip.show()
    strip.rotate(1)
    basic.pause(500)
})
basic.forever(function () {
    strip = neopixel.create(DigitalPin.P16, 3, NeoPixelMode.RGB)
    Blue = randint(-255, 255)
    Green = randint(-255, 255)
    Red = randint(-255, 255)
    for (let index = 0; index < 101; index++) {
        strip.setPixelColor(0, neopixel.rgb(Red, Green, Blue))
        Blue += randint(-255, 255)
        Red += randint(-255, 255)
        Green += randint(-255, 255)
    }
    for (let index = 0; index < 101; index++) {
        strip.setPixelColor(1, neopixel.rgb(Red, Green, Blue))
        Blue += randint(-255, 255)
        Red += randint(-255, 255)
        Green += randint(-255, 255)
    }
    for (let index = 0; index < 101; index++) {
        strip.setPixelColor(2, neopixel.rgb(Red, Green, Blue))
        Blue += randint(-255, 255)
        Red += randint(-255, 255)
        Green += randint(-255, 255)
    }
})
