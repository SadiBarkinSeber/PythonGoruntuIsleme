import cv2

# Kamera bağlanır. webcam --> 0 başka bir harici webcam --> 1
kamera = cv2.VideoCapture(0)

while True:
    # Kameradan alınan verileri oku.
    ret, goruntu = kamera.read()
    # Kameradan aldığımız görüntüyü y ekseninde çevirerek bize gösterir.
    goruntu = cv2.flip(goruntu, 1)
    # Kameradan alınan görüntürü siyah beyaz formata çevirir.
    griton = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)
    # Bu görüntüleri bize gösterir.
    cv2.imshow('Goruntu', goruntu)
    cv2.imshow('Gri Ton', griton)
    # q tuşuna basarak bütün pencereleri kapat.
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
# Kameradan alınan görüntüyü bırak.
kamera.release()
# Bir hata almamak için cv2.destroyAllWindows() fonksiyonu eklenir.
cv2.destroyAllWindows()
