import cv2
import numpy as np

cap = cv2.VideoCapture('b5.mp4')
human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

while True:
    _, frame = cap.read()
    # İşlem yapabilmek için kameradaki görüntüyü gri tona çeviriyoruz
    griton = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # % 30 oranında skalasın, video görüntüsünde 3 kere vucut var diye teyit etsin.
    insan = human_cascade.detectMultiScale(griton, 1.1, 3)

    for (x, y, w, h) in insan:
        # sarı renkli 2px kalınlığında bir dikdörtgen olsun.
        cv2.rectangle(frame, (x, y), (x + h, y + w), (0, 255, 255), 2)
    cv2.imshow('insanlar', frame)
    # q tuşuna basıldığında döngüyü sonlandır.
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
# Kamerayı serbest bırak.
kamera.release()
# Bütün pencereleri kapat.
cv2.destroyAllWindows()
