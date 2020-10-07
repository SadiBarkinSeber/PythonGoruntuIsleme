import cv2
# Kullanacağımız videoyu çalışmamıza dahil edelim.
vid = cv2.VideoCapture('b5.mp4')
# Kullanacağımız cascade dosyalarını çalışmamıza dahil edelim.
car_cascade = cv2.CascadeClassifier('cars.xml')

while True:
    # Her kareyi tek tek okuyalım.
    ret, frame = vid.read()
    frame = cv2.resize(frame, (640, 480))
    # Haar-like özellikleri kolay algılayabilmek için her bir kareyi boz(gri) tonlara çevirelim.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 4)
    # "cars" değişkeninde tuttuğumuz koordinatları kullanarak arabaları dikdörtgen içerisine alalım.
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
    # İşlediğimiz kareleri görelim.
    cv2.imshow('image', frame)
    # Programı kapatacak kodu yazalım.
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
