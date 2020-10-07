import cv2
import numpy as np

kamera = cv2.VideoCapture("b1.mp4")

while (1):
    ret, frame = kamera.read()
    # Hsv ye çeviriyoruz. COLOR_BGR2HSV ile filtreliyoruz.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    dusuk_mavi = np.array([30, 40, 30])
    ust_mavi = np.array([140, 255, 255])

    mask = cv2.inRange(hsv, dusuk_mavi, ust_mavi)
    son_resim = cv2.bitwise_and(frame, frame, mask=mask)
    # Ortalama 15 pixel de bir bulanıklaştırmasını sağlar.
    kernel = np.ones((15, 15), np.float32) / 225
    # Filte oluşturuyoruz.
    smoothed = cv2.filter2D(frame, -1, kernel)
    # blurlama fonksiyonu.
    blur = cv2.GaussianBlur(son_resim, (15, 15), 0)
    # blurlama fonksiyonu.
    median = cv2.medianBlur(son_resim, 15)
    # blurlama fonksiyonu.
    bileteral = cv2.bilateralFilter(son_resim, 15, 75, 75)
    # Ekranda göster.
    cv2.imshow('orjinal', frame)
    cv2.imshow('son_resim', son_resim)
    cv2.imshow('bileteral', smoothed)
    # q tuşuna basınca bütü pencereleri kapat.
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
# Videodan alınan görüntüyü bırak.
kamera.release()
# Bir hata almamak için cv2.destroyAllWindows() fonksiyonu eklenir.
cv2.destroyAllWindows()
