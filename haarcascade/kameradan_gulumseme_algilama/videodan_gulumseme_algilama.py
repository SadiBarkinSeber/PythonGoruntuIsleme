import cv2
# Kameradan görüntüyü alsın.
vid = cv2.VideoCapture(0)
# Haarcascade xml dosyalarını çalıştıyoruz.
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier("smile.xml")

while 1:
    # Kameradaki görüntüyü okuyarak frame oluşturdum.
    ret, frame = vid.read()
    # İşlem yapabilmek için kameradaki görüntüyü gri tona çeviriyoruz
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # % 20 oranında skalasın, video görüntüsünde 8 kere yüz var diye teyit etsin.
    faces = face_cascade.detectMultiScale(gray, 1.2, 8)

    for (x, y, w, h) in faces:

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        roi_gray = gray[x:x + w, y:y + h]
        roi_img = frame[x:x + w, y:y + h]
        # % 90 oranında skalasın, video görüntüsünde 9 kere gulumseme var mı diye teyit etsin.
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.9, 9)
        for (ex, ey, ew, eh) in smiles:
            # yeşil renkli 2px kalınlığında bir dikdörtgen olsun.
            cv2.rectangle(roi_img, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('videos', frame)
    # q tuşuna basıldığında döngüyü sonlandır.
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()