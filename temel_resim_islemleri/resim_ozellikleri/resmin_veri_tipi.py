import cv2
import numpy as np

# Resim img = cv2.imread fonksiyonu ile eklenir.
img = cv2.imread("a1.jpg",)
# print(img.dtype) Resmin veri tipini gösterir.
print(img.dtype)
cv2.imshow("sehir", img)
# Ekran biz kapatana kadar açık kalsın diye cv2.waitKey eklenir.
cv2.waitKey(0)
# Bir hata almamak için cv2.destroyAllWindows() fonksiyonu eklenir.
cv2.destroyAllWindows()
