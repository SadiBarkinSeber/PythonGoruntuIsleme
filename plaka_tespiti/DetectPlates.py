import cv2
import numpy as np
import math
import Main
import random

import Preprocess
import DetectChars
import PossiblePlate
import PossibleChar

# modül seviyesi değişkenleri ##########################################################################
PLATE_WIDTH_PADDING_FACTOR = 1.3
PLATE_HEIGHT_PADDING_FACTOR = 1.5

###################################################################################################
def detectPlatesInScene(imgOriginalScene):
    listOfPossiblePlates = []

    height, width, numChannels = imgOriginalScene.shape

    imgGrayscaleScene = np.zeros((height, width, 1), np.uint8)
    imgThreshScene = np.zeros((height, width, 1), np.uint8)
    imgContours = np.zeros((height, width, 3), np.uint8)

    cv2.destroyAllWindows()

    if Main.showSteps == True: #
        cv2.imshow("0", imgOriginalScene)
    # sonlandır if # adımları göster #########################################################################

    imgGrayscaleScene, imgThreshScene = Preprocess.preprocess(imgOriginalScene)         #  Gri tonlamalı ve eşik görüntülerini elde etmek için ön işlem

    if Main.showSteps == True: # adımları göster #######################################################
        cv2.imshow("1a", imgGrayscaleScene)
        cv2.imshow("1b", imgThreshScene)
    # sonlandır if # adımları göster #########################################################################

            # sahnedeki tüm olası karakterleri bul,
            # bu işlev önce tüm konturları bulur, sonra yalnızca karakter olabilecek konturları içerir (henüz diğer karakterlerle karşılaştırılmadan)
    listOfPossibleCharsInScene = findPossibleCharsInScene(imgThreshScene)

    if Main.showSteps == True: # adımları göster #######################################################
        print("step 2 - len(listOfPossibleCharsInScene) = " + str(
            len(listOfPossibleCharsInScene)))
        imgContours = np.zeros((height, width, 3), np.uint8)

        contours = []

        for possibleChar in listOfPossibleCharsInScene:
            contours.append(possibleChar.contour)
        # sonlandır for

        cv2.drawContours(imgContours, contours, -1, Main.SCALAR_WHITE)
        cv2.imshow("2b", imgContours)
    # sonlandır if # adımları göster #########################################################################

    # olası tüm karakterlerin bir listesi verildiğinde, eşleşen karakter gruplarını bulun
    # sonraki adımlarda her eşleşen karakter grubu bir plaka olarak tanınmaya çalışacak
    listOfListsOfMatchingCharsInScene = DetectChars.findListOfListsOfMatchingChars(listOfPossibleCharsInScene)

    if Main.showSteps == True: # show steps #######################################################
        print("step 3 - listOfListsOfMatchingCharsInScene.Count = " + str(
            len(listOfListsOfMatchingCharsInScene)))

        imgContours = np.zeros((height, width, 3), np.uint8)

        for listOfMatchingChars in listOfListsOfMatchingCharsInScene:
            intRandomBlue = random.randint(0, 255)
            intRandomGreen = random.randint(0, 255)
            intRandomRed = random.randint(0, 255)

            contours = []

            for matchingChar in listOfMatchingChars:
                contours.append(matchingChar.contour)
            # sonlandır for

            cv2.drawContours(imgContours, contours, -1, (intRandomBlue, intRandomGreen, intRandomRed))
        # sonlandır for

        cv2.imshow("3", imgContours)
    # sonlandır if # adımları göster #########################################################################

    for listOfMatchingChars in listOfListsOfMatchingCharsInScene:                   # eşleşen her karakter grubu için
        possiblePlate = extractPlate(imgOriginalScene, listOfMatchingChars)         # plakayı çıkarmaya çalış

        if possiblePlate.imgPlate is not None:                          # plaka bulunursa
            listOfPossiblePlates.append(possiblePlate)                  # # olası platelerin listesine ekle
        # sonlandır if
    # sonlandır for

    print("\n" + str(len(listOfPossiblePlates)) + " possible plates found")  # 13 with MCLRNF1 image

    if Main.showSteps == True: # adımları göster #######################################################
        print("\n")
        cv2.imshow("4a", imgContours)

        for i in range(0, len(listOfPossiblePlates)):
            p2fRectPoints = cv2.boxPoints(listOfPossiblePlates[i].rrLocationOfPlateInScene)

            cv2.line(imgContours, tuple(p2fRectPoints[0]), tuple(p2fRectPoints[1]), Main.SCALAR_RED, 2)
            cv2.line(imgContours, tuple(p2fRectPoints[1]), tuple(p2fRectPoints[2]), Main.SCALAR_RED, 2)
            cv2.line(imgContours, tuple(p2fRectPoints[2]), tuple(p2fRectPoints[3]), Main.SCALAR_RED, 2)
            cv2.line(imgContours, tuple(p2fRectPoints[3]), tuple(p2fRectPoints[0]), Main.SCALAR_RED, 2)

            cv2.imshow("4a", imgContours)

            print("possible plate " + str(i) + ", click on any image and press a key to continue . . .")

            cv2.imshow("4b", listOfPossiblePlates[i].imgPlate)
            cv2.waitKey(0)
        # sonlandır for

        print("\nplate detection complete, click on any image and press a key to begin char recognition . . .\n")
        cv2.waitKey(0)
    # sonlandır if # adımları göster #########################################################################

    return listOfPossiblePlates
# sonlandır function

###################################################################################################
def findPossibleCharsInScene(imgThresh):
    listOfPossibleChars = []                # bu dönüş değeri olacaktır

    intCountOfPossibleChars = 0

    imgThreshCopy = imgThresh.copy()

    contours, npaHierarchy = cv2.findContours(imgThreshCopy, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)   # tüm konturları bul

    height, width = imgThresh.shape
    imgContours = np.zeros((height, width, 3), np.uint8)

    for i in range(0, len(contours)):                       # her kontur için

        if Main.showSteps == True: # adımları göster  ###################################################
            cv2.drawContours(imgContours, contours, i, Main.SCALAR_WHITE)
        # sonlandır if # adımları göster #####################################################################

        possibleChar = PossibleChar.PossibleChar(contours[i])

        if DetectChars.checkIfPossibleChar(possibleChar):                   # kontur olası bir karakter ise, bunun diğer karakterlerle (henüz) karşılaştırılmadığını unutmayın. . .
            intCountOfPossibleChars = intCountOfPossibleChars + 1           # olası karakter sayısını artır
            listOfPossibleChars.append(possibleChar)                        # ve olası karakterler listesine ekleyin
        # sonlandır if
    # sonlandır for

    if Main.showSteps == True: # adımları göster #######################################################
        print("\nstep 2 - len(contours) = " + str(len(contours)))
        print("step 2 - intCountOfPossibleChars = " + str(intCountOfPossibleChars))
        cv2.imshow("2a", imgContours)
    # sonlandır if # adımları göster #########################################################################

    return listOfPossibleChars
# sonlandır function


###################################################################################################
def extractPlate(imgOriginal, listOfMatchingChars):
    possiblePlate = PossiblePlate.PossiblePlate()           # bu dönüş değeri olacaktır

    listOfMatchingChars.sort(key = lambda matchingChar: matchingChar.intCenterX)        # x konumuna göre karakterleri soldan sağa sırala

            # plakanın merkez noktasını hesaplayın
    fltPlateCenterX = (listOfMatchingChars[0].intCenterX + listOfMatchingChars[len(listOfMatchingChars) - 1].intCenterX) / 2.0
    fltPlateCenterY = (listOfMatchingChars[0].intCenterY + listOfMatchingChars[len(listOfMatchingChars) - 1].intCenterY) / 2.0

    ptPlateCenter = fltPlateCenterX, fltPlateCenterY

            # plaka genişliğini ve yüksekliğini hesaplayın
    intPlateWidth = int((listOfMatchingChars[len(listOfMatchingChars) - 1].intBoundingRectX + listOfMatchingChars[len(listOfMatchingChars) - 1].intBoundingRectWidth - listOfMatchingChars[0].intBoundingRectX) * PLATE_WIDTH_PADDING_FACTOR)

    intTotalOfCharHeights = 0

    for matchingChar in listOfMatchingChars:
        intTotalOfCharHeights = intTotalOfCharHeights + matchingChar.intBoundingRectHeight
    # sonlandır for

    fltAverageCharHeight = intTotalOfCharHeights / len(listOfMatchingChars)

    intPlateHeight = int(fltAverageCharHeight * PLATE_HEIGHT_PADDING_FACTOR)

            # plaka bölgesinin düzeltme açısını hesaplayın
    fltOpposite = listOfMatchingChars[len(listOfMatchingChars) - 1].intCenterY - listOfMatchingChars[0].intCenterY
    fltHypotenuse = DetectChars.distanceBetweenChars(listOfMatchingChars[0], listOfMatchingChars[len(listOfMatchingChars) - 1])
    fltCorrectionAngleInRad = math.asin(fltOpposite / fltHypotenuse)
    fltCorrectionAngleInDeg = fltCorrectionAngleInRad * (180.0 / math.pi)

            # plaka bölgesi merkez noktasını, genişliğini ve yüksekliğini ve düzeltme açısını plakanın döndürülmüş dikdörtgen elemanına paketleyin
    possiblePlate.rrLocationOfPlateInScene = ( tuple(ptPlateCenter), (intPlateWidth, intPlateHeight), fltCorrectionAngleInDeg )

            # son adım, gerçek rotasyonu gerçekleştirmektir

            # Hesaplanan düzeltme açımız için dönüş matrisini alın
    rotationMatrix = cv2.getRotationMatrix2D(tuple(ptPlateCenter), fltCorrectionAngleInDeg, 1.0)

    height, width, numChannels = imgOriginal.shape      # orijinal resim genişliğini ve yüksekliğini açın

    imgRotated = cv2.warpAffine(imgOriginal, rotationMatrix, (width, height))       # tüm resmi döndür

    imgCropped = cv2.getRectSubPix(imgRotated, (intPlateWidth, intPlateHeight), tuple(ptPlateCenter))

    possiblePlate.imgPlate = imgCropped         # Kesilmiş plaka görüntüsünü olası plakanın uygulanabilir eleman değişkenine kopyalayın

    return possiblePlate
# sonlandır function

