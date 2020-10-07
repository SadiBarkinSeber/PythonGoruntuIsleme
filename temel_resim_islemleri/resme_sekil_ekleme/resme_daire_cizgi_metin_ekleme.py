import cv2
import numpy as np

img = np.zeros((400, 400, 3), dtype='uint8')
# Sarı renkli bir dikörtgen çizilir.
cv2.rectangle(img, (10, 10), (390, 210), (0, 255, 251), 5)
# Kırmızı renkli bir çicgi çizilir.
cv2.line(img, (10, 10), (390, 210), (0, 0, 251), 3)
# Mor renkli bir çizgi çizilir.
cv2.line(img, (10, 230), (390, 230), (123, 45, 78), 3)
# Mavi renkli bir daire çizilir.
cv2.circle(img, (200, 350), 25, (148, 0, 4), 3)
# cv2.putText() fonksiyonu ile kalınlığını, fontunu, rengini belirlediğimiz bir yazıyı ekrana yazdırır.
cv2.putText(img, "Barkin Seber", (40, 300), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (255, 255, 255), 4, cv2.LINE_4)
# Şekillerimizi siyah bir fontun üstüne yazar ve bize gösterir.
cv2.imshow('siyah', img)
# Ekran biz kapatana kadar açık kalsın diye cv2.waitKey eklenir.
cv2.waitKey(0)
# Bir hata almamak için cv2.destroyAllWindows() fonksiyonu eklenir.
cv2.destroyAllWindows()
