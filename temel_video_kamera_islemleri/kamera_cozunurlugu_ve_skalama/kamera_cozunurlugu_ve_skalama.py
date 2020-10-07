import cv2

# Webcamden görüntüyü çekeriz.
kamera = cv2.VideoCapture(0)


# Çözünürlük parametresi gireriz.
def cozun_1080p():
    # (3)--> genişlik (4)--> yükseklik
    kamera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)


# Çözünürlük parametresi gireriz.
def cozun_720p():
    # (3)--> genişlik (4)--> yükseklik
    kamera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


# Çözünürlük parametresi gireriz.
def cozun_480p():
    # (3)--> genişlik (4)--> yükseklik
    kamera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


# Çözünürlük parametresi kendimiz oluştururuz.
def coz_belirle(width, height):
    # (3)--> genişlik (4)--> yükseklik
    kamera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

cozun_1080p()

# Alınan görüntünün % 75'i gösteririz.
def scalalama(frame, percent=75):
    # Tam sayıya çeviririz.
    width = int(frame.shape[1] * percent / 100)
    height = int(frame.shape[0] * percent / 100)
    boyut = (width, height)
    # Yeniden boyutlandırılır.
    return cv2.resize(frame, boyut, interpolation=cv2.INTER_AREA)


# Kamerayı çalıştırmak için while döngüsü kullanırız.
while True:
    ret, frame = kamera.read()
    # Yekseninde görüntüyü ters çeviririz.
    frame = cv2.flip(frame, 1)
    frame150 = scalalama(frame, 75)
    cv2.imshow('goruntu1', frame)
    cv2.imshow('goruntu2', frame150)
    # q tuşuna basınca pencereleri kapat.
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
# Videodan alınan görüntüyü bırak.
kamera.release()
# Bir hata almamak için cv2.destroyAllWindows() fonksiyonu eklenir.
cv2.destroyAllWindows()
