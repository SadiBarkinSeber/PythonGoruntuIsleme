import cv2
import numpy as np
# Resmi ekleriz.
img = cv2.imread("a2.jpg")
# Up fonksiyonu ile resmin boyutunu büyütürüz.
up = cv2.pyrUp(img)
# Down fonksiyonu ile resmin boyutunu küçültürüz.
down = cv2.pyrDown(img)
# Orjinal resmi göster.
while True:
    # Orjinal resmi göster.
    cv2.imshow('orjinal', img)
    # Büyütülmüş resmi göster.
    cv2.imshow('up', up)
    # Küçültülmüş resmi göster.
    cv2.imshow('down', down)
    # q harfine basarak bütün döngüyü kırar ve gösterilenleri kapatırız.
    if cv2.waitKey(1) & 0xFF == ord("q"):
         break
# Ekran biz kapatana kadar açık kalsın diye cv2.waitKey eklenir
cv2.waitKey(0)
# Bir hata almamak için cv2.destroyAllWindows() fonksiyonu eklenir.
cv2.destroyAllWindows()
