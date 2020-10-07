import numpy as np
import cv2
# Resim değişkeni oluşturup, resmi çağırırız.
resim = cv2.imread('a7.jpg')
# Resmi gri formata çeviriyoruz.
griton = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
# Tip dönüşümü yapıyoruz.
griton = np.float32(griton)
# Tahmini 300 köşe, 10 px işlemler yapsın.
koseler = cv2.goodFeaturesToTrack(griton, 300, 0.01, 10)
# Tip dönüşümü yaparak en baştaki haline döndürdük.
koseler = np.int0(koseler)
# For döngüsüyle köseleri buluruz.
for kose in koseler:
    # Her köşenin x ve y değerlerini aldık.
    x, y = kose.ravel()
    # Bulduğumuz köşelere daire ile belirlemesini sağlıyoruz.
    cv2.circle(resim, (x, y), 3, 255, -1)
# Resmi göster.
cv2.imshow('koseler', resim)
# Ekran biz kapatana kadar açık kalsın diye cv2.waitKey eklenir.
cv2.waitKey(0)
# Bir hata almamak için cv2.destroyAllWindows() fonksiyonu eklenir.
cv2.destroyAllWindows()
