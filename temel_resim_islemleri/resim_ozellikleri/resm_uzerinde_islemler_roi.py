import cv2
import numpy as np

# Resim img = cv2.imread fonksiyonu ile eklenir.
img = cv2.imread("stormtrooper.jpg", )
# roi --> Görüntü üzerinde işlemler (Region of Interest)
# İlk bileşen y ekseni, ikinci bileşen x ekseni
# roi, resmin belirli bir bölümünün alınması işlemidir
roi = img[28:190, 210:360]
cv2.imshow("roi", roi)

cv2.imshow("stormtrooper", img)
# Ekran biz kapatana kadar açık kalsın diye cv2.waitKey eklenir.
cv2.waitKey(0)
# Bir hata almamak için cv2.destroyAllWindows() fonksiyonu eklenir.
cv2.destroyAllWindows()
