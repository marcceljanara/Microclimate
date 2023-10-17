import serial
import sys
import time

time.sleep(240)
while True:
    try:
        # Inisialisasi koneksi serial dengan Arduino
        ser = serial.Serial('/dev/ttyUSB0', 9600)  # Ganti '/dev/ttyUSB0' dengan port USB Arduino Anda

        while True:
            # Baca data dari Arduino
            data = ser.readline().decode('utf-8').strip()
            
            # Tampilkan data yang dibaca
            print(data)
            time.sleep(600)

    except KeyboardInterrupt:
        # Tutup koneksi serial ketika program dihentikan dengan Ctrl+C
        ser.close()
        sys.exit(0)

    except serial.SerialException as e:
        print("tidak_terdeteksi","tidak_terdeteksi","tidak_terdeteksi")
        time.sleep(600)  # Jeda sebelum mencoba kembali
