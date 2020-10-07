import cv2

img = cv2.imread("a2.jpg")
cv2.imshow("img", img)
# Belirlenmiş alana mavi renkte bir dikdörtgen eklenir.
cv2.rectangle(img, (303, 145), (325, 195), (255, 0, 0), 2)
cv2.imshow('dortgen', img)
# Ekran biz kapatana kadar açık kalsın diye cv2.waitKey eklenir.
cv2.waitKey(0)
# Bir hata almamak için cv2.destroyAllWindows() fonksiyonu eklenir.
cv2.destroyAllWindows()
