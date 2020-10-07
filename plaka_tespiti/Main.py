import cv2
import numpy as np
import os

import DetectChars
import DetectPlates
import PossiblePlate


SCALAR_BLACK = (0.0, 0.0, 0.0)
SCALAR_WHITE = (255.0, 255.0, 255.0)
SCALAR_YELLOW = (0.0, 255.0, 255.0)
SCALAR_GREEN = (0.0, 255.0, 0.0)
SCALAR_RED = (0.0, 0.0, 255.0)

showSteps = False


def main():

    blnKNNTrainingSuccessful = DetectChars.loadKNNDataAndTrainKNN()

    if blnKNNTrainingSuccessful == False:
        print("\nerror: KNN traning was not successful\n")
        return
    # sonlandır if

    imgOriginalScene  = cv2.imread("LicPlateImages/1.png")   # Resmi burdan değiştirebilirsiniz.

    if imgOriginalScene is None:
        print("\nerror: image not read from file \n\n")
        os.system("pause")
        return
    # sonlandır if

    listOfPossiblePlates = DetectPlates.detectPlatesInScene(imgOriginalScene)

    listOfPossiblePlates = DetectChars.detectCharsInPlates(listOfPossiblePlates)

    cv2.imshow("imgOriginalScene", imgOriginalScene)

    if len(listOfPossiblePlates) == 0:
        print("\nno license plates were detected\n")
    else:

        listOfPossiblePlates.sort(key = lambda possiblePlate: len(possiblePlate.strChars), reverse = True)

        licPlate = listOfPossiblePlates[0]

        cv2.imshow("imgPlate", licPlate.imgPlate)
        cv2.imshow("imgThresh", licPlate.imgThresh)

        if len(licPlate.strChars) == 0:
            print("\nno characters were detected\n\n")
            return


        drawRedRectangleAroundPlate(imgOriginalScene, licPlate)

        print("\nlicense plate read from image = " + licPlate.strChars + "\n")
        print("----------------------------------------")

        writeLicensePlateCharsOnImage(imgOriginalScene, licPlate)           # Resmin üzerine plaka metni yazın

        cv2.imshow("imgOriginalScene", imgOriginalScene)                # yeniden göster

        cv2.imwrite("imgOriginalScene.png", imgOriginalScene)           # görüntüyü dosyaya yaz

    # sonlandır if else

    cv2.waitKey(0)					# kullanıcı bir tuşa basana kadar pencereleri açık tutun

    return
# sonlandır main

def drawRedRectangleAroundPlate(imgOriginalScene, licPlate):

    p2fRectPoints = cv2.boxPoints(licPlate.rrLocationOfPlateInScene)

    cv2.line(imgOriginalScene, tuple(p2fRectPoints[0]), tuple(p2fRectPoints[1]), SCALAR_RED, 2)         # 4 kırmızı çizgi çiz
    cv2.line(imgOriginalScene, tuple(p2fRectPoints[1]), tuple(p2fRectPoints[2]), SCALAR_RED, 2)
    cv2.line(imgOriginalScene, tuple(p2fRectPoints[2]), tuple(p2fRectPoints[3]), SCALAR_RED, 2)
    cv2.line(imgOriginalScene, tuple(p2fRectPoints[3]), tuple(p2fRectPoints[0]), SCALAR_RED, 2)
# sonlandır function

###################################################################################################
def writeLicensePlateCharsOnImage(imgOriginalScene, licPlate):
    ptCenterOfTextAreaX = 0                             # bu, metnin yazılacağı alanın merkezi olacaktır
    ptCenterOfTextAreaY = 0

    ptLowerLeftTextOriginX = 0                          # bu, metnin yazılacağı alanın sol alt kısmı olacaktır
    ptLowerLeftTextOriginY = 0

    sceneHeight, sceneWidth, sceneNumChannels = imgOriginalScene.shape
    plateHeight, plateWidth, plateNumChannels = licPlate.imgPlate.shape

    intFontFace = cv2.FONT_HERSHEY_SIMPLEX                      # yazı tipi seçin
    fltFontScale = float(plateHeight) / 30.0                    # temel yazı tipi ölçeği
    intFontThickness = int(round(fltFontScale * 1.5))           # yazı tipi kalınlığı

    textSize, baseline = cv2.getTextSize(licPlate.strChars, intFontFace, fltFontScale, intFontThickness)

            # merkez noktasına, genişliğe ve yüksekliğe ve açıya döndürülmüş dik açıyla ambalajını açın
    ( (intPlateCenterX, intPlateCenterY), (intPlateWidth, intPlateHeight), fltCorrectionAngleInDeg ) = licPlate.rrLocationOfPlateInScene

    intPlateCenterX = int(intPlateCenterX)              # merkezin tam sayı olduğundan emin olun
    intPlateCenterY = int(intPlateCenterY)

    ptCenterOfTextAreaX = int(intPlateCenterX)         # metin alanının yatay konumu plakayla aynıdır

    if intPlateCenterY < (sceneHeight * 0.75):                                                  # plaka görüntünün üst 3/4'ünde ise
        ptCenterOfTextAreaY = int(round(intPlateCenterY)) + int(round(plateHeight * 1.6))      # karakterleri plakanın altına yazın
    else:                                                                                       # başka bir plaka görüntünün alt 1/4'ünde ise
        ptCenterOfTextAreaY = int(round(intPlateCenterY)) - int(round(plateHeight * 1.6))      # karakterleri plakanın üstüne yazın
    # sonlandır if

    textSizeWidth, textSizeHeight = textSize                # metin boyutu genişliğini ve yüksekliği

    ptLowerLeftTextOriginX = int(ptCenterOfTextAreaX - (textSizeWidth / 2))           # metin alanının sol alt başlangıç noktasını hesapla
    ptLowerLeftTextOriginY = int(ptCenterOfTextAreaY + (textSizeHeight / 2))          # metin alanı merkezine, genişliğine ve yüksekliğine göre

            # metni resmin üzerine yaz
    cv2.putText(imgOriginalScene, licPlate.strChars, (ptLowerLeftTextOriginX, ptLowerLeftTextOriginY), intFontFace, fltFontScale, SCALAR_YELLOW, intFontThickness)
# sonlandır function

###################################################################################################
if __name__ == "__main__":
    main()

