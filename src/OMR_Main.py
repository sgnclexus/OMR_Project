import cv2
import numpy as np
from numpy.lib import utils
from numpy.lib.function_base import append
import Utils
import OMR_Rastreo
import csv
import os
import io

#Google Vission para ver que podemos recuperar del OCR
from google.cloud import vision
from PIL import Image, ImageDraw, ImageFont

import func_Get_Data
import func_DropBoxes


# VARIABLE DEFINITION
########################################################################################################################

#webCamFeed = True
#cap = cv2.VideoCapture(1)
#cap.set(10,160)

sPath ="test_images"
output_File_OMR = "Outputs"

heightImg = 1000
widthImg  = 900
#questions=20
#choices=4

#BORRAMOS ARCHIVO CSV
try:
    os.remove(output_File_OMR)
except: 
    pass


for filename in os.listdir(sPath):

    pathImage = ""
    path_WA_Image = ""
    pathImage = ""
    path_WA_Image = ""    


    if filename.endswith(".jpg"):

        pathImage ="C:/Users/ceneval/Downloads/Documentacion/2021/08/ProyectoSEP/Imgs/"
        path_WA_Image = "C:/Users/ceneval/Downloads/Documentacion/2021/08/ProyectoSEP/Imgs/WA_Img/"
        
        
        pathImage = pathImage + filename
        path_WA_Image = path_WA_Image + filename

        sFolio = []
        sGenero = []
        sPromedio = []
        sTipoSecundaria = []
        sModalidad = []
        sTurno = []
        sResp = []


        #ID
        sFolio = []        
        #sFolio += OMR_Rastreo.get_Folio(pathImage,path_WA_Image,heightImg,widthImg, 825,140,938,314)    
        sFolio += OMR_Rastreo.get_Folio(pathImage,path_WA_Image,heightImg,widthImg, 827,140,938,314)    
        strFolio = ""
        longitud = len(sFolio)

        for i in range(longitud):
            strFolio += sFolio[i]

        #GENERO
        sGenero = []                
        #sGenero += OMR_Rastreo.get_Genero(pathImage,path_WA_Image,heightImg,widthImg, 345,135,405,180) 
        sGenero += OMR_Rastreo.get_Genero(pathImage,path_WA_Image,heightImg,widthImg, 345,143,405,180) 

        strGenero = ""
        iLongGenero = 0
        iLongGenero = len(sGenero) 

        for i in range(iLongGenero):
            strGenero += sGenero[i]


        #PROMEDIO
        sPromedio = []        
        #sPromedio += OMR_Rastreo.get_Promedio(pathImage,path_WA_Image,heightImg,widthImg, 440,145,478,269)  
        #sPromedio += OMR_Rastreo.get_Promedio(pathImage,path_WA_Image,heightImg,widthImg, 440,143,484,271)  

        #TIPO SECUNDARIA
        sTipoSecundaria = []
        #sTipoSecundaria = OMR_Rastreo.get_TipoSec(pathImage,path_WA_Image,heightImg,widthImg, 677,175,715,285)  #semibuena
        sTipoSecundaria = OMR_Rastreo.get_TipoSec(pathImage,path_WA_Image,heightImg,widthImg, 674,175,718,285)  

        strTipoSecundaria = ""
        ilongitudTS = len(sTipoSecundaria)

        for i in range(ilongitudTS):
            strTipoSecundaria += sTipoSecundaria[i]

        #MODALIDAD
        sModalidad = []
        ##sModalidad = OMR_Rastreo.get_Modalidad(pathImage,path_WA_Image,heightImg,widthImg, 777,175,817,240) #Semibuena 
        sModalidad = OMR_Rastreo.get_Modalidad(pathImage,path_WA_Image,heightImg,widthImg, 775,187,813,234)  

        strModalidad = ""
        longitudM = len(sModalidad)

        for i in range(longitudM):
            strModalidad += sModalidad[i]


        #TURNO
        sTurno = []
        sTurno = OMR_Rastreo.get_Turno(pathImage,path_WA_Image,heightImg,widthImg, 771,278,815,310)  

        strTurno = ""
        iLongTurno = 0
        iLongTurno = len(sTurno)

        for i in range(iLongTurno):
            strTurno += sTurno[i]



        #Respuestas
        sResp = []
        sResp += OMR_Rastreo.get_Respuestas(pathImage,path_WA_Image,heightImg,widthImg, 75,408,199,871)    #SECTION A
        sResp += OMR_Rastreo.get_Respuestas(pathImage,path_WA_Image,heightImg,widthImg,225,408,345,871)    #SECTION B
        sResp += OMR_Rastreo.get_Respuestas(pathImage,path_WA_Image,heightImg,widthImg,373,408,493,871)    #SECTION C
        #sResp += OMR_Rastreo.get_Respuestas(pathImage,path_WA_Image,heightImg,widthImg,517,410,646,865)    #SECTION D LO TUVE Q HACE UN POCO GRANDE
        sResp += OMR_Rastreo.get_Respuestas(pathImage,path_WA_Image,heightImg,widthImg,517,410,648,865)    #SECTION D LO TUVE Q HACE UN POCO GRANDE
        sResp += OMR_Rastreo.get_Respuestas(pathImage,path_WA_Image,heightImg,widthImg,670,410,790,865)    #SECTION E
        sResp += OMR_Rastreo.get_Respuestas(pathImage,path_WA_Image,heightImg,widthImg,818,408,938,871)    #SECTION F

        strRespuesta = ""
        longitudR = len(sResp)

        for i in range(longitudR):
            strRespuesta += sResp[i]

        print("Folio :", strFolio)
        print("Genero :", strGenero)
        print("Promedio :", sPromedio)
        print("Tipo Secundaria :", strTipoSecundaria)
        print("Modalidad :", strModalidad)
        print("Turno :", strTurno)
        print("Respuestas :", strRespuesta)

        #np.savetxt("output_File_OMR", strFolio,delimiter=',')

        with open(output_File_OMR, mode='a', newline="") as employee_file:
            #employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            employee_writer = csv.writer(employee_file, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            #employee_writer.writerow(['Folio','Genero','Promedio','Tipo Secundaria', 'Modalidad', 'Turno', 'Respuestas'])
            employee_writer.writerow([strFolio,strGenero,0,strTipoSecundaria,strModalidad,strTurno,strRespuesta])
            #employee_writer.writerow([strFolio,str(sGenero[0]),0,str(sTipoSecundaria[0]),strModalidad,str(sTurno[0]),strRespuesta])

    else:
        continue