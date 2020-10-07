# ilk olarak seçmek istediğiniz şekli, eşyayı belirleyin ardından
# ilk olarak seçiceğiniz eşyanın sol üstüne ardından isa sağ üstüne dokunun
# sonra sol altına ven en son olarak sağ altına dokunun ekranda mause ile belirlediğiniz
# ekranın görüntüsü çıkacaktır
import cv2
import numpy as np

circles = np.zeros((4, 2), np.int)
counter = 0
img = cv2.imread('a70.jpg')


def mousePoints(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x, y
        counter = counter + 1
        print(circles)


while True:

    if counter == 4:
        width, height = 250, 350
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow("Output Image ", imgOutput)

    for x in range(0, 4):
        cv2.circle(img, (circles[x][0], circles[x][1]), 3, (0, 255, 0), cv2.FILLED)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    cv2.imshow("Original Image ", img)
    cv2.setMouseCallback("Original Image ", mousePoints)
    cv2.waitKey(1)
