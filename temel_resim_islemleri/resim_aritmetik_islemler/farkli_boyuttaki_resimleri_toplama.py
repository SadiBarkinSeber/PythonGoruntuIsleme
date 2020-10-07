import cv2
import numpy as np

# Resimleri ekledik.
img1 = cv2.imread('a1.jpg')
img2 = cv2.imread('a5.jpg')
# 1. resmimizde 2. resmimizin sol üst köşesindeki alanını belirliyoruz.
satir, sutun, kanal = img2.shape
roi = img1[0:satir, 0:sutun]
# Griye çevirdik.
im2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cv2.imshow('im2gray', im2gray)
# siyah dışındaki her yeri beyaz ile maskeleyerek 2 renk elde ettik.
# siyah ve beyaz böylece ayırmak daha kolay olucak
ret, mask = cv2.threshold(im2gray, 10, 255, cv2.THRESH_BINARY)
# Mask'ın tam tersini aldı siyahlar beyaz, beyazlar siyah oldu.
mask_inv = cv2.bitwise_not(mask)
# Üstte yaptığımız işlemleri gösterdik.
cv2.imshow('mask', mask)
cv2.imshow('mask_inv', mask_inv)
# Belirlediğimiz bölgeyi sabit tutarak arka planını aldı.
im1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
cv2.imshow('im1_bg', im1_bg)
# Arka planı siyahlatıp renklerini korudu.
im2_fg = cv2.bitwise_and(img2, img2, mask=mask)
cv2.imshow('im2_fg', im2_fg)
# 1. resmimizin background'u ile 2. resmin foreground'unu topladık.
son_resim = cv2.add(im1_bg, im2_fg)
img1[0:satir, 0:sutun] = son_resim
# Resmi gösterdik.
cv2.imshow('son resim', img1)
# Ekran biz kapatana kadar açık kalsın diye cv2.waitKey eklenir.
cv2.waitKey(0)
# Bir hata almamak için cv2.destroyAllWindows() fonksiyonu eklenir.
cv2.destroyAllWindows()
