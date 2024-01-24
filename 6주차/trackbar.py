import numpy as np
import cv2

def onChange(value):
    global image, title1

    add_value = value - int(image[0][0])
    print("추가 화소값:", add_value)
    image = image + add_value       
    cv2.imshow(title, image)

image = np.zeros((300, 500), np.uint8)


title = 'Trackbaar Event'
cv2.imshow(title, image)

cv2.createTrackbar('Brightness', title, image[0][0], 255, onChange)
cv2.waitKey(0)
cv2.destroyAllWindows()
