# 通过SPI连接bmp388和esp32
#
# warning:
#   this demo 只支持python3
#   run this demo : python3 SPIReadTemperature.py
#
# connect:
#   raspberry       bmp388
#   CS  (15)        CSB
#   3.3v(17)        VCC
#   MOSI(19)        SDI
#   MISO(21)        SDO
#   SCLK(23)        SCK
#   GND (25)        GND

import bmp388
import time

#define chip selection pins
cs = 22

#create SPI通信的bmp388 object
bmp388 = bmp388.DFRobot_BMP388_SPI(cs)

#read temperature and print it
while 1:
  temp = bmp388.readTemperature()
  print("Temperature : %s" %temp)  
  time.sleep(0.5)