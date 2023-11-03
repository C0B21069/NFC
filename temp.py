import time
import requests
import busio
import board

import adafruit_amg88xx

while True:
    url = "https://maker.ifttt.com/trigger/temp/with/key/cNIQxlL1O5HfyMf7-WUVdh"
    i2c = busio.I2C(board.SCL, board.SDA)
    sensor = adafruit_amg88xx.AMG88XX(i2c, addr=0x68)
    time.sleep(0.2)
    temp = [sum(temps) for temps in sensor.pixels]
    total_temp = sum(temp)//64
    payload = {"value1":str(total_temp),"value2":str("nothing"),"value3":str("nothing")}
    response = requests.post(url,data=payload)
    print(total_temp)
    time.sleep(10)



