import bmp388
from machine import Pin,SPI
import time

D3 = 26

spi = SPI(baudrate=100000, polarity=1, phase=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
cs = Pin(D3,Pin.OUT)
bmp388 = bmp388.DFRobot_BMP388_SPI(spi,cs)
while 1:
  pressure = bmp388.readPressure();
  elevation = 44330 * (1.0 - pow(pressure / 101325, 0.1903))
  print(elevation)
  time.sleep(0.5)
