import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('a10.jpg')
# Resme maske tanıttık.
mask = np.zeros(img.shape[:2], np.uint8)
# Arka kısma bir backgraund belirledik.
bgdMmodel = np.zeros((1, 65), np.float64)
# Ön ksıma bir ön plan beirledik.
fgdMmodel = np.zeros((1, 65), np.float64)
# On plana çıkarılcak şeklin büyüklüğünü belirleriz.
diktortgen = (150, 250, 400, 500)
# Ön plana çıkardığımız komut.
cv2.grabCut(img, mask, diktortgen, bgdMmodel, fgdMmodel, 5, cv2.GC_INIT_WITH_RECT)
# Bir maske daha ekliyoruz.
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
# Resimle maskeyi bir araya getiriyoruz.
img = img * mask2[:, :, np.newaxis]
# Resmi göster.
plt.imshow(img)
plt.colorbar()
# Göster.
plt.show()
