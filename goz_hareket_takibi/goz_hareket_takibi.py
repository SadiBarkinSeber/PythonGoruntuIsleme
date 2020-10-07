

import cv2
import numpy as np

cap = cv2.VideoCapture("b21.flv")

while True:
    ret, frame = cap.read()
    if ret is False:
        break
    # Bu şekil de saptamayı sadece gözbebeği, iris ve sklera ile sınırlıyor ve kirpik,
    # göz çevresi gibi tüm gereksiz şeyleri kesiyoruz.
    roi = frame[50: 300, 200: 500]
    rows, cols, _ = roi.shape
    # Önce gri tonlamaya dönüştürme ve ardından sadece gözbebeğini çıkarmak
    # için eşiği buluyoruz.
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gray_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0)
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gray_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0)
    #Eşikten konturları buluyoruz. Ve en büyük alana sahip öğeyi seçerek
    # (gözbebeği olması gereken) tüm gürültüyü kaldırır ve geri kalanını atlarız.
    _, threshold = cv2.threshold(gray_roi, 3, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)

        # Ekranda her şeyi gösteriyoruz.
        cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.line(roi, (x + int(w / 2), 0), (x + int(w / 2), rows), (0, 255, 0), 2)
        cv2.line(roi, (0, y + int(h / 2)), (cols, y + int(h / 2)), (0, 255, 0), 2)
        break
    cv2.imshow("Threshold", threshold)
    cv2.imshow("gray roi", gray_roi)
    cv2.imshow("Roi", roi)
    key = cv2.waitKey(30)
    if key == 27:
        break

cv2.destroyAllWindows()