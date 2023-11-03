import time
import busio
import board

import adafruit_amg88xx

i2c = busio.I2C(board.SCL, board.SDA)

sensor = adafruit_amg88xx.AMG88XX(i2c, addr=0x68)

time.sleep(0.2)

print(sensor.pixels)


