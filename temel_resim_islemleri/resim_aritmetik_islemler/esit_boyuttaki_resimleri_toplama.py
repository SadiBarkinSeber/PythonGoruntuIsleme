import cv2
import numpy as np
# Resimler eklenir.
img1 = cv2.imread("a4.jpg")
img2 = cv2.imread("a5.jpg")
# Resimler üst üste sırayla toplanır. İlk yazılan resim altta ikinci yazılan
# resim üstünde görünür. Yoğunluklarıyla oynayarak belirginlikleri değiştirilebilir.
toplam = cv2.addWeighted(img1, 0.2, img2, 0.8, 0)
# Toplam ismi verilen resim gösterilir.
cv2.imshow("toplam", toplam)
# Ekran biz kapatana kadar açık kalsın diye cv2.waitKey eklenir.
cv2.waitKey(0)
# Bir hata almamak için cv2.destroyAllWindows() fonksiyonu eklenir.
cv2.destroyAllWindows()
