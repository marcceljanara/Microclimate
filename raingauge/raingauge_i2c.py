# -*- coding: utf-8 -*
'''!
  @file  read_data.py
  @brief Get the raw data, which is the tipping bucket count of rainfall, in units of counts.
  @copyright   Copyright (c) 2021 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license     The MIT License (MIT)
  @author      [fary](feng.yang@dfrobot.com)
  @version     V1.0
  @date        2023-01-28
  @url         https://github.com/DFRobor/DFRobot_RainfallSensor
'''
from __future__ import print_function
import sys
sys.path.append("../")
import time

from DFRobot_RainfallSensor import *

#sensor=DFRobot_RainfallSensor_UART()
sensor=DFRobot_RainfallSensor_I2C()
interval = 600

def setup():
  while (sensor.begin() == False):
    print("tidak_terdeteksi")
    time.sleep(600)
  print(0.0)

  #Get the raw data, which is the tipping bucket count of rainfall, in units of counts.
  #sensor.set_rain_accumulated_value(0.2794)
# Inisialisasi last_value dengan None pada awal program
last_value = None
rainCount = 0

def loop():
    global last_value  # Untuk mengakses variabel last_value di luar fungsi
    global start_time
    global rainCount

    # Get the raw data, which is the tipping bucket count of rainfall, in units of counts.
    rainfall_raw = sensor.get_raw_data()

    if last_value is not None:
        # Menghitung selisih antara data saat ini dengan data sebelumnya
        per_tip_rainfall = rainfall_raw - last_value
        rainCount += per_tip_rainfall

    # Update last_value dengan data saat ini
    last_value = rainfall_raw

    if time.time() - start_time >= interval:
       mm = 0.3 * rainCount
       print(round(mm,3))
       rainCount = 0
       start_time = time.time()

if __name__ == "__main__":
  time.sleep(240)
  setup()
  start_time = time.time()
  while True:
    loop()
