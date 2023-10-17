import sht85
import time

mps = 1  # accepted intervals 0.5, 1, 2, 4, 10 seconds
rep = 'HIGH'  # Repeatability: HIGH, MEDIUM, LOW

# print ('serial number = ', sht85.sn())
#time.sleep(0.5e-3)

try:
    sht85.periodic(mps, rep)
    time.sleep(240)
except OSError as e:
    pass

while True:
    try:
        t, rh = sht85.read_data()
        dp = sht85.dew_point(t, rh)
        print(t, rh)
    except OSError:
        print("tidak_terdeteksi","tidak_terdeteksi")
    
    time.sleep(600)

sht85.stop()
