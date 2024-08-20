import cv2
import numpy as np
import logging

from datetime import datetime

## TO STACK ALL THE IMAGES IN ONE WINDOW
def stackImages(imgArray,scale,lables=[]):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
            hor_con[x] = np.concatenate(imgArray[x])
        ver = np.vstack(hor)
        ver_con = np.concatenate(hor)
    else:
        for x in range(0, rows):
            imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        hor_con= np.concatenate(imgArray)
        ver = hor
    if len(lables) != 0:
        eachImgWidth= int(ver.shape[1] / cols)
        eachImgHeight = int(ver.shape[0] / rows)
        #print(eachImgHeight)
        for d in range(0, rows):
            for c in range (0,cols):
                cv2.rectangle(ver,(c*eachImgWidth,eachImgHeight*d),(c*eachImgWidth+len(lables[d][c])*13+27,30+eachImgHeight*d),(255,255,255),cv2.FILLED)
                cv2.putText(ver,lables[d][c],(eachImgWidth*c+10,eachImgHeight*d+20),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,0,255),2)
    return ver    

def rectContour(contours):

    rectCon = []
    max_area = 0

    for i in contours:
        area = cv2.contourArea(i)
        #print("Area : ",area)    #imprime el area de todos los contornos que encuentra

        if area > 50:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            #print("Corner Points : ",len(approx))              
            if len(approx) == 4:
                rectCon.append(i)

    rectCon = sorted(rectCon, key=cv2.contourArea,reverse=True)
    #print(len(rectCon))
    return rectCon


# FOLIO
########################################################################################################################

def rectContourFolio(contours, areaSeleccion):

    logging.basicConfig(filename="C:/Users/ceneval/Downloads/Documentacion/2021/08/ProyectoSEP/Logs/LogFileName.log", level=logging.INFO)

    rectCon = []
    rectConFinal = []
    retAreasSobre = []
    max_area = 0

    for i in contours:
        area = cv2.contourArea(i)
        #print("Area : ",area)    #imprime el area de todos los contornos que encuentra
        #logging.info(area)
        #logging.error("error : ")
        #logging.debug("debug : ")

        if(area > 9000):            
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            #print("Corner Points : ",len(approx))              
            if len(approx) == 4:                
                rectCon.append(i)
                
    
    #print("Sobrevivientes : ",rectCon)
    rectCon = sorted(rectCon, key=cv2.contourArea,reverse=False)

    """     for i in rectCon:
            print("Areas Sobrevivientes : ",cv2.contourArea(i))

        for i in rectCon:
            area = cv2.contourArea(i)
            if(area == (areaSeleccion-2000)):
                rectConFinal.append(i)
            elif(area > (areaSeleccion-2000)):
                rectConFinal.append(i)
            else:
                rectConFinal.append(rectCon[0])

        if(len(rectConFinal) > 1):
            rectConFinal = rectConFinal[len(rectConFinal)-1]
    """

    #print(len(rectCon))
    #return rectConFinal    
    return rectCon

# GENERO
########################################################################################################################

def rectContourGenero(contours, areaSeleccion, perimetroSeleccion):

    now = datetime.now()
    sFilename =""
    sFilename = now.strftime('%Y%m%d%H%M%S')
    sFilename = "C:/Users/ceneval/Downloads/Documentacion/2021/08/ProyectoSEP/Logs/" + sFilename + '.log'

    logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',datefmt='%d-%m-%Y:%H:%M:%S', level=logging.INFO,filename=sFilename, filemode='w')

    rectCon = []
    rectConFinal = []
    retAreasSobre = []
    max_area = 0

    for i in contours:
        area = cv2.contourArea(i)
        #print("Area : ",area)    #imprime el area de todos los contornos que encuentra
        #logging.info(area)
        #logging.error("error : ")
        #logging.debug("debug : ")

        #if(area >= (areaSeleccion-100) and area < (areaSeleccion+ 100)):            

        peri = cv2.arcLength(i, True)
        
        #if(area > (areaSeleccion - 50) and area < (areaSeleccion + 50) and peri > (perimetroSeleccion - 50) and peri < (perimetroSeleccion + 50) ):            
        #if(area > 1500 and area < 3000):                        
        if(area > 2100):                        
            #logging.info(peri)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            #print("Corner Points : ",len(approx))              
            if len(approx) == 4:                
                logging.info(area)
                rectCon.append(i)


                
    
    #print("Sobrevivientes : ",rectCon)
    rectCon = sorted(rectCon, key=cv2.contourArea,reverse=False)


    #print(len(rectCon))
    #return rectConFinal    
    return rectCon

# PROMEDIOOOOOOOOOOOOOOOOOOO
########################################################################################################################

def rectContourPromedio(contours, areaSeleccion, perimetroSeleccion):

    rectCon = []
    max_area = 0

    for i in contours:
        area = cv2.contourArea(i)
        #print("Area : ",area)    #imprime el area de todos los contornos que encuentra
        #logging.info(area)
        #logging.error("error : ")
        #logging.debug("debug : ")

        #if(area >= (areaSeleccion-100) and area < (areaSeleccion+ 100)):            

        peri = cv2.arcLength(i, True)
        
        #if(area > (areaSeleccion - 50) and area < (areaSeleccion + 50) and peri > (perimetroSeleccion - 50) and peri < (perimetroSeleccion + 50) ):            
        #if(area > 1500 and area < 3000):                        
        if(area > 4000):                        
            #logging.info(peri)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            #print("Corner Points : ",len(approx))              
            if len(approx) == 4:                
                logging.info(area)
                rectCon.append(i)

    rectCon = sorted(rectCon, key=cv2.contourArea,reverse=False)
    #print(len(rectCon))
    return rectCon

# TIPO SECUNDARIA
########################################################################################################################


def rectContourTipoSec(contours, areaSeleccion, perimetroSeleccion):

    now = datetime.now()
    sFilename =""
    sFilename = now.strftime('%Y%m%d%H%M%S')
    sFilename = "C:/Users/ceneval/Downloads/Documentacion/2021/08/ProyectoSEP/Logs/" + sFilename + '.log'

    logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',datefmt='%d-%m-%Y:%H:%M:%S', level=logging.INFO,filename=sFilename, filemode='w')

    rectCon = []
    rectConFinal = []
    retAreasSobre = []
    max_area = 0

    for i in contours:
        area = cv2.contourArea(i)
        #print("Area : ",area)    #imprime el area de todos los contornos que encuentra
        #logging.info(area)
        #logging.error("error : ")
        #logging.debug("debug : ")

        #if(area >= (areaSeleccion-100) and area < (areaSeleccion+ 100)):            

        peri = cv2.arcLength(i, True)
        
        #if(area > (areaSeleccion - 50) and area < (areaSeleccion + 50) and peri > (perimetroSeleccion - 50) and peri < (perimetroSeleccion + 50) ):            
        #if(area > 1500 and area < 3000):                        
        if(area > 2000):                        
            #logging.info(peri)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            #print("Corner Points : ",len(approx))              
            if len(approx) == 4:                
                logging.info(area)
                rectCon.append(i)


                
    
    #print("Sobrevivientes : ",rectCon)
    rectCon = sorted(rectCon, key=cv2.contourArea,reverse=False)


    #print(len(rectCon))
    #return rectConFinal    
    return rectCon    

# MODALIDAD
########################################################################################################################


def rectContourModalidad(contours, areaSeleccion, perimetroSeleccion):

    rectCon = []
    max_area = 0

    for i in contours:
        area = cv2.contourArea(i)
        #print("Area : ",area)    #imprime el area de todos los contornos que encuentra
        #logging.info(area)
        #logging.error("error : ")
        #logging.debug("debug : ")

        #if(area >= (areaSeleccion-100) and area < (areaSeleccion+ 100)):            

        peri = cv2.arcLength(i, True)
        
        #if(area > (areaSeleccion - 50) and area < (areaSeleccion + 50) and peri > (perimetroSeleccion - 50) and peri < (perimetroSeleccion + 50) ):            
        #if(area > 1500 and area < 3000):                        
        if(area > 1800):                        
            #logging.info(peri)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            #print("Corner Points : ",len(approx))              
            if len(approx) == 4:                
                logging.info(area)
                rectCon.append(i)

    rectCon = sorted(rectCon, key=cv2.contourArea,reverse=False)
    #print(len(rectCon))
    return rectCon


# TURNO
########################################################################################################################


