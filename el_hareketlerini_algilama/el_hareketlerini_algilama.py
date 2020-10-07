#Elinizi tarayan kutunun arka planında cisim olmaması
#gerekiyor(duvar gibi düz bir zemin gerekiyor) yoksa
#elinizi doğru bir biçimde algılamıyor.

import cv2
import numpy as np
import math

cap = cv2.VideoCapture(0)

while (True):

    try:  # pencerede hiçbir şey bulamazsa bir hata gelir.
        # bu nedenle bu try ekleriz.

        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        kernel = np.ones((3, 3), np.uint8)

        # bölgeyi tanımlarız
        roi = frame[100:300, 100:300]

        cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 0)
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        # HSV'de renk aralığını tanımlarız.
        lower_skin = np.array([0, 20, 70], dtype=np.uint8)
        upper_skin = np.array([20, 255, 255], dtype=np.uint8)

        mask = cv2.inRange(hsv, lower_skin, upper_skin)

        # içindeki karanlık noktaları doldurmak için
        mask = cv2.dilate(mask, kernel, iterations=4)

        # görüntüyü bulanıklaştırırız
        mask = cv2.GaussianBlur(mask, (5, 5), 100)

        # kontür bul
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # maksimum alanın konturunu bul
        cnt = max(contours, key=lambda x: cv2.contourArea(x))

        # kontur
        epsilon = 0.0005 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)

        # dışbükey gövde yaparız.
        hull = cv2.convexHull(cnt)

        # gövde alanını ve el alanını tanımlarız.
        areahull = cv2.contourArea(hull)
        areacnt = cv2.contourArea(cnt)

        # Dışbükey gövdede elle kaplanmamış alan yüzdesini buluruz
        arearatio = ((areahull - areacnt) / areacnt) * 100

        # Dışbükey gövdede elle kapsanmayan alanın yüzdesini buluruz.
        hull = cv2.convexHull(approx, returnPoints=False)
        defects = cv2.convexityDefects(approx, hull)

        l = 0

        # parmaklardan kaynaklanan kusurları bulmak için
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            start = tuple(approx[s][0])
            end = tuple(approx[e][0])
            far = tuple(approx[f][0])
            pt = (100, 180)

            # üçgenin tüm kenarlarının uzunluğunu bulun
            a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
            b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
            c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
            s = (a + b + c) / 2
            ar = math.sqrt(s * (s - a) * (s - b) * (s - c))

            # nokta ve dışbükey gövde arasındaki mesafeyi bulun
            d = (2 * ar) / a

            # kosinüs kuralını buraya uygulayın
            angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 57
            # 90 dereceden bğyük olan açıları yok sayın (bunlar genellikle gürültüden kaynaklanır)
            if angle <= 90 and d>30:
                l += 1
                cv2.circle(roi, far, 3, [255, 0, 0], -1)

            # elinizin etrafına çizgiler çizin
            cv2.line(roi, start, end, [0, 255, 0], 2)

        l += 1

        # kendi aralıklarında bulunan ilgili hareketleri yazdırır
        font = cv2.FONT_HERSHEY_SIMPLEX
        if l == 1:
            if areacnt < 2000:
                cv2.putText(frame, 'Elinizi kutuya yerlestirin', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
            else:
                if arearatio < 12:
                    cv2.putText(frame, '0', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
                elif arearatio < 17.5:
                    cv2.putText(frame, 'Bol Sans', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

                else:
                    cv2.putText(frame, '1', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

        elif l == 2:
            cv2.putText(frame, '2', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

        elif l == 3:

            if arearatio < 27:
                cv2.putText(frame, '3', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
            else:
                cv2.putText(frame, 'Tamam', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

        elif l == 4:
            cv2.putText(frame, '4', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

        elif l == 5:
            cv2.putText(frame, '5', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

        elif l == 6:
            cv2.putText(frame, 'yeniden konumlandırma', (0, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

        else:
            cv2.putText(frame, 'yeniden konumlandırma', (10, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)

        # Göster
        cv2.imshow('mask', mask)
        cv2.imshow('frame', frame)
    except:
        pass

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()