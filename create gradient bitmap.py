import cv2
import numpy as np

# image height 300, width 400
img = np.zeros((512, 512, 3), np.uint8)  # unsigned integer 8 bit (0-255)

print(img)

count = 0
for row in img:
    count += 0.5
    for pixel in row:
       pixel[0] = 0                  # blue
       pixel[1] = count                  # green
       pixel[2] = 0               # red

cv2.imshow("Image", img)
cv2.waitKey(0)
