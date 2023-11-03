import cv2 as cv
import numpy as np

import time
import busio
import board

import adafruit_amg88xx
import colorsys

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_amg88xx.AMG88XX(i2c, addr=0x68)

time.sleep(0.2)

img = np.full((320, 320, 3), 128, dtype=np.uint8)

cellsize = 40

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

def mapVal(val, inMin, inMax, outMin, outMax):
    return (val - inMin) * (outMax - outMin) / (inMax - inMin) + outMin

pixels = sensor.pixels
for x in range(len(pixels)):
    for y in range(len(pixels[0])):
        val = mapVal(pixels[x][y], 15, 28, 270, 0)
        val = min(max(0, val), 270)
        color = tuple(reversed(hsv2rgb(val/360, 1.0, 0.5)))
        cv.rectangle(img, (x*cellsize, y*cellsize), (x*cellsize+cellsize, y*cellsize+cellsize), color, thickness=-1)

cv.imshow('image', img);
cv.waitKey()

cv.destroyAllWindows()
