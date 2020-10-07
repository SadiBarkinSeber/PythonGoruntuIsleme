import os

import cv2
import numpy as np
import math
import random

import Main
import Preprocess
import PossibleChar

# modül seviyesi değişkenleri ##########################################################################

kNearest = cv2.ml.KNearest_create()

        # checkIfPossibleChar için sabitler, bu yalnızca olası bir karakteri kontrol eder (başka bir karakterle karşılaştırılmaz
MIN_PIXEL_WIDTH = 2
MIN_PIXEL_HEIGHT = 8

MIN_ASPECT_RATIO = 0.25
MAX_ASPECT_RATIO = 1.0

MIN_PIXEL_AREA = 80

        # iki karakteri karşılaştırmak için sabitler
MIN_DIAG_SIZE_MULTIPLE_AWAY = 0.3
MAX_DIAG_SIZE_MULTIPLE_AWAY = 5.0

MAX_CHANGE_IN_AREA = 0.5

MAX_CHANGE_IN_WIDTH = 0.8
MAX_CHANGE_IN_HEIGHT = 0.2

MAX_ANGLE_BETWEEN_CHARS = 12.0

        # diğer sabitler
MIN_NUMBER_OF_MATCHING_CHARS = 3

RESIZED_CHAR_IMAGE_WIDTH = 20
RESIZED_CHAR_IMAGE_HEIGHT = 30

MIN_CONTOUR_AREA = 100

###################################################################################################
def loadKNNDataAndTrainKNN():
    allContoursWithData = []                # boş listeler
    validContoursWithData = []

    try:
        npaClassifications = np.loadtxt("classifications.txt", np.float32)
    except:                                                                                 # dosya açılamazsa
        print("error, unable to open classifications.txt, exiting program\n")  # show error message
        os.system("pause")
        return False                                                                        # Yanlış döndür
    # sonlandır try

    try:
        npaFlattenedImages = np.loadtxt("flattened_images.txt", np.float32)                 # görüntülerinde okuyun
    except:                                                                                 # dosya açılamazsa
        print("error, unable to open flattened_images.txt, exiting program\n")
        os.system("pause")
        return False
    # sonlandır try

    npaClassifications = npaClassifications.reshape((npaClassifications.size, 1))       # numpy dizisini 1d'ye yeniden şekillendir, eğitmek için çağrıya geçmek için gerekli

    kNearest.setDefaultK(1)                                                             # varsayılan K'yı 1'e ayarla

    kNearest.train(npaFlattenedImages, cv2.ml.ROW_SAMPLE, npaClassifications)

    return True
# sonlandır function

