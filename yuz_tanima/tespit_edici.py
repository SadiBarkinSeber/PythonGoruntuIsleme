import cv2

recognizer = cv2.face.LBPHFaceRecognizer_create()
# training içinden trainer.ymldosyasını oku
recognizer.read('training/trainer.yml')
cascadePath = "face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
path = 'yuzverileri'
# Webcamden canlı tarat.
cam = cv2.VideoCapture(0)
while True:
    ret, im = cam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # Yüz bulması için skalama --> 1.2, fotoğrafı en az 5 kere tarasın, minimum sice 100x100 olsun.
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=8, minSize=(100, 100),
                                         flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        tahminEdilenKisi, conf = recognizer.predict(gray[y:y + h, x:x + w])
        cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
        if (tahminEdilenKisi == 1):
            tahminEdilenKisi = 'Barkin Seber'
        elif (tahminEdilenKisi == 2):
            tahminEdilenKisi = 'Edison'
        else:
            tahminEdilenKisi = "Bilinmeyen kişi"
        fontFace = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        fontColor = (255, 255, 255)
        cv2.putText(im, str(tahminEdilenKisi), (x, y + h), fontFace, fontScale, fontColor)
        cv2.imshow('im', im)
        cv2.waitKey(10)
