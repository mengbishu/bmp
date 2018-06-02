#通过SPI连接bmp388和esp32
#download bmp388.py and downloadAndRun this demo

import bmp388
from machine import Pin,SPI
import time

#selection pin D3/pin26
D3 = 26

#create SPI object
spi = SPI(baudrate=100000, polarity=1, phase=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))

#将片选引脚设置为输出模式
cs = Pin(D3,Pin.OUT)

#create SPI通信的bmp388 object
bmp388 = bmp388.DFRobot_BMP388_SPI(spi,cs)

#read pressure and count elevation
while 1:
  pressure = bmp388.readPressure();
  elevation = 44330 * (1.0 - pow(pressure / 101325, 0.1903))
  print(elevation)
  time.sleep(0.5)
