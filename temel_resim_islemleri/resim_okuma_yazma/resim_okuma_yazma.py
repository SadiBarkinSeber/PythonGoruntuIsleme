import cv2
# Resim img = cv2.imread fonksiyonu ile eklenir.
# Virgülden sonra 0 ekleyerek resmi siyah beyaz hale getiririz.
img = cv2.imread("stormtrooper.jpg", 0)
# Resim cv2.imshow fonksiyonu ile gösterilir.
cv2.imshow("stormtrooper", img)
# Renklerini değiştirdiğimiz resme gri ismini vererek kaydederiz.
cv2.imwrite("gri.png", img)
# Ekran biz kapatana kadar açık kalsın diye cv2.waitKey eklenir.
cv2.waitKey(0)
# Bir hata almamak için cv2.destroyAllWindows() fonksiyonu eklenir.
cv2.destroyAllWindows()