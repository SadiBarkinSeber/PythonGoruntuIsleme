import cv2

cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('face.xml')
# Her bir kişiye bir sayı veriyoruz ve o sayıyla kaydediyoruz.
i = 0
# input komutu kullanıcıya veri sorup onu string olarak kaydeden bir komut.
kisi_id = input('ID numarası giriniz')
# Kameradan görüntü alacağımız için while döngüsü kuruyoruz.
while True:
    _, img = cam.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Yüz bulması için skalama --> 1.2, fotoğrafı en az 5 kere tarasın, minimum sice 100x100 olsun.
    faces = detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100),
                                      flags=cv2.CASCADE_SCALE_IMAGE)
    # Yüz tespiti için her bir fotoğrafı kaydet.
    for (x, y, w, h) in faces:
        i = i + 1
        # Gri tonda aldığımız resmin sadece yüz kısımlarını kaydet.
        cv2.imwrite("yuz_verileri/face-" + kisi_id + '.' + str(i) + ".jpg", gray[y:y + h, x:x + w])
        # Bir dikdörtgen içine alsın yüzü
        cv2.rectangle(img, (x, y), (x + w, y + h), (225, 0, 0), 2)
        cv2.imshow('resim', img[y:y + h, x:x + w])
        cv2.waitKey(100)
    # i > 20 ise (20 tane resim )
    if i > 20:
        cam.release()
        cv2.destroyAllWindows()
        break
cv2.destroyAllWindows()
