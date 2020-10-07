import cv2
import numpy as np
# Fotoğrefı ekliyoruz.
img = cv2.imread('a21.jpg')
# Vücut tanımlama yapmak için eklediğimiz haarcascade_frontalface dosyasını çağırıyoruz.
body_cascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")
# İşlem yapabilmek için siyah beyaz formata çeviriyoruz.
griton = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# %10 büyütsün, 1 kere teyit etsin vücut olup olmadğını.
bodies = body_cascade.detectMultiScale(griton, 1.1, 1)
# w= genişlik, h= yükseklik, x ve ye de kordinant değerleri
for (x, y, w, h) in bodies:
    # Sarı renkli kare içine al.
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
# Resmi göster.
cv2.imshow('body', img)
# Ekran biz kapatana kadar açık kalsın diye cv2.waitKey eklenir.
cv2.waitKey(0)
# Bir hata almamak için cv2.destroyAllWindows() fonksiyonu eklenir.
cv2.destroyAllWindows()