def rectContourTurno(contours, areaSeleccion, perimetroSeleccion):

    rectCon = []
    max_area = 0

    for i in contours:
        area = cv2.contourArea(i)
        #print("Area : ",area)    #imprime el area de todos los contornos que encuentra
        #logging.info(area)
        #logging.error("error : ")
        #logging.debug("debug : ")

        #if(area >= (areaSeleccion-100) and area < (areaSeleccion+ 100)):            

        peri = cv2.arcLength(i, True)
        
        #if(area > (areaSeleccion - 50) and area < (areaSeleccion + 50) and peri > (perimetroSeleccion - 50) and peri < (perimetroSeleccion + 50) ):            
        #if(area > 1500 and area < 3000):                        
        if(area > 1580):                        
            #logging.info(peri)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            #print("Corner Points : ",len(approx))              
            if len(approx) == 4:                
                logging.info(area)
                rectCon.append(i)

    rectCon = sorted(rectCon, key=cv2.contourArea,reverse=False)
    #print(len(rectCon))
    return rectCon


# CALIFICACIONES
########################################################################################################################

def rectContourCalificacion(contours):

    rectCon = []
    max_area = 0

    for i in contours:
        area = cv2.contourArea(i)
        #print("Area : ",area)    #imprime el area de todos los contornos que encuentra
        #logging.info(area)
        #logging.error("error : ")
        #logging.debug("debug : ")

        #if(area >= (areaSeleccion-100) and area < (areaSeleccion+ 100)):            

        peri = cv2.arcLength(i, True)
        
        #if(area > (areaSeleccion - 50) and area < (areaSeleccion + 50) and peri > (perimetroSeleccion - 50) and peri < (perimetroSeleccion + 50) ):            
        #if(area > 1500 and area < 3000):                        
        if(area > 100):                        
            #logging.info(peri)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            #print("Corner Points : ",len(approx))              
            if len(approx) == 4:                
                logging.info(area)
                rectCon.append(i)

    rectCon = sorted(rectCon, key=cv2.contourArea,reverse=False)
    #print(len(rectCon))
    return rectCon


def getCornerPoints(cont):
    peri = cv2.arcLength(cont, True) # LENGTH OF CONTOUR
    approx = cv2.approxPolyDP(cont, 0.02 * peri, True) # APPROXIMATE THE POLY TO GET CORNER POINTS
    #approx = cv2.approxPolyDP(cont, 0.03 * peri, True) # APPROXIMATE THE POLY TO GET CORNER POINTS
    return approx


def reorder(myPoints):

    myPoints = myPoints.reshape((4, 2)) # REMOVE EXTRA BRACKET
    #print(myPoints)
    myPointsNew = np.zeros((4, 1, 2), np.int32) # NEW MATRIX WITH ARRANGED POINTS
    add = myPoints.sum(1)
    #print(add)
    #print(np.argmax(add))
    myPointsNew[0] = myPoints[np.argmin(add)]  #[0,0]
    myPointsNew[3] =myPoints[np.argmax(add)]   #[w,h]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] =myPoints[np.argmin(diff)]  #[w,0]
    myPointsNew[2] = myPoints[np.argmax(diff)] #[h,0]

    return myPointsNew

def splitBoxes(img, iRows, iCols):
    rows = np.vsplit(img,iRows)
    #cv2.imshow("Split", rows[0])
    boxes=[]
    for r in rows:
        cols= np.hsplit(r,iCols)
        for box in cols:
            boxes.append(box)
            #cv2.imshow("Split", box)
    return boxes

def ret_x_cord_contour(contours):
    if cv2.contourArea(contours) > 500:
        cent_moment = cv2.moments(contours)
        return (int(cent_moment['m10']/cent_moment['m00']))
    else:
        pass


def identify_centroid(image, centroid):
    # places a blue circle on the centers of contours
    cent_moment = cv2.moments(centroid)
    centroid_x = int(cent_moment['m10'] / cent_moment['m00'])
    centroid_y = int(cent_moment['m01'] / cent_moment['m00'])

    # draw blue circles on the contours
    cv2.circle(image,(centroid_x,centroid_y),10,(255,0,0),1)

    return image


def finf_contour_areas(contours):
    areas = []
    for cnt in contours:
        cont_area = cv2.contourArea(cnt)
        areas.append(cont_area)
    
    return areas 