import cv2
import numpy as np

img = cv2.imread('sayfa.jpg')
ret, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

griton = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresholdgri = cv2.threshold(griton, 12, 255, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(griton, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

ret, otsu = cv2.threshold(griton, 200, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('orjinal', img)
cv2.imshow('threshold', threshold)
cv2.imshow('thresholdgri', thresholdgri)
cv2.imshow('gaus', gaus)

cv2.waitKey(0)
cv2.destroyAllWindows()
