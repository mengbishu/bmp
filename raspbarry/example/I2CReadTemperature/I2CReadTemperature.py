# 通过I2C连接bmp388和esp32
#
# warning:
#   this demo 只支持python3
#   run this demo : python3 I2CreadTemperature.py
#
# connect:
#   raspberry       bmp388
#   3.3v(1)         VCC
#   GND(6)          GND
#   SCL(5)          SCL
#   SDA(3)          SDA


import bmp388
import time

#create I2C通信的bmp388 object
bmp388 = bmp388.DFRobot_BMP388_I2C()

#read temperature and print it
while 1:
  temp = bmp388.readTemperature()
  print("Temperature : %s" %temp)
  time.sleep(0.5)