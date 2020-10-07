import cv2
import numpy as np
# Fotoğrefı ekliyoruz.
img = cv2.imread('a22.jpg')
# Yüz tanımlama yapmak için eklediğimiz haarcascade_frontalface dosyasını çağırıyoruz.
yuz_casc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# İşlem yapabilmek için siyah beyaz formata çeviriyoruz.
griton = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# %10 büyütsün, 4 kere teyit etsin yüz olup olmadğını.
yuzler = yuz_casc.detectMultiScale(griton, 1.1, 4)
# For döngüsüyle yüzleri bir kare içine alırız.
# w= genişlik, h= yükseklik, x ve ye de kordinant değerleri
for (x, y, w, h) in yuzler:
    # Yeşil renkli kare içine al.
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
# Resmi göster.
cv2.imshow('yuzler', img)
# Ekran biz kapatana kadar açık kalsın diye cv2.waitKey eklenir.
cv2.waitKey(0)
# Bir hata almamak için cv2.destroyAllWindows() fonksiyonu eklenir.
cv2.destroyAllWindows()

