import cv2
import numpy as np
from matplotlib import pyplot as plt
# Mavi rengini tanımladık.
mavi = [255, 0, 0]
# opencv.JPG remini ekledim.
img = cv2.imread('opencv.JPG')
# Her bir fonksiyona o fonksiyona ayit kenar ekledim.
# Replicate kenarlardan renkleri çekti.
replicate = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
# Reflect ile yansıtma yaptı
reflect = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT101)
# Wrap ile ters yansıttı.
wrap = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_WRAP)
# Constant ile resme mavi renk sabit bir çerçeve ekledi.
constant = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=mavi)

plt.subplot(231), plt.imshow(img, 'gray'), plt.title('orjinal')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('replicate')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('reflect')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('reflect101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('wrap')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('constant')
# Tek tek imshow yapmayarak tek Pyplot komutu ile gösterdik.
plt.show()

# Ekran biz kapatana kadar açık kalsın diye cv2.waitKey eklenir.
cv2.waitKey(0)
# Bir hata almamak için cv2.destroyAllWindows() fonksiyonu eklenir.
cv2.destroyAllWindows()
