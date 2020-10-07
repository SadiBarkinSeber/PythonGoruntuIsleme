# İlk olarak tesseract kurulumunu yapıyoruz ardından gelişmiş sistem
# ayarlarından ortam değişkenleri bölümünü açıyoruz. Sistem değişkenlerinden
# path adlı dosyanın üzerine tıklayıp düzenle diyoruz. Ardından yeni bir path ekliyoruz
# tesseract kurulu olduğu yeri path ismine yapıştırıp işlemi tamamlıyoruz.
import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseracta.exe"
img = cv2.imread("a60.png")
text = pytesseract.image_to_string(img)
print(text)
