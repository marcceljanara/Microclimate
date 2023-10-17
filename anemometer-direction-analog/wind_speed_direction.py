from DFRobot_ADS1115 import ADS1115
import time
ADS1115_REG_CONFIG_PGA_6_144V        = 0x00 # 6.144V range = Gain 2/3
ads1115 = ADS1115()

def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def map_direction(adc_value):
    direction = map_value(adc_value,0,4710,0,360)

    # Map the direction to 8 cardinal directions
    if (direction >= 338 or direction <= 23):
        return "Utara"
    elif direction >= 24 and direction <= 68:
        return "Timur_Laut"
    elif direction >= 69 and direction <= 113:
        return "Timur"
    elif direction >= 114 and direction <= 158:
        return "Tenggara"
    elif direction >= 159 and direction <= 203:
        return "Selatan"
    elif direction >= 204 and direction <= 248:
        return "Barat_Daya"
    elif direction >= 249 and direction <= 293:
        return "Barat"
    elif direction >= 294 and direction <= 337:
        return "Barat_Laut"

def main():
    while True:
        try:
            #Set the I2C address
            ads1115.set_addr_ADS1115(0x48)

            #Sets the gain and input voltage range.
            ads1115.set_gain(ADS1115_REG_CONFIG_PGA_6_144V ) # 6.144V range = Gain 2/3

            #Get the Digital Value of Analog of selected channel
            adc0 = ads1115.read_voltage(0)
            adc2 = ads1115.read_voltage(2)

            # read voltage
            sensor_value0 = adc0['r']
            sensor_value2 = adc2['r']
            
            # Wind Speed
            out_voltage = sensor_value0 /1000  # 4.096V adalah penuh skala ADC pada GAIN 2/3
            wind_speed_level = round(float(6 * out_voltage),3)  # Tingkat kecepatan angin berbanding lurus dengan tegangan keluaran sensor.
            if wind_speed_level <= 0:
                wind_speed_level = 0

            # Wind Direction
            direction = map_value(sensor_value2,0,4710,0,360)
            wind_direction = map_direction(sensor_value2)

            # Send serial
            print(wind_speed_level,wind_direction,int(direction))
            time.sleep(600)
        
        # Handling error
        except OSError:
            print('tidak_terdeteksi','tidak_terdeteksi','tidak_terdeteksi')
            time.sleep(600)
            
if __name__ == "__main__":
    time.sleep(240)
    main()
