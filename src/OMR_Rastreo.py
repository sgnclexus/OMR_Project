import os,sys
import cv2
import numpy as np
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
from src.utils.Utils import rectContourCalificacion, getCornerPoints, reorder, splitBoxes, stackImages
# from utils.Utils import rectContourFolio,getCornerPoints,splitBoxes
#from numpy.lib import utils
# from numpy.lib.function_base import append


"""
Now we get the answers
"""
def get_Answers(img_Location,WA_img_Location,widthImg,heightImg,xs,ys,xe,ye):

    questions=10
    choices=5

    try:
        os.remove(WA_img_Location)
    except: 
        pass



    #WORKAROUND TO NOT CONSIDERAR BIGGEST BOX    
    # cv2.rectangle(img,(xs,ys),(xe,ye),(0,0,0),3) 
    # cv2.rectangle(img,(203,447),(310,962),(0,0,0),5)
    # cv2.imwrite(WA_img_Location,img)
    # PerimetroMiCuadro = (xe - xs) + (ye - ys) + (xe - xs) + (ye - ys)
    # areaMiCuadro = (xe - xs)*(ye - ys)
    # print("Area de mi Cuadrado Calificaciones : ", areaMiCuadro)
    # print("Perimetro de mi Cuadrado : ", PerimetroMiCuadro)  
    # imgWC = cv2.imread(WA_img_Location)

    # PREPROCESSING
    #imgWC = cv2.resize(imgWC, (widthImg,heightImg))
    #img = cv2.resize(img, (widthImg,heightImg))
    img = cv2.imread(img_Location)
    # cv2.imshow("Original", img)
    # cv2.waitKey(0)
    imgResized = cv2.resize(img, (widthImg,heightImg))    
    imgContours = imgResized.copy()
    imgBiggestContours = imgResized.copy()
    # cv2.imshow("Resized", imgResized)
    # cv2.waitKey(0)()    
    imgGrey = cv2.cvtColor(imgResized, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGrey, (5,5),1)
    imgCanny = cv2.Canny(imgBlur, 10,50)    
    imgBlank = np.zeros_like(imgResized)
    #imgCanny = cv2.Canny(imgGrey, 40,250)    

    # FINDING ALL CONTOURS
    contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(imgContours,contours,-1,(0,255,0),2)    

    # FIND RECTANGULES
    rectCon = rectContourCalificacion(contours)
    biggestContour = getCornerPoints(rectCon[0])
    #gradePoints = Utils.getCornerPoints(rectCon[2])

    if biggestContour.size != 0:
        cv2.drawContours(imgBiggestContours,biggestContour,-1,(255,0,0),20)
    ########################################################################################################################

    
    imageArray = ([imgResized,imgGrey,imgBlur,imgCanny],
                  [imgContours,imgBiggestContours,imgBlank,imgBlank]
                  )                    
    imgStacked = stackImages(imageArray,0.9)
    cv2.imshow("Stacked Images", imgStacked)
    cv2.waitKey(0)()    

    #WORKAROUD PARA PROCESAMIENTO
    #cv2.rectangle(imgBiggestContours,(60,455),(190,960),(0,0,0),10)
    #cv2.imwrite(imgProccesed,imgBiggestContours)
    # imgBiggestContours = cv2.resize(imgBiggestContours, (widthImg,heightImg))
    #cv2.imshow("Para Procesar",imgBiggestContours)




    # ret, threshold = cv2.threshold(imgBlur,127,255,0)
    # contours, hierarchy = cv2.findContours(threshold, cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
    #cv2.drawContours(imgContours,contours,-1,(0,255,0),5)
    #cv2.imshow("Para Procesar",imgContours)
    #cv2.waitKey(0)

    # cv2.drawContours(blacky_img,contours,-1,(0,255,0),3)
    #cv2.imshow("Para Procesar",blacky_img)
    #cv2.waitKey(0)

    #print("contador de areas antes de orden : ", Utils.finf_contour_areas(contours))

    #acomodo
    # sorted_contours_by_area = sorted(contours, key=cv2.contourArea, reverse=False)
    #print("contador de areas antes de orden : ", Utils.finf_contour_areas(sorted_contours_by_area))    

    #for sc in sorted_contours_by_area:
    #    cv2.drawContours(duplicate_img, [sc], -1, (0,0,255),3)
    #    cv2.waitKey(0)
    #    cv2.imshow('Remarca contro por cada enter', duplicate_img)
    #    cv2.waitKey(0)
    #    cv2.destroyAllWindows()



    # Revisar si calcula mi contorno
    #imgCentroides = imgWC.copy()    
    #contour_from_left_to_right = sorted(contours, key=int(Utils.ret_x_cord_contour(contours)), reverse=False)
    #for(i,c) in enumerate(contours):
    #    orig = Utils.identify_centroid(imgCentroides, c)
    
    #cv2.imshow('Contours with centroids : ', imgCentroides)
    #cv2.waitKey(0)


    # rectCon = rectContourCalificacion(contours,areaMiCuadro,PerimetroMiCuadro)
    

    # for sc in rectCon:
    #    cv2.drawContours(duplicate_img, [sc], -1, (0,0,255),3)
        #cv2.waitKey(0)
        #cv2.imshow('Remarca contro por cada enter', duplicate_img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()        


    # FIND RECTANGULES
    # rectCon = rectContourCalificacion(contours,areaMiCuadro,PerimetroMiCuadro)
    # biggestContour = getCornerPoints(rectCon[0])
    #gradePoints = Utils.getCornerPoints(rectCon[2])
    #x3 = Utils.getCornerPoints(rectCon[3])
    #x4 = Utils.getCornerPoints(rectCon[4])
    #x5 = Utils.getCornerPoints(rectCon[5])
    #x6 = Utils.getCornerPoints(rectCon[6])
    #gradePointsSA = Utils.getCornerPoints([843,438])
    #print(biggestContour)

    #Seccion A Respuestas
    #pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
    ####cv2.rectangle(imgBiggestContours,(50,450),(180,960),(254,210,235),10)
    #sa = cv2.rectangle(imgBiggestContours,(50,450),(180,960),(254,210,235),10)
    #seccionA = Utils.getCornerPoints(sa)
    #print("Seccion A : ", seccionA)

    # if biggestContour.size != 0:
    #     cv2.drawContours(imgBiggestContours,biggestContour,-1,(255,0,0),20)
        #cv2.drawContours(imgBiggestContours,gradePoints,-1,(0,255,0),20)
        #cv2.drawContours(imgBiggestContours,x3,-1,(0,0,255),20)
        #cv2.drawContours(imgBiggestContours,x4,-1,(255,0,0),20)
        #cv2.drawContours(imgBiggestContours,x5,-1,(0,255,0),20)
        #cv2.drawContours(imgBiggestContours,x6,-1,(0,0,255),20)

    # biggestContour = reorder(biggestContour)
    #gradePoints = Utils.reorder(gradePoints)


    # BIGGEST RECTANGLE WARPING
    #biggestPoints=Utils.reorder(biggestPoints) # REORDER FOR WARPING
    #cv2.drawContours(imgBigContour, biggestPoints, -1, (0, 255, 0), 20) # DRAW THE BIGGEST CONTOUR
    # pts1 = np.float32(biggestContour) # PREPARE POINTS FOR WARP
    # pts2 = np.float32([[0, 0],[widthImg, 0], [0, heightImg],[widthImg, heightImg]]) # PREPARE POINTS FOR WARP
    # matrix = cv2.getPerspectiveTransform(pts1, pts2) # GET TRANSFORMATION MATRIX
    # imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg)) # APPLY WARP PERSPECTIVE

    #pts1SA = np.float32([[0, 0],[325, 0], [0, 150],[325, 150]]) # PREPARE POINTS FOR WARP
    #pts2SA = np.float32([[0, 0],[325, 0], [0, 150],[325, 150]]) # PREPARE POINTS FOR WARP
    #matrixSA = cv2.getPerspectiveTransform(pts1SA, pts2SA) # GET TRANSFORMATION MATRIX
    #imgWarpColoredSA = cv2.warpPerspective(img, matrixSA, (widthImg, heightImg)) # APPLY WARP PERSPECTIVE

    #APLY THRESHOLD
    # imgWarpGray = cv2.cvtColor(imgWarpColored,cv2.COLOR_BGR2GRAY)
    # imgThresh = cv2.threshold(imgWarpGray,145,255,cv2.THRESH_BINARY_INV)[1]

    # boxes = splitBoxes(imgThresh, questions,choices)
    #cv2.imshow("Test", boxes[2])

    #print(cv2.countNonZero(boxes[0]),cv2.countNonZero(boxes[1]),cv2.countNonZero(boxes[2]),cv2.countNonZero(boxes[3]))

    # GETTING PIXEL VALUES OF EACH BOX
    # myPixelVal = np.zeros((questions,choices))
    # countC = 0
    # countR = 0

    # for image in boxes:
    #     totalPixels = cv2.countNonZero(image)
    #     myPixelVal[countR][countC] = totalPixels
    #     countC += 1
    #     if(countC == choices):
    #         countR += 1
    #         countC = 0
        
    #print(myPixelVal)

    # myIndex = []
    # sResp = []

    # for x in range(0,questions):
    #     arr = myPixelVal[x]
    #     #print("arr",arr)
    #     myInsdexVal = np.where(arr==np.amax(arr))
    #     #print(myInsdexVal[0])
    #     #print("Maximo : ",np.amax(arr))
    #     myIndex.append(myInsdexVal[0][0])

    #     if(np.amax(arr) >= 6000 and myInsdexVal[0][0] == 0):
    #         sResp.append("A")
    #     elif(np.amax(arr) >= 6000 and myInsdexVal[0][0] == 1):
    #         sResp.append("B")
    #     elif(np.amax(arr) >= 6000 and myInsdexVal[0][0] == 2):
    #         sResp.append( "C")
    #     elif(np.amax(arr) >= 6000 and myInsdexVal[0][0] == 3):
    #         sResp.append( "D")        
    #     else:        
    #         sResp.append("*") 

    #print(sResp)



    #cv2.imshow("Arreglo de Imagenes ", imgStacked)
    #cv2.waitKey(0)
    sResp = ""
    return sResp

