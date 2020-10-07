import cv2
import numpy as np

kamera = cv2.VideoCapture("b1.mp4")

while (1):
    ret, frame = kamera.read()
    # Hsv ye çeviriyoruz. COLOR_BGR2HSV ile filtreliyoruz.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Alt tonu belirleriz.
    dusuk_mavi = np.array([30, 40, 30])
    # Üst tonu belirleriz.
    ust_mavi = np.array([140, 255, 255])

    mask = cv2.inRange(hsv, dusuk_mavi, ust_mavi)
    son_resim = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('orjinal', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('son_resim', son_resim)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
# Videodan alınan görüntüyü bırak.
kamera.release()
# Bir hata almamak için cv2.destroyAllWindows() fonksiyonu eklenir.
cv2.destroyAllWindows()
