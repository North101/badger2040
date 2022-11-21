from adafruit_neokey.neokey1x4 import NeoKey1x4
from adafruit_seesaw.digitalio import DigitalIO
from adafruit_seesaw.neopixel import NeoPixel
from adafruit_seesaw.rotaryio import IncrementalEncoder
from adafruit_seesaw.seesaw import Seesaw
from rainbowio import colorwheel

from pimoroni_i2c import PimoroniI2C
from pimoroni import BREAKOUT_GARDEN_I2C_PINS


def start():
  i2c = PimoroniI2C(**BREAKOUT_GARDEN_I2C_PINS)

  seesaw = Seesaw(i2c, 0x36)
  encoder = IncrementalEncoder(seesaw)
  encoder_pixel = NeoPixel(seesaw, 6, 1)
  encoder_pixel.brightness = 0
  encoder_pixel.fill(colorwheel(encoder.position % 256))
  encoder_switch = DigitalIO(seesaw, 24)

  neokey = NeoKey1x4(i2c, 0x30)
  keys = [
      (neokey, 0, 0),
      (neokey, 1, 64),
      (neokey, 2, 128),
      (neokey, 3, 192),
  ]

  off = (0, 0, 0)

  last_position = encoder.position
  while True:
    position = encoder.position

    for (neokey, key, color) in keys:
      if neokey[key]:
        print(f'Button: {key}')
        neokey.pixels[key] = colorwheel((color + encoder.position) % 256)
      else:
        neokey.pixels[key] = off

    if last_position != position:
      print(f'Rotary: {position}')
      encoder_pixel.fill(colorwheel(position % 256))
      if last_position is not None:
        encoder_pixel.brightness = 0.1
      last_position = position

    if encoder_pixel.brightness > 0:
      encoder_pixel.brightness -= 0.01
    
    if not encoder_switch.value:
      print('Rotary: Pressed')
      encoder_pixel.brightness = 0.1
