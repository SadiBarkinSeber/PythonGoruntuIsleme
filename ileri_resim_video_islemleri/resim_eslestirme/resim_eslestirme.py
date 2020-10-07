import numpy as np
import cv2
import matplotlib.pyplot as plt
# İşlem yapacağımız için gri formata çeviririz.
resim_aranacak = cv2.imread('a20.jpg', 0)
# İşlem yapacağımız için gri formata çeviririz.
resim_buyuk = cv2.imread('a19.jpg', 0)
# orb değişkenini kullanıcaz.
orb = cv2.ORB_create()
# Anahtar notka 1 (key point) bu parametreler ile aranıcak.
an1, hedef1 = orb.detectAndCompute(resim_aranacak, None)
# Anahtar notka 2 (key point) bu parametreler ile aranıcak.
an2, hedef2 = orb.detectAndCompute(resim_buyuk, None)
# bf (brute force method) ile eşleştirici ekleriz. Çapraz sorgu açıksa
# resim yan dönmüşse bile farketmez
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# Eşleşme olduysa hedef 1 ile hedef 2 yi eşleştir.
eslesmeler = bf.match(hedef1, hedef2)
# Eğer eşleştirme bulduysa mesafe bilgilerini alırız.
eslesmeler = sorted(eslesmeler, key=lambda x: x.distance)
# Eşleşmeleri çiz. import matplotlib kütüphanesini bu fonk kullanabilmek için ekleriz.
son_resim = cv2.drawMatches(resim_aranacak, an1, resim_buyuk, an2, eslesmeler[:10], None, flags=2)
# Resmi göster.
plt.imshow(son_resim)
# Her şeyi göster.
plt.show()
