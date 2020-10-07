import cv2
# Webcamden görüntüyü çekeriz.
kamera = cv2.VideoCapture(0)
# Görüntünün boyutunu ayarlarız.
kamera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    # Videodan alınan verileri oku.
    ret, goruntu = kamera.read()
    # Yekseninde görüntüyü ters çeviririz.
    goruntu = cv2.flip(goruntu, 1)
    # Videodan alınan görüntürü siyah beyaz formata çevirir.
    griton = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)
    # Bu görüntüleri bize gösterir.
    cv2.imshow('Goruntu', goruntu)
    cv2.imshow('Gri ton', griton)
    # q tuşuna basarak bütün pencereleri kapat.
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
# Videodan alınan görüntüyü bırak.
kamera.release()
# Bir hata almamak için cv2.destroyAllWindows() fonksiyonu eklenir.
cv2.destroyAllWindows()
