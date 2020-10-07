# İlk olarak internetten get-pip.py dosyasını indiriyoruz ve indirdiğimiz
# dosyayı masa üstüne taşıyoruz. Bilgisayardan cmd komut istemcisini açıp
# içine (cd Deskop) yazarak dosyayı masa üstünden çekeceğimizi belirtiyoruz.
# get-pip.py yazarak kurulumunu yapıyoruz. Ardından pip komutu ile
# (pip install pafy)'i ve (pip install --upgrade youtube_dl) komutlarını cmd
# ekranına yazarak kurulumlarını yapıyoruz.

import cv2
import numpy as np
import pafy

# Açmak istediğimiz video linkini "" içine yazıyoruz.
# New york sokak turu videosu.
url = "https://www.youtube.com/watch?v=eZe4Q_58UTU&ab_channel=NomadicAmbience"
# Yazdığımız url'yi pafy ile tutuyoruz.
video = pafy.new(url)
# Tipini mp4 olarak belirliyoruz.
best = video.getbest(preftype="mp4")

captura = cv2.VideoCapture()

captura.open(best.url)
while True:
    ret, frame = captura.read()

    cv2.imshow('Salida', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

captura.release()
cv2.destroyAllWindows()
