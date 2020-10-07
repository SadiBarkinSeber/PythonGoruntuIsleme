import cv2

# Yüz tespiti için xml dosyası yükleriz.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface.xml')
# Göz tespiti için xml dosyası yükleriz.
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
# Görüntüyü kameradan alırız.
cap = cv2.VideoCapture(0)
# Kamerada bir süreç kaydettiği için While döngüsü kurarız.
while True:
    # ret ve frame adlı iki değişken ekleriz.
    ret, frame = cap.read()
    # Kamera da görüntü ters düşeceğinden x eksenine
    # göre tersini alarak düzgün bir görüntü sağlarız.
    frame = cv2.flip(frame, 1)
    ret = cv2.flip(ret, 1)
    # İ şlem yapabilmek için grey formatına çeviririz.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # % 30 oranında skalasın, video görüntüsünde 3 kere yüz var diye teyit etsin.
    faces = face_cascade.detectMultiScale(gray, 1.3, 3)
    # Yüzleri kare içerisinde gösterelim.
    for (x, y, w, h) in faces:
        # sarı renkli 2px kalınlığında bir dikdörtgen olsun.
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # Gri tonda işlem yaptığımız için belirlediğimiz yüzü dörtgen şeklinde aırız.
        roi_gray = gray[y:y + h, x:x + w]
        # Renkliye çeviririz.
        roi_renkli = frame[y:y + h, x:x + w]
        # Gri tonda gözleri aratırız.
        eye = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eye:
            # Yeşil renkli 2px kalınlığında bir dikdörtgen olsun.
            cv2.rectangle(roi_renkli, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    # Göster.
    cv2.imshow('goruntu', frame)
    # q tuşuna basıldığında döngüyü sonlandır.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Kamerayı serbest bırak.
cap.release()
# Bütün pencereleri kapat.
cv2.destroyAllWindows()
