import cv2

def main():
    img = cv2.imread('stormtrooper.jpg')
    ekran_cozunulurluk = 500, 400
    # Genişlik skalası
    skala_genislik = ekran_cozunulurluk[0] / img.shape[1]
    # Yükseklik skalası
    skala_yukseklik = ekran_cozunulurluk[1] / img.shape[0]
    # Hangsisi düşükse onu parametre alıyoruz.
    skala = min(skala_genislik, skala_yukseklik)
    # Genişlik ve yüksekliği skala ile çarparız.
    pencere_genislik = int(img.shape[1] * skala)
    pencere_yukseklik = int(img.shape[0] * skala)
    # Pencerenin boyutlanabilir olması sağlanır.
    cv2.namedWindow("Resim", cv2.WINDOW_NORMAL)
    # Pencere verdiğimiz değerlere göre yeniden boyutlanır.
    cv2.resizeWindow("Resim", pencere_genislik, pencere_yukseklik)
    # Resmi gösterdik.
    cv2.imshow("Resim", img)
    # Ekran biz kapatana kadar açık kalsın diye cv2.waitKey(0) eklenir.
    cv2.waitKey(0)
    # Bir hata almamak için cv2.destroyAllWindows() fonksiyonu eklenir.
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
