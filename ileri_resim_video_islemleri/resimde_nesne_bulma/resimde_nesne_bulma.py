import cv2
import numpy as np
# Ana resmi çağırdık.
img_rgb = cv2.imread('a11.jpg')
# Gri formata çevirdik.
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# Ana resmin içinde arayacağımız resmi ekleriz. Gri formda alırız.
nesne = cv2.imread('a12.jpg', 0)
# 3. ve 4. parametreleri alırız.
w, h = nesne.shape[::-1]
# Verdiğimiz iki resmi eşleştirmeye çalış.
res = cv2.matchTemplate(img_gray, nesne, cv2.TM_CCOEFF_NORMED)
# %80 doğruluk payı ile bulmaya çalış.
threshold = 0.8
# %80 den fazla olan kısımları loc'ta tut.
loc = np.where(res > threshold)

for n in zip(*loc[::-1]):
    # Çizeceğimiz dörtgenin kalınlığını, rengini
    cv2.rectangle(img_rgb, n, (n[0] + w, n[1] + h), (0, 255, 255), 2)
# Resmi göster.
cv2.imshow('bulunan nesneler', img_rgb)
# Ekran biz kapatana kadar açık kalsın diye cv2.waitKey eklenir.
cv2.waitKey(0)
# Bir hata almamak için cv2.destroyAllWindows() fonksiyonu eklenir.
cv2.destroyAllWindows()
