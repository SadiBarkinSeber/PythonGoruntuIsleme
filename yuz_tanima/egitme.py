# dosya sistemini kaydetmek için os(operating systems) belirtiriz.
import cv2
import numpy as np
import os
from PIL import Image

# cv2 içindeki özel kütüphaneyi çağırırız.
recognizer = cv2.face.LBPHFaceRecognizer_create()
# Haarcascade dosyayını çağırırız.
cascadePath = "face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
path = 'yuz_verileri'


# resimleri ve etiketleri alması için bir fonk yazıyoruz.
def get_images_and_labels(path):
    # Başka bir dosyadan veri alırken bu işemi uyguluyoruz.
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    images = []
    labels = []
    for image_path in image_paths:
        # PIL kütüphanesinin bir özelliği () içine L yazarsak gri tona çevirir.
        image_pil = Image.open(image_path).convert('L')
        image = np.array(image_pil, 'uint8')
        #
        nbr = int(os.path.split(image_path)[1].split(".")[0].replace("face-", ""))
        print(nbr)
        # Her bir yüzü öğretiriz
        faces = faceCascade.detectMultiScale(image)
        for (x, y, w, h) in faces:
            images.append(image[y: y + h, x: x + w])
            labels.append(nbr)
            cv2.imshow("Adding faces to training set...", image[y: y + h, x: x + w])
            cv2.waitKey(10)
    return images, labels


images, labels = get_images_and_labels(path)
cv2.imshow('test', images[0])
cv2.waitKey(1)

recognizer.train(images, np.array(labels))
recognizer.write('training/trainer.yml')
cv2.destroyAllWindows()
