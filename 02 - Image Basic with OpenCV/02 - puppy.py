import cv2
import numpy as np

img = cv2.imread(r'C:\Users\Data\computer vision\00-puppy.jpg')

while True:
    cv2.imshow('puppys', img)
    if cv2.waitKey(20) & 0xff == 27:
        break

cv2.destroyAllWindows()
