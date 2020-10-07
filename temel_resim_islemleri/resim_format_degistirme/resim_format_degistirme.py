import cv2
import numpy as np


def kaydet(path, image, jpg_kalite=None, png_compress=None):
    # Jpg seçiliyse kalitesini gösterir. (0-100)
    if jpg_kalite:
        cv2.imwrite(path, image, [int(cv2.IMWRITE_JPEG_QUALITY), jpg_kalite])
    # Png seçiliyse kalitesini gösterir. (0-9)
    elif png_compress:
        cv2.imwrite(path, image, [int(cv2.IMWRITE_PNG_COMPRESSION), png_compress])
    # Bunların hiçbiri değilse default değerleri al.
    else:
        cv2.imwrite(path, image)


# Ana fonksiyon
def main():
    impath = "stormtrooper.jpg"
    img = cv2.imread(impath)
    # İlgili resmi gösterir.
    cv2.imshow('stormtrooper', img)
    # Jpeg formatında 60 kalitesinde kaydedelim.
    cikis_jpeg = "stormtrooper2JPG.jpg"
    kaydet(cikis_jpeg, img, jpg_kalite=60)
    # Png formatında 3 sıkıştırır.
    cikis_png = "stormtrooper2PNG.png"
    kaydet(cikis_png, img, png_compress=3)
    # Ekran biz kapatana kadar açık kalsın diye cv2.waitKey eklenir.
    cv2.waitKey(0)
    # Bir hata almamak için cv2.destroyAllWindows() fonksiyonu eklenir.
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
