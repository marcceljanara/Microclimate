import RPi.GPIO as GPIO
import time

bucketPin = 16  # Pin yang terhubung ke sensor ember
rainCount = 0
totalRainComulative = 0  # Jumlah hujan dalam interval 1 menit
interval = 600 # Interval pengukuran dalam detik
#daysInterval = 86400  # Interval 1 menit dalam detik

GPIO.setmode(GPIO.BCM)
GPIO.setup(bucketPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def bucket_tipped(channel):
    global rainCount
    rainCount += 1

def main():
    global rainCount, totalRainComulative

    GPIO.add_event_detect(bucketPin, GPIO.FALLING, callback=bucket_tipped, bouncetime=100)

    try:
        while True:
            time.sleep(interval)
            
            mm = 0.3 * rainCount  # Menghitung volume hujan dalam mm
            totalRainComulative += mm
            rainCount = 0  # Reset hitungan setelah mengukur
            print(round(mm,3))
            

    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    time.sleep(240)
    print(0)
    main()
