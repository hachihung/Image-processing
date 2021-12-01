import cv2
from colour import Color

img = cv2.imread("A.png")
print(img.shape)
print(img.size)

for row in img:
    for element in row:
        print(element[0] // 255, end="")
    print()
