 /*!
  * file readTemperature.ino
  * 
  * 将BMP388连接到Arduino的I2C接口上, 下载程序
  * @n 打开 serial monitor 可以看到检测的温度.
  *
  * Copyright   [DFRobot](http://www.dfrobot.com), 2016
  * Copyright   GNU Lesser General Public License
  *
  * version  V0.1
  * date  2018-5-29
  */
#include "DFRobot_BMP388.h"
#include "Wire.h"

/*创建一个I2C通信的bmp388对象*/
DFRobot_BMP388 bmp388;

void setup(){
  /*串口初始化*/
  Serial.begin(9600);
  /*bmp388初始化*/
  bmp388.begin();
}

void loop(){
  /*读取温度,并通过串口打印数据*/
  float Temperature = bmp388.readTemperature();
  Serial.print("Temperature : ");
  Serial.println(Temperature);
  delay(100);
}