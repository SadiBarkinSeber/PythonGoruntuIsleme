import cv2
import numpy as np
from matplotlib import pyplot as plt
# Resmi gri formda ekleriz.
img = cv2.imread('gurultuluresim.JPG', 0)
# THRESH_BINARY' e göre, 127' ye göre thresholding yaparız.
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# Artık 127 vermiyoruz o kendi algotitmaları ile otomatik hesaplıyor o yüzden 0 verdik.
_, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# 3. resmi ilk olarak blurlarız.
blur = cv2.GaussianBlur(img, (5, 5), 0)
# Blurladığımız resmi threshold yaparız.
_, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# Resimleri tanıttık.
resimler = [img, 0, th1,
            img, 0, th2,
            blur, 0, th3]
# Resimlerin başlıklarını ekledik.
basliklar = ['orjinal resim', 'Histogram', 'Basit Thresholding(v=127)',
             'orjinal resim', 'Histogram', 'Otsu Thresholding',
             'Gaussian Blur', 'Histogram', 'Otsu Thresholding']
# 3 resim için for döngüsü kurduk.
for i in range(3):
    # 3 e 3 bir gösterim yaptık. İlk olarak orjinal remi gri formatta gösterdik.
    plt.subplot(3, 3, i * 3 + 1), plt.imshow(resimler[i * 3], 'gray')
    plt.title(basliklar[i * 3]), plt.xticks([]), plt.yticks([])
    # 3 e 3 bir gösterim yaptık. Histogramları gösterdik.
    plt.subplot(3, 3, i * 3 + 2), plt.hist(resimler[i * 3].ravel(), 200)
    plt.title(basliklar[i * 3 + 1]), plt.xticks([]), plt.yticks([])
    # 3 e 3 bir gösterim yaptık. İlk olarak sadece 127' ye göre thresholding yaptığımızı gösterdik
    # İkinci olarak otomatik otsu yöntemi ile threshold yaptığı resmi gösterdik.
    # Son olarakta blurlama yaptıktan sonra otsu yöntemi ile thresholding yaptığımız resimleri gösterdik
    plt.subplot(3, 3, i * 3 + 3), plt.imshow(resimler[i * 3 + 2], 'gray')
    plt.title(basliklar[i * 3 + 2]), plt.xticks([]), plt.yticks([])
# Her şeyi göster.
plt.show()
