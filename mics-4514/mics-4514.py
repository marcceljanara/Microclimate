# -*- coding:utf-8 -*-
'''!
  @file get_gas_ppm.py
  @brief Read gas concentration unit(PPM).
  @n step: we must first determine the i2c device address, will dial the code switch A0, A1 (MICS_ADDRESS_0 for [0 0]), (MICS_ADDRESS_1 for [1 0]), (MICS_ADDRESS_2 for [0 1]), (MICS_ADDRESS_3 for [1 1]).
  @n       Then wait for the calibration to succeed.
  @n       The calibration time is approximately three minutes.
  @copyright Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license The MIT License (MIT)
  @author [ZhixinLiu](zhixin.liu@dfrobot.com)
  @version V1.2
  @date 2021-6-18
  @url https://github.com/DFRobot/DFRobot_MICS
'''
import sys
import os
sys.path.append("../")
from DFRobot_MICS import *
import time

CALIBRATION_TIME = 0x03            # calibration time
I2C_BUS          = 0x01            # default use I2C1
'''
   The first  parameter is to select i2c0 or i2c1
   The second parameter is the i2c device address
   The default address for i2c is MICS_ADDRESS_0
     MICS_ADDRESS_0              0x75
     MICS_ADDRESS_1              0x76
     MICS_ADDRESS_2              0x77
     MICS_ADDRESS_3              0x78
'''
mics = DFRobot_MICS_I2C (I2C_BUS ,MICS_ADDRESS_0)

interval = 598
def setup():
  '''
    Gets the power mode of the sensor
    The sensor is in sleep mode when power is on,so it needs to wake up the sensor. 
    The data obtained in sleep mode is wrong
  '''
  if mics.get_power_mode() == SLEEP_MODE:
    mics.wakeup_mode()
    #print("wake up sensor success")
    pass
  else:
    #print("the sensor is wake up mode")
    pass

  '''
    Do not touch the sensor probe when preheating the sensor.
    Place the sensor in clean air.
    The default calibration time is 3 minutes.
  '''
  mics.warm_up_time(CALIBRATION_TIME)

def loop():
  global start_time
  '''
    Type of detection gas
    CO       = 0x01  (Carbon Monoxide)
    CH4      = 0x02  (Methane)
    C2H5OH   = 0x03  (Ethanol)
    H2       = 0x06  (Hydrogen)
    NH3      = 0x08  (Ammonia)
    NO2      = 0x0A  (Nitrogen Dioxide)
  '''
  if time.time() - start_time >= interval:
    mics.wakeup_mode()
    time.sleep(2)
    # Read gas in ppm 
    # Read gas CO
    gas_CO = mics.get_gas_ppm(CO)
    # Read gas CH4
    gas_CH4 = mics.get_gas_ppm(CH4)
    # Read gas C2H5OH
    gas_C2H5OH = mics.get_gas_ppm(C2H5OH)
    # Read gas H2
    gas_H2 = mics.get_gas_ppm(H2)
    # Read gas NH3
    gas_NH3 = mics.get_gas_ppm(NH3)
    # Read gas NO2
    gas_NO2 = mics.get_gas_ppm(NO2)

    #send data to std:out
    data = f"{round(gas_CO,1)} {round(gas_CH4,1)} {round(gas_C2H5OH,1)} {round(gas_H2,1)} {round(gas_NH3,1)} {round(gas_NO2,1)}"
    encode_data = data.encode('utf-8')
    print(encode_data)
    start_time = time.time()
  else:
    mics.sleep_mode()


if __name__ == "__main__":
  setup()
  time.sleep(50)
  # Read gas CO
  gas_CO = mics.get_gas_ppm(CO)
  # Read gas CH4
  gas_CH4 = mics.get_gas_ppm(CH4)
  # Read gas C2H5OH
  gas_C2H5OH = mics.get_gas_ppm(C2H5OH)
  # Read gas H2
  gas_H2 = mics.get_gas_ppm(H2)
  # Read gas NH3
  gas_NH3 = mics.get_gas_ppm(NH3)
  # Read gas NO2
  gas_NO2 = mics.get_gas_ppm(NO2)

  #send data to std:out
  data = f"{round(gas_CO,1)} {round(gas_CH4,1)} {round(gas_C2H5OH,1)} {round(gas_H2,1)} {round(gas_NH3,1)} {round(gas_NO2,1)}"
  encode_data = data.encode('utf-8')
  print(encode_data)
  
  start_time = time.time()
  while True:
    loop()
