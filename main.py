strip: neopixel.Strip = None
Blue = 0
Green = 0
Red = 0

def on_forever():
    global strip, Blue, Green, Red
    strip = neopixel.create(DigitalPin.P16, 3, NeoPixelMode.RGB)
    Blue = randint(-255, 255)
    Green = randint(-255, 255)
    Red = randint(-255, 255)
    for index in range(101):
        strip.set_pixel_color(0, neopixel.rgb(Red, Green, Blue))
        Blue += randint(-255, 255)
        Red += randint(-255, 255)
        Green += randint(-255, 255)
    for index2 in range(101):
        strip.set_pixel_color(1, neopixel.rgb(Red, Green, Blue))
        Blue += randint(-255, 255)
        Red += randint(-255, 255)
        Green += randint(-255, 255)
    for index3 in range(101):
        strip.set_pixel_color(2, neopixel.rgb(Red, Green, Blue))
        Blue += randint(-255, 255)
        Red += randint(-255, 255)
        Green += randint(-255, 255)
basic.forever(on_forever)

def on_forever2():
    mbit_Robot.car_ctrl_speed(mbit_Robot.CarState.CAR_RUN, 255)
basic.forever(on_forever2)

def on_forever3():
    strip.show()
    strip.rotate(1)
    basic.pause(500)
basic.forever(on_forever3)
