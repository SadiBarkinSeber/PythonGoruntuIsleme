import cv2 as cv

# Webcamden görüntüyü çekeriz.
cap = cv.VideoCapture(0)
# Görüntüyü kaydederiz. XVID formatında kaydederiz.
fourcc = cv.VideoWriter_fourcc(*'XVID')
## Kaydedilecek video dosyasının adı, uzantısı, konumu, saniyedeki
# çerçeve sayısı ve çözünürlüğü
out = cv.VideoWriter('output.avi', fourcc, 25.0, (640, 480))

while (cap.isOpened()):
    # Videodan görüntü oku ve geri döndür.
    ret, frame = cap.read()
    if ret == True:
        # 1 => yatay döndürme
        frame = cv.flip(frame, 1, dst=None)
        out.write(frame)
        cv.imshow('frame', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# İşin bittikten sonra her şeyi serbest bırak.
kamera.release()
kayit.release()
cv2.destroyAllWindows()
