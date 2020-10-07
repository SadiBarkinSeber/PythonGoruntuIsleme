import cv2
import numpy as np

img = cv2.imread('stormtrooper.jpg')

print(img[:, :, 1])
alanmavi = img[:, :, 0]
img[:, :, 1] = 0
img[:, :, 2] = 0

cv2.imshow('mavi', alanmavi)
cv2.imshow('img', img)
# Ekran biz kapatana kadar açık kalsın diye cv2.waitKey eklenir.
cv2.waitKey(0)
# Bir hata almamak için cv2.destroyAllWindows() fonksiyonu eklenir.
cv2.destroyAllWindows()

