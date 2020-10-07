import cv2
import numpy as np

# () içine "b5.mp4" yazarsanız kalabalık bir videodaki performansını görürsünüz.
# () içine "b6.mp4" yazarsanız durum tespiti yaptığını hareket algıladığını daha rahat görebilirsiniz.
# () içine "0" yazarsanız webcamden kendinizi görürsünüz. Haraket ederken
# hareketinizi algılayıp hareket halinde uyarısını verdiğini görebilirsiniz.
cap = cv2.VideoCapture(0)
# Genişlik için bu fonksiyonu ekleriz.
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# Yükseklik için bu fonksiyonu ekleriz.
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fourcc--> (Four character code) pixel formatlarını, renk formatlarını,
# sıkıştırma formatlarını standart bir biçimde tanımlamlar.
# İlk parametremiz kayıt edilecek olan videonun ismi.q
# İkinci parametre kullanacağımız fourcc algoritmamız.
# Üçüncü parametremiz saniyedeki çerçeve oranı (FPS)
# Dördüncü parametremiz ise kaydedilecek olan videonun çözünürlük oranlarıdır.
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
# Videonun ismi -> "output"
# Fourcc algoritmamız -> fourcc
# FPS -> 5.0
# Videonun çözünürlük oranı -> 1280x720
out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1280, 720))
# cap.read(), bir bool döndürür. Böylece bu Dönüş değerini kontrol ederek
# videoyu kontrol edebiliriz. Burada frame1 için bool döndürüyoruz.
ret, frame1 = cap.read()
# cap.read(), bir bool döndürür. Böylece bu Dönüş değerini kontrol ederek
# videoyu kontrol edebiliriz. Burada frame2 için bool döndürüyoruz.
ret, frame2 = cap.read()
print(frame1.shape)
# Cap.isOpened () yöntemiyle yakalamayı başlatılıp başlatılmadığını
# kontrol edebiliriz.
while cap.isOpened():
    # Arka plan temizleme işlemini absdiff metodu ile yaparız.
    diff = cv2.absdiff(frame1, frame2)
    # Videoda işlem yapabilmek için video tonunu griye çeviririz.
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    # Gauss bulanıklığı sırasıyla sigmaX ve sigmaY değerlerine değer verilir.
    # Standart sapmayı belirtmiş oluruz.
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # threshold = binary, görüntünün siyah ve beyaz olarak tanımlanmasıdır.
    # Görüntü üzerindeki gürültüleri azaltmak veya nesne belirlemek için kullanırız.
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    # Bu genişletme sayesinde piksel gurupları büyütürüz bu sayede pikseller arası boşluklar küçülür.
    dilated = cv2.dilate(thresh, None, iterations=3)
    #  cv.findContours() fonksiyonunda üç argüman vardır;
    #  birincisi kaynak görüntü, --> dilated
    #  ikincisi kontur alma modu, --> cv2.RETR_TREE
    #  üçüncüsü kontur yaklaşımı metodu --> cv2.CHAIN_APPROX_SIMPLE
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Contourları bulmak için bir for döngüsü kurarız.
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        # Kontur alanını 900den daha küçük olucak şekilde belirledik.
        if cv2.contourArea(contour) < 900:
            continue
        # Dikdörtgenler yeşil renkli ve 2px kalınlığındadır.
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Ekrana beyaz renkte 2px kalınlığında Durumlari: Haraket halinde yazdırız.
        # Yazının konumu x=10, y=30. eksenlerden başlıcak şekilde olur.
        cv2.putText(frame1, "Durum: {}".format('Haraket halinde'), (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 255, 255), 2)
    # Çerçece boyutunu 1280x720 şeklinde ayarlarız.
    image = cv2.resize(frame1, (1280, 720))
    # Yazmayı durdur.
    out.write(image)
    # Pencereye Goruntu ismini veririz.
    cv2.imshow("Goruntu", frame1)
    # İşlemler bittikten sonra frame1 ve frame2'yi eşitleriz.
    frame1 = frame2
    # videoyu kontrol edebiliriz. Burada frame2 için bool döndürüyoruz.
    ret, frame2 = cap.read()
    # q tuşuna basıldığında pencereyi kapat.
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
# Her şeyi kapat.
cv2.destroyAllWindows()
# Kamerayı serbest bırak.
cap.release()
# Her şeyi kapat.
out.release()