###################################################################################################
def detectCharsInPlates(listOfPossiblePlates):
    intPlateCounter = 0
    imgContours = None
    contours = []

    if len(listOfPossiblePlates) == 0:
        return listOfPossiblePlates
    # sonlandır if

            # bu noktada olası platelerin listesinin en az bir  plate içerdiğinden emin olabiliriz

    for possiblePlate in listOfPossiblePlates:          # olası her plate için bu, işlevin çoğunu alan büyük bir döngüdür

        possiblePlate.imgGrayscale, possiblePlate.imgThresh = Preprocess.preprocess(possiblePlate.imgPlate)

        if Main.showSteps == True: # adımları göster ###################################################
            cv2.imshow("5a", possiblePlate.imgPlate)
            cv2.imshow("5b", possiblePlate.imgGrayscale)
            cv2.imshow("5c", possiblePlate.imgThresh)
        # sonlandır if # adımları göster #####################################################################

                # Daha kolay görüntüleme için plaka görüntüsünün boyutunu artırın
        possiblePlate.imgThresh = cv2.resize(possiblePlate.imgThresh, (0, 0), fx = 1.6, fy = 1.6)

                # gri alanları ortadan kaldırmak için yeniden eşik
        thresholdValue, possiblePlate.imgThresh = cv2.threshold(possiblePlate.imgThresh, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        if Main.showSteps == True: # adımları göster ###################################################
            cv2.imshow("5d", possiblePlate.imgThresh)
        # sonlandır if # adımları göster #####################################################################

        # bu işlev önce tüm konturları bulur, sonra yalnızca karakter olabilecek konturları içerir (henüz diğer karakterlerle karşılaştırmadan)
        listOfPossibleCharsInPlate = findPossibleCharsInPlate(possiblePlate.imgGrayscale, possiblePlate.imgThresh)

        if Main.showSteps == True: # adımları göster ###################################################
            height, width, numChannels = possiblePlate.imgPlate.shape
            imgContours = np.zeros((height, width, 3), np.uint8)
            del contours[:]

            for possibleChar in listOfPossibleCharsInPlate:
                contours.append(possibleChar.contour)
            # sonlandır for

            cv2.drawContours(imgContours, contours, -1, Main.SCALAR_WHITE)

            cv2.imshow("6", imgContours)
        # sonlandır if # adımları göster #####################################################################

                # tüm olası karakterlerin bir listesi verildiğinde, plakadaki eşleşen karakter gruplarını bulun
        listOfListsOfMatchingCharsInPlate = findListOfListsOfMatchingChars(listOfPossibleCharsInPlate)

        if Main.showSteps == True: # adımları göster ###################################################
            imgContours = np.zeros((height, width, 3), np.uint8)
            del contours[:]

            for listOfMatchingChars in listOfListsOfMatchingCharsInPlate:
                intRandomBlue = random.randint(0, 255)
                intRandomGreen = random.randint(0, 255)
                intRandomRed = random.randint(0, 255)

                for matchingChar in listOfMatchingChars:
                    contours.append(matchingChar.contour)
                # sonlandır for
                cv2.drawContours(imgContours, contours, -1, (intRandomBlue, intRandomGreen, intRandomRed))
            # sonlandır for
            cv2.imshow("7", imgContours)
        # sonlandır if # adımları göster #####################################################################

        if (len(listOfListsOfMatchingCharsInPlate) == 0):			# plakada eşleşen karakter grupları yoksa

            if Main.showSteps == True: # adımları göster ###############################################
                print("chars found in plate number " + str(
                    intPlateCounter) + " = (none), click on any image and press a key to continue . . .")
                intPlateCounter = intPlateCounter + 1
                cv2.destroyWindow("8")
                cv2.destroyWindow("9")
                cv2.destroyWindow("10")
                cv2.waitKey(0)
            # sonlandır if # adımları göster #################################################################

            possiblePlate.strChars = ""
            continue
        # sonlandır if

        for i in range(0, len(listOfListsOfMatchingCharsInPlate)):
            listOfListsOfMatchingCharsInPlate[i].sort(key = lambda matchingChar: matchingChar.intCenterX)
            listOfListsOfMatchingCharsInPlate[i] = removeInnerOverlappingChars(listOfListsOfMatchingCharsInPlate[i])
        # sonlandır for

        if Main.showSteps == True: # adımları göster ###################################################
            imgContours = np.zeros((height, width, 3), np.uint8)

            for listOfMatchingChars in listOfListsOfMatchingCharsInPlate:
                intRandomBlue = random.randint(0, 255)
                intRandomGreen = random.randint(0, 255)
                intRandomRed = random.randint(0, 255)

                del contours[:]

                for matchingChar in listOfMatchingChars:
                    contours.append(matchingChar.contour)
                # sonlandır for

                cv2.drawContours(imgContours, contours, -1, (intRandomBlue, intRandomGreen, intRandomRed))
            # sonlandır for
            cv2.imshow("8", imgContours)
        # sonlandır if # adımları göster #####################################################################

                # olası her plaka içinde, potansiyel eşleşen karakterlerin en uzun listesinin gerçek karakter listesi olduğunu varsayalım
        intLenOfLongestListOfChars = 0
        intIndexOfLongestListOfChars = 0

                # eşleşen karakterlerin tüm vektörleri arasında döngü yapın, en çok karaktere sahip olanın dizinini alın
        for i in range(0, len(listOfListsOfMatchingCharsInPlate)):
            if len(listOfListsOfMatchingCharsInPlate[i]) > intLenOfLongestListOfChars:
                intLenOfLongestListOfChars = len(listOfListsOfMatchingCharsInPlate[i])
                intIndexOfLongestListOfChars = i
            # sonlandır if
        # sonlandır for

                94 / 5000
                # plakadaki en uzun eşleşen karakter listesinin gerçek karakter listesi olduğunu varsayalım
        longestListOfMatchingCharsInPlate = listOfListsOfMatchingCharsInPlate[intIndexOfLongestListOfChars]

        if Main.showSteps == True: # adımları göster ###################################################
            imgContours = np.zeros((height, width, 3), np.uint8)
            del contours[:]

            for matchingChar in longestListOfMatchingCharsInPlate:
                contours.append(matchingChar.contour)
            # sonlandır for

            cv2.drawContours(imgContours, contours, -1, Main.SCALAR_WHITE)

            cv2.imshow("9", imgContours)
        # sonlandır if # adımları göster #####################################################################

        possiblePlate.strChars = recognizeCharsInPlate(possiblePlate.imgThresh, longestListOfMatchingCharsInPlate)

        if Main.showSteps == True: # adımları göster ###################################################
            print("chars found in plate number " + str(
                intPlateCounter) + " = " + possiblePlate.strChars + ", click on any image and press a key to continue . . .")
            intPlateCounter = intPlateCounter + 1
            cv2.waitKey(0)
        # sonlandır if # adımları göster #####################################################################

    # işlevin çoğunu alan büyük for döngüsünün sonu

    if Main.showSteps == True:
        print("\nchar detection complete, click on any image and press a key to continue . . .\n")
        cv2.waitKey(0)
    # sonlandır if

    return listOfPossiblePlates
# sonlandır function

###################################################################################################
def findPossibleCharsInPlate(imgGrayscale, imgThresh):
    listOfPossibleChars = []                        # bu dönüş değeri olacak
    contours = []
    imgThreshCopy = imgThresh.copy()

            # plakadaki tüm konturları bul
    contours, npaHierarchy = cv2.findContours(imgThreshCopy, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:                        # her kontur için
        possibleChar = PossibleChar.PossibleChar(contour)

        if checkIfPossibleChar(possibleChar):              # kontur olası bir karakter ise, bunun diğer karakterlerle (henüz) karşılaştırılmadığını unutmayın. . .
            listOfPossibleChars.append(possibleChar)       # olası karakter listesine ekle
        # sonlandır if
    # sonlandır if

    return listOfPossibleChars
# sonlandır function

###################################################################################################
def checkIfPossibleChar(possibleChar):
            # bu işlev, bir karakter olup olmadığını görmek için bir kontur üzerinde kaba bir kontrol yapan bir 'ilk geçiştir',
            # Bir grup aramak için (henüz) karakteri diğer karakterlerle karşılaştırmadığımızı unutmayın.
    if (possibleChar.intBoundingRectArea > MIN_PIXEL_AREA and
        possibleChar.intBoundingRectWidth > MIN_PIXEL_WIDTH and possibleChar.intBoundingRectHeight > MIN_PIXEL_HEIGHT and
        MIN_ASPECT_RATIO < possibleChar.fltAspectRatio and possibleChar.fltAspectRatio < MAX_ASPECT_RATIO):
        return True
    else:
        return False
    # sonlandır if
# sonlandır function

###################################################################################################
def findListOfListsOfMatchingChars(listOfPossibleChars):
            # bu işlevle, tek bir büyük listede tüm olası karakterlerle başlıyoruz
            # Bu işlevin amacı, tek bir büyük karakter listesini eşleşen karakter listeleri halinde yeniden düzenlemek.
            # bir grup maçta bulunmayan karakterlerin daha fazla dikkate alınmasına gerek olmadığını unutmayın
    listOfListsOfMatchingChars = []                  # bu dönüş değeri olacak

    for possibleChar in listOfPossibleChars:                        # tek büyük karakter listesindeki her olası karakter için
        listOfMatchingChars = findListOfMatchingChars(possibleChar, listOfPossibleChars)        # büyük listedeki mevcut karakterle eşleşen tüm karakterleri bul

        listOfMatchingChars.append(possibleChar)                # ayrıca geçerli karakteri mevcut olası eşleşen karakter listesine ekle

        if len(listOfMatchingChars) < MIN_NUMBER_OF_MATCHING_CHARS:     # mevcut olası eşleşen karakter listesi, olası bir plakayı oluşturmaya yetecek kadar uzun değilse
            continue                            # for döngüsünün başına geri dönün ve sonraki karakterle tekrar deneyin, bunun gerekli olmadığını unutmayın
                                                # olası bir plaka olmak için yeterli karaktere sahip olmadığından listeyi herhangi bir şekilde kaydetmek
        # sonlandır if

                                                # buraya gelirsek, mevcut liste, eşleşen karakterlerin bir "grubu" veya "kümesi" olarak testi geçti
        listOfListsOfMatchingChars.append(listOfMatchingChars)      # eşleşen karakterler listemize ekleyin

        listOfPossibleCharsWithCurrentMatchesRemoved = []

                                                # mevcut eşleşen karakter listesini büyük listeden kaldırın, böylece aynı karakterleri iki kez kullanmayız,
                                                # orijinal büyük listeyi değiştirmek istemediğimizden bunun için yeni bir büyük liste yaptığınızdan emin olun.
        listOfPossibleCharsWithCurrentMatchesRemoved = list(set(listOfPossibleChars) - set(listOfMatchingChars))

        recursiveListOfListsOfMatchingChars = findListOfListsOfMatchingChars(listOfPossibleCharsWithCurrentMatchesRemoved)      # yinelemeli çağrı

        for recursiveListOfMatchingChars in recursiveListOfListsOfMatchingChars:        # özyinelemeli çağrı tarafından bulunan her eşleşen karakter listesi için
            listOfListsOfMatchingChars.append(recursiveListOfMatchingChars)             # eşleşen karakterlerin orijinal listemize ekleyin
        # sonlandır for

        break       #  for dan çık

    # sonlandır for

    return listOfListsOfMatchingChars
# sonlandır function

###################################################################################################
def findListOfMatchingChars(possibleChar, listOfChars):
            # bu işlevin amacı, olası bir karakter ve olası karakterlerin büyük bir listesi verildiğinde,
            # Büyük listedeki tek olası karakter için eşleşen tüm karakterleri bulun ve eşleşen bu karakterleri liste olarak geri getirin
    listOfMatchingChars = []

    for possibleMatchingChar in listOfChars:
        if possibleMatchingChar == possibleChar:    # Eşleşmeleri bulmaya çalıştığımız karakter, şu anda kontrol ettiğimiz büyük listedeki karakterle tam olarak aynı ise
                                                    # o zaman mevcut karakter dahil olmak üzere iki katına çıkacak b / c eşleşmeleri listesine dahil etmemeliyiz
            continue                                # bu yüzden eşleşme listesine eklemeyin ve for döngüsünün en üstüne atlamayın
        # sonlandır if
                    # karakterlerin eşleşip eşleşmediğini görmek için bir şeyler hesaplayın
        fltDistanceBetweenChars = distanceBetweenChars(possibleChar, possibleMatchingChar)

        fltAngleBetweenChars = angleBetweenChars(possibleChar, possibleMatchingChar)

        fltChangeInArea = float(abs(possibleMatchingChar.intBoundingRectArea - possibleChar.intBoundingRectArea)) / float(possibleChar.intBoundingRectArea)

        fltChangeInWidth = float(abs(possibleMatchingChar.intBoundingRectWidth - possibleChar.intBoundingRectWidth)) / float(possibleChar.intBoundingRectWidth)
        fltChangeInHeight = float(abs(possibleMatchingChar.intBoundingRectHeight - possibleChar.intBoundingRectHeight)) / float(possibleChar.intBoundingRectHeight)

                # karakterlerin eşleşip eşleşmediğini kontrol et
        if (fltDistanceBetweenChars < (possibleChar.fltDiagonalSize * MAX_DIAG_SIZE_MULTIPLE_AWAY) and
            fltAngleBetweenChars < MAX_ANGLE_BETWEEN_CHARS and
            fltChangeInArea < MAX_CHANGE_IN_AREA and
            fltChangeInWidth < MAX_CHANGE_IN_WIDTH and
            fltChangeInHeight < MAX_CHANGE_IN_HEIGHT):

            listOfMatchingChars.append(possibleMatchingChar)
        # sonlandır if
    # sonlandır for

    return listOfMatchingChars
# sonlandır function

###################################################################################################
# iki karakter arasındaki mesafeyi hesaplamak için Pisagor teoremini kullanın
def distanceBetweenChars(firstChar, secondChar):
    intX = abs(firstChar.intCenterX - secondChar.intCenterX)
    intY = abs(firstChar.intCenterY - secondChar.intCenterY)

    return math.sqrt((intX ** 2) + (intY ** 2))
# sonlandır function

###################################################################################################
# karakterler arasındaki açıyı hesaplamak için temel trigonometri (SOH CAH TOA) kullanın
def angleBetweenChars(firstChar, secondChar):
    fltAdj = float(abs(firstChar.intCenterX - secondChar.intCenterX))
    fltOpp = float(abs(firstChar.intCenterY - secondChar.intCenterY))

    if fltAdj != 0.0:                           # Merkez X konumları eşitse sıfıra bölmediğimizden emin olmak için kontrol edin, sıfıra kayan bölme Python'da bir çökmeye neden olur
        fltAngleInRad = math.atan(fltOpp / fltAdj)
    else:
        fltAngleInRad = 1.5708                          # eğer bitişik sıfırsa, bunu açı olarak kullanın, bu programın C ++ sürümü ile tutarlı olmalıdır
    # sonlandır if

    fltAngleInDeg = fltAngleInRad * (180.0 / math.pi)       # açıyı derece cinsinden hesapla

    return fltAngleInDeg
# sonlandır function

###################################################################################################
# Çakışan iki karakterimiz varsa veya muhtemelen ayrı karakterler olması için birbirine yakınsa, iç (daha küçük) karakteri kaldırın,
# bu, aynı karakter için iki kontur bulunursa aynı karakteri iki kez eklemeyi önlemek içindir,
# örneğin 'O' harfi için hem iç halka hem de dış halka kontur olarak bulunabilir, ancak biz sadece bir kez karakter eklemeliyiz
def removeInnerOverlappingChars(listOfMatchingChars):
    listOfMatchingCharsWithInnerCharRemoved = list(listOfMatchingChars)                # bu dönüş değeri olacaktır

    for currentChar in listOfMatchingChars:
        for otherChar in listOfMatchingChars:
            if currentChar != otherChar:        # mevcut karakter ve diğer karakter aynı karakter değilse. . .
                                                                            # mevcut karakter ve diğer karakter hemen hemen aynı konumda merkez noktalarına sahipse. . .
                if distanceBetweenChars(currentChar, otherChar) < (currentChar.fltDiagonalSize * MIN_DIAG_SIZE_MULTIPLE_AWAY):
                                # Buraya gelirsek örtüşen karakterler bulduk
                                # daha sonra hangi karakterin daha küçük olduğunu belirleriz, sonra bu karakter önceki geçişte zaten kaldırılmamışsa, onu kaldırırız.
                    if currentChar.intBoundingRectArea < otherChar.intBoundingRectArea:         # mevcut karakter diğer karakterden daha küçükse
                        if currentChar in listOfMatchingCharsWithInnerCharRemoved:              # mevcut karakter önceki bir geçişte zaten kaldırılmamışsa. . .
                            listOfMatchingCharsWithInnerCharRemoved.remove(currentChar)         # sonra mevcut karakteri kaldır
                        # sonlandır if
                    else:                                                                       # başka bir karakter mevcut karakterden daha küçükse
                        if otherChar in listOfMatchingCharsWithInnerCharRemoved:                # diğer karakter önceki geçişte zaten kaldırılmamışsa. . .
                            listOfMatchingCharsWithInnerCharRemoved.remove(otherChar)           # sonra diğer karakterleri kaldır
                        # sonlandır if
                    # sonlandır if
                # sonlandır if
            # sonlandır if
        # sonlandır for
    # sonlandır for

    return listOfMatchingCharsWithInnerCharRemoved
# sonlandır function

###################################################################################################
# gerçek karakter tanımayı uyguladığımız yer burasıdır
def recognizeCharsInPlate(imgThresh, listOfMatchingChars):
    strChars = ""               # bu dönüş değeri olacak, plakadaki karakterler

    height, width = imgThresh.shape

    imgThreshColor = np.zeros((height, width, 3), np.uint8)

    listOfMatchingChars.sort(key = lambda matchingChar: matchingChar.intCenterX)        # karakterleri soldan sağa sırala

    cv2.cvtColor(imgThresh, cv2.COLOR_GRAY2BGR, imgThreshColor)                     # Eşik görüntüsünün renkli versiyonunu yapın, böylece üzerine renkli konturlar çizebiliriz

    for currentChar in listOfMatchingChars:
        pt1 = (currentChar.intBoundingRectX, currentChar.intBoundingRectY)
        pt2 = ((currentChar.intBoundingRectX + currentChar.intBoundingRectWidth), (currentChar.intBoundingRectY + currentChar.intBoundingRectHeight))

        cv2.rectangle(imgThreshColor, pt1, pt2, Main.SCALAR_GREEN, 2)

                # karakter eşik dışında kırp resimi
        imgROI = imgThresh[currentChar.intBoundingRectY : currentChar.intBoundingRectY + currentChar.intBoundingRectHeight,
                           currentChar.intBoundingRectX : currentChar.intBoundingRectX + currentChar.intBoundingRectWidth]

        imgROIResized = cv2.resize(imgROI, (RESIZED_CHAR_IMAGE_WIDTH, RESIZED_CHAR_IMAGE_HEIGHT))           # resmi yeniden boyutlandır, bu karakter tanıma için gereklidir

        npaROIResized = imgROIResized.reshape((1, RESIZED_CHAR_IMAGE_WIDTH * RESIZED_CHAR_IMAGE_HEIGHT))        # görüntüyü 1d numpy dizisine düzleştir

        npaROIResized = np.float32(npaROIResized)               # 1d numpy dizi dizisinden 1d numpy float dizisine dönüştür

        retval, npaResults, neigh_resp, dists = kNearest.findNearest(npaROIResized, k = 1)

        strCurrentChar = str(chr(int(npaResults[0][0])))            # sonuçlardan karakter al

        strChars = strChars + strCurrentChar                        # geçerli karakteri tam dizeye ekle

    # sonlandır for

    if Main.showSteps == True: # adımları göster #######################################################
        cv2.imshow("10", imgThreshColor)
    # sonlandır if # adımları göster #########################################################################

    return strChars
# sonlandır function

