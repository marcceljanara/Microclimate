# Microclimate

- Rasberry Pi
1. Rain Gauge : SDA SCL (I2C)
2. MICS-4514 : SDA SCL (I2C)
3. DS18B20 (stasiun 1) : GPIO 26
4. ens160 (tidak terpakai)
5. ds18b20 (nodered)

- ESP32
1. Pyranometer : DIR 14 (Join RE & DE), RO 25, DI 26 --> Module Max485
2. Anemometer : RX2(16) dan TX2(17) --> Module XY485
3. Wind Direction : RX 18 dan TX 19 --> Module XY485
4. SHT85 : SDA SCL (I2C)
