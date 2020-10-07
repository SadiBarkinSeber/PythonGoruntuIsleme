import cv2
import numpy as np
# Resimleri çoklu göstermek için bu kütüphaneyi ekleriz.
from matplotlib import pyplot as plt
# Resmi çağırırız. Gri tonda çağırırız.
img = cv2.imread('sudoku.JPG', 0)
# Resmi blurlarız.
img = cv2.medianBlur(img, 5)
# Klasik threshold yaparak resmi netleştirebilicez mi bakarız.
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# adaptiveThreshold yaparak ve THRESH_MEAN kullanarak gölgelemelerin
# ortalamasını alarak tresh işlemi uygular.
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
# adaptiveThreshol yaparak ve THRESH_GAUSSIAN kullanarak gölgelemelerin ağırlıklı
# ortalamasını alarak tresh işlemi uygular.
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 2)
# Başlıkları ekledik.
basliklar = ['Orjinal Resim', 'Basit Thresholding(127)', 'MEAN_C', 'GAUSSIAN_C']
# Resimleri tanımladık.
resimler = [img, th1, th2, th3]
for i in range(4):
    # 2 satır 2 sütun olucak şekilde göster.
    # i . elemandan başlayarak göster.
    plt.subplot(2, 2, i + 1), plt.imshow(resimler[i], 'gray')
    plt.title(basliklar[i])
    # Değerleri girebilmek için boş değer koyduk.
    plt.xticks([]), plt.yticks([])
# Her şeyi göster
plt.show()
