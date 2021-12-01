import cv2

img = cv2.imread("A.png")
print(img.shape)
print(img.size)

for row in img:
   for pixel in row:
       pixel[0] = 255 - pixel[0]                     # blue
       pixel[1] = 255 - pixel[1]                     # green
       pixel[2] = 255 - pixel[2]                     # red

cv2.imshow("Image", img)
cv2.waitKey(0)
