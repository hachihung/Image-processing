# create a bitmap image with Python

import cv2
import numpy as np

# image height 300, width 400
img = np.zeros((300, 400, 3), np.uint8)  # unsigned integer 8 bit (0-255)

print(img)

for row in img:
   for pixel in row:
       pixel[0] = 32                   # blue
       pixel[1] = 32                   # green
       pixel[2] = 32                   # red

cv2.imshow("Image", img)
cv2.waitKey(0)
