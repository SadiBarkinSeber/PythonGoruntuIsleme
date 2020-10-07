# İlk olarak bir resim çekiyor o resimde takip etmesini istediğiniz
# şeyi mause ile seçip enter tuşuna basıyorsunuz ardından seçtiğiniz
# şeyi takip ediyor
import cv2
tracker = cv2.TrackerMOSSE_create()

cap = cv2.VideoCapture(0)
success, frame = cap.read()
bbox = cv2.selectROI("Tracking", frame, False)
tracker.init(frame, bbox)

# Takip edilen şekli kutucuk şeklinde gösteriyoruz
def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 255), 3, 3)
    cv2.putText(img, "Takip Ediliyor", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)


5

while True:

    timer = cv2.getTickCount()
    success, img = cap.read()
    success, bbox = tracker.update(img)

    if success:
        drawBox(img, bbox)
        # Eğer seçilen şekli kaybolduysa EDuruma kayip yazıyor.
    else:
        cv2.putText(img, "Kayip", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    # Ekrandan takip edilmesi  Fps göstergesi ve durum göstergesini ekliyoruz
    cv2.rectangle(img, (15, 15), (200, 90), (255, 0, 255), 2)
    cv2.putText(img, "Fps:", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2);
    cv2.putText(img, "Durum:", (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2);

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
    # Farklı FPS değerlerine farklı renkler atıyoruz.
    if fps > 60:
        myColor = (20, 230, 20)
    elif fps > 20:
        myColor = (230, 20, 20)
    else:
        myColor = (20, 20, 230)
    cv2.putText(img, str(int(fps)), (75, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, myColor, 2);

    cv2.imshow("Takip", img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
