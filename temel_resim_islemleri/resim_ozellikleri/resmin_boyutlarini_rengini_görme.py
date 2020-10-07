import cv2
import numpy as np

# Resim img = cv2.imread fonksiyonu ile eklenir.
img = cv2.imread("a1.jpg",)
# print(str(img.shape)) resmin boyutlarını bize gösterir.
print(str(img.shape))
# print(str(len(img.shape))) metoduyla bir resmin siyah beyaz yada renkli olup olmadığını anlarız.
# siyah-beyaz(2), renli(3)
print(str(len(img.shape)))
# Resim cv2.imshow fonksiyonu ile gösterilir.
cv2.imshow("sehir", img)
# Ekran biz kapatana kadar açık kalsın diye cv2.waitKey eklenir.
cv2.waitKey(0)
# Bir hata almamak için cv2.destroyAllWindows() fonksiyonu eklenir.
cv2.destroyAllWindows()
