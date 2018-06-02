import bmp388
from machine import Pin,SPI
import time

D3 = 26
spi = SPI(baudrate=100000, polarity=1, phase=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
cs = Pin(D3,Pin.OUT)
bmp388 = bmp388.DFRobot_BMP388_SPI(spi,cs)

while 1:
  temp = bmp388.readTemperature()
  print("Temperature : %s" %temp)
  time.sleep(0.5)