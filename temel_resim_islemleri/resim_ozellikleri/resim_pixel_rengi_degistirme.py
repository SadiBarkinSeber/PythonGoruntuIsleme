import cv2
import numpy as np

# Resim img = cv2.imread fonksiyonu ile eklenir.
img = cv2.imread("a1.jpg", )
# Resim cv2.imshow fonksiyonu ile gösterilir.
cv2.imshow("sehir", img)
# Resmin 100x100 pixeli içindeki kırmızı renge erişilir.
# Mavi(0), Yeşil(1), Kırmızı(2)
print(str(img.item(100, 100, 1)))
# 100x100 pixelindeki mavi pixeline 255 renk kodunu atarız.
img.itemset((100, 100, 0), 255)
# Ekran biz kapatana kadar açık kalsın diye cv2.waitKey eklenir.
cv2.waitKey(0)
# Bir hata almamak için cv2.destroyAllWindows() fonksiyonu eklenir.
cv2.destroyAllWindows()
