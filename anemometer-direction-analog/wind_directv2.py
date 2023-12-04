import sys
sys.path.append('../')
import time
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from DFRobot_ADS1115 import ADS1115
ADS1115_REG_CONFIG_PGA_6_144V        = 0x00 # 6.144V range = Gain 2/3

def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def map_direction(adc_value):
    direction = map_value(adc_value, 0, 4710, 0, 360)

    if (0 <= direction < 11.3) or (348.8 <= direction <= 360):
        return "Utara"
    elif 11.3 <= direction < 33.8:
        return "Utara_Timur_Laut"
    elif 33.8 <= direction < 56.3:
        return "Timur_Laut"
    elif 56.3 <= direction < 78.8:
        return "Timur_Timur_Laut"
    elif 78.8 <= direction < 101.3:
        return "Timur"
    elif 101.3 <= direction < 123.8:
        return "Timur_Tenggara"
    elif 123.8 <= direction < 146.3:
        return "Tenggara"
    elif 146.3 <= direction < 168.8:
        return "Selatan_Tenggara"
    elif 168.8 <= direction < 191.3:
        return "Selatan"
    elif 191.3 <= direction < 213.8:
        return "Selatan_Barat_Daya"
    elif 213.8 <= direction < 236.3:
        return "Barat_Daya"
    elif 236.3 <= direction < 258.8:
        return "Barat_Barat_Daya"
    elif 258.8 <= direction < 281.3:
        return "Barat"
    elif 281.3 <= direction < 303.8:
        return "Barat_Barat_Laut"
    elif 303.8 <= direction < 326.3:
        return "Barat_Laut"
    elif 326.3 <= direction < 348.8:
        return "Utara_Barat_Laut"

while True :
    try:
        #Set the IIC address
        ads1115.set_addr_ADS1115(0x48)
        #Sets the gain and input voltage range.
        ads1115.set_gain(ADS1115_REG_CONFIG_PGA_6_144V)
        #Get the Digital Value of Analog of selected channel
        adc1 = ads1115.read_voltage(1)
        sensor_value = adc1['r']
        direction = map_value(sensor_value,0,4710,0,360)
        wind_direction = map_direction(sensor_value)
        print(wind_direction,round(direction,1))
    except Exception as e:
        print("tidak_terdeteksi",0.0)
    time.sleep(1)
