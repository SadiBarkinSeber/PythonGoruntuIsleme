import cv2

# "" işaretleri içinde göstermesini istediğimiz videoyu yazarız.
kamera = cv2.VideoCapture("b1.mp4")

while True:
    # Videodan alınan verileri oku.
    ret, goruntu = kamera.read()
    # Videodan alınan görüntürü siyah beyaz formata çevirir.
    griton = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)
    # Bu görüntüleri bize gösterir.
    cv2.imshow('Goruntu', goruntu)
    cv2.imshow('Gri Ton', griton)
    # q tuşuna basarak bütün pencereleri kapat.
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
# Videodan alınan görüntüyü bırak.
kamera.release()
# Bir hata almamak için cv2.destroyAllWindows() fonksiyonu eklenir.
cv2.destroyAllWindows()
