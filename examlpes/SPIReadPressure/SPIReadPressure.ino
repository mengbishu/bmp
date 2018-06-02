 /*!
  * file readPressure.ino
  * 
  * 将BMP388连接到Arduino的SPI接口上, 下载程序
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

/*创建一个spi接口的bmp388对象,spi的片选引脚为3*/
DFRobot_BMP388 bmp388(3);
void setup(){
  while(!Serial);
  Serial.begin(9600);
  /*bmp388初始化*/
  bmp388.begin();
}

void loop(){
  /*读取大气压,并通过串口打印数据*/
  float Pressure = bmp388.readPressure();
  Serial.print("Pressure : ");
  Serial.println(Pressure);
  delay(100);
}