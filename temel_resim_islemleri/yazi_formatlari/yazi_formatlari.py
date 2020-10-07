import cv2
import numpy as np

# Metin yaz adında bir format oluştururuz.
def metin_yaz():
    # Pixel alanını ve renk formatını belirledik.
    img = np.zeros((640, 900, 3), np.uint8)
    # İçini (arka planını) siyah yapıyoruz.
    img.fill(0)
    # Yazı kalınlığı.
    fontscale = 1.5
    # Yazı rengi (255,0,0) --> Mor
    color = (100, 0, 100)
    # Farklı fontlarda yazılar yazdım.
    fontface = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img, "FONT_HERSHEY_COMPLEX", (25, 40), fontface, fontscale, color)
    fontface = cv2.FONT_HERSHEY_COMPLEX_SMALL
    cv2.putText(img, "FONT_HERSHEY_COMPLEX_SMALL", (25, 80), fontface, fontscale, color)
    fontface = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(img, "FONT_HERSHEY_DUPLEX", (25, 120), fontface, fontscale, color)
    fontface = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(img, "FONT_HERSHEY_PLAIN", (25, 160), fontface, fontscale, color)
    fontface = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    cv2.putText(img, "FONT_HERSHEY_SCRIPT_COMPLEX", (25, 200), fontface, fontscale, color)
    fontface = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    cv2.putText(img, "FONT_HERSHEY_SCRIPT_SIMPLEX", (25, 240), fontface, fontscale, color)
    fontface = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, "FONT_HERSHEY_SIMPLEX", (25, 280), fontface, fontscale, color)
    fontface = cv2.FONT_HERSHEY_TRIPLEX
    cv2.putText(img, "FONT_HERSHEY_TRIPLEX", (25, 320), fontface, fontscale, color)
    fontface = cv2.FONT_ITALIC
    cv2.putText(img, "FONT_ITALIC", (25, 360), fontface, fontscale, color)
    # Çerçeveye isim verdik.
    cv2.namedWindow('text ornekler')
    # Her şeyi gösterdik.
    cv2.imshow('text ornekler', img)
    cv2.imwrite('text_ornekler.jpg', img)
    # Ekran biz kapatana kadar açık kalsın diye cv2.waitKey eklenir.
    cv2.waitKey(0)
    # Bir hata almamak için cv2.destroyAllWindows() fonksiyonu eklenir.
    cv2.destroyAllWindows()


def main():
    metin_yaz()


if __name__ == "__main__":
    main()
