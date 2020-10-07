import cv2
import numpy as np
# Kameradan görüntüyü alsın.
kamera = cv2.VideoCapture(0)
# Haarcascade xml dosyasını çalıştırarak kamerada yüzümüzü çerçeve içine alıyoruz.
yuz_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while (1):
    # Kameradaki görüntüyü okuyarak frame oluşturdum.
    ret, frame = kamera.read()

    frame = cv2.flip(frame, 1)
    # İşlem yapabilmek için kameradaki görüntüyü gri tona çeviriyoruz
    griton = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # % 30 oranında skalasın, video görüntüsünde 3 kere yüz var mı diye teyit etsin.
    yuzler = yuz_cascade.detectMultiScale(griton, 1.3, 3)
    # Yüzü algılayıp sarı çerçeve içine alıyor
    for (x, y, w, h) in yuzler:
        # sarı renkli 3px kalınlığında bir dikdörtgen olsun.
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 3)
    # Göster.
    cv2.imshow('orjinal', frame)
    # q tuşuna basıldığında döngüyü sonlandır.
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
# Kamerayı serbest bırak.
kamera.release()
# Bütün pencereleri kapat.
cv2.destroyAllWindows()
