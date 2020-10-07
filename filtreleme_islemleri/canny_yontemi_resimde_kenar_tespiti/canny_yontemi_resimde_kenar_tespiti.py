import cv2
import numpy as np
from matplotlib import pyplot as plt
# 0 ile gri tona çeviriyoruz.
resim = cv2.imread("a2.jpg", 0)
# Eşik değerlerini belirleyerek kenar tespitini sağlıyoruz.
kenarlar = cv2.Canny(resim, 800, 200)
# Orjinal resmi gri tonda göstersin.
plt.subplot(121), plt.imshow(resim, cmap='gray')
plt.title('orjinal'), plt.xticks([]), plt.yticks([])
# Kenarları göster.
plt.subplot(122), plt.imshow(kenarlar, cmap='gray')
plt.title('kenarlar'), plt.xticks([]), plt.yticks([])
# Göster.
plt.show()
