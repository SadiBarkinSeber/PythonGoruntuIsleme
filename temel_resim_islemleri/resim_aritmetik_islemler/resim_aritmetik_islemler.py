import cv2

img = cv2.imread('a3.jpg')
# 80X80 pixelinin değerini gösterir.
print(img[80, 80])
# 80x80 pixelinin değerini değiştirdik.
img[80, 80] = [255, 255, 255]
# Belirli bir alanı seçip ismine bölge dedik.
bolge = img[80:330, 90:335]
# 90:340,350:595 kordinatındaki bölgeye, bölge ismini verdiğimiz değerleri atadık.
img[90:340, 350:595] = bolge
# Belirlenmiş alanın içini mor kapladık
# img[90:320, 90:335] = [90,0,90]
# Sarı renkli kalınlığı 2 olan bir dikdörtgen ile belirledik.
cv2.rectangle(img, (90, 320), (335, 90), (0, 255, 225), 2)
# cv2.imshow() fonksiyonu ile resimleri gösterdik.
cv2.imshow('saat', img)
cv2.imshow('saat2', bolge)
# Ekran biz kapatana kadar açık kalsın diye cv2.waitKey eklenir.
cv2.waitKey(0)
# Bir hata almamak için cv2.destroyAllWindows() fonksiyonu eklenir.
cv2.destroyAllWindows()
