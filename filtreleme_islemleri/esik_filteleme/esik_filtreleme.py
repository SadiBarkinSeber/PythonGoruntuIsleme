import cv2
import numpy as np
from matplotlib import pyplot as plt

# Resmi ekliyoruz.
resim = cv2.imread('a2.JPG')
# Resmi THRESH_BINARY formatında filtrelenmiş şekilde göster.
ret, thresh1 = cv2.threshold(resim, 127, 255, cv2.THRESH_BINARY)
# Resmi THRESH_BINARY_INV formatında filtrelenmiş şekilde göster.
ret, thresh2 = cv2.threshold(resim, 127, 255, cv2.THRESH_BINARY_INV)
# Resmi THRESH_TRUNC formatında filtrelenmiş şekilde göster.
ret, thresh3 = cv2.threshold(resim, 127, 255, cv2.THRESH_TRUNC)
# Resmi THRESH_TOZERO formatında filtrelenmiş şekilde göster.
ret, thresh4 = cv2.threshold(resim, 127, 255, cv2.THRESH_TOZERO)
# Resmi THRESH_TOZERO_INV formatında filtrelenmiş şekilde göster.
ret, thresh5 = cv2.threshold(resim, 127, 255, cv2.THRESH_TOZERO_INV)
# Başlıkları ekledik.
basliklar = ['orjinal resim', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
# Resimleri tanımladık.
resimler = [resim, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    # 2 satır 3 sütun olucak şekilde göster.
    # i . elemandan başlayarak göster.
    plt.subplot(2, 3, i + 1), plt.imshow(resimler[i], 'gray')
    plt.title(basliklar[i])
    # Değerleri girebilmek için boş değer koyduk.
    plt.xticks([]), plt.yticks([])
# Her şeyi göster
plt.show()
