import time
from w1thermsensor import W1ThermSensor

time.sleep(240)
while True:
    try:
        sensor = W1ThermSensor()
        temperature = sensor.get_temperature()
        print(temperature)
    except Exception as e:
        print(0)
    time.sleep(600)
