import cv2
import numpy as np
import OMR_Rastreo
import csv
import os
import io

# from numpy.lib import arrayutils
# from numpy import append
# import Utils

# Google Vission para ver que podemos recuperar del OCR
# from google.cloud import vision
# from PIL import Image, ImageDraw, ImageFont

#import utils.func_Get_Data as func_Get_Data
#import utils.func_DropBoxes as func_DropBoxes


# VARIABLE DEFINITION
########################################################################################################################

#webCamFeed = True
#cap = cv2.VideoCapture(1)
#cap.set(10,160)

sPath_Images ="test_images"
output_File_OMR = "Output"

widthImg  = 1000
heightImg = 900

#questions=20
#choices=4

# BORRAMOS ARCHIVO CSV
try:
    os.remove(output_File_OMR)
except: 
    pass


for filename in os.listdir(sPath_Images):

    pathImage = ""
    path_WA_Image = ""
    pathImage = ""
    path_WA_Image = ""    

    if filename.endswith(".jpg"):

        #pathImage = "C:/Users/ceneval/Downloads/Documentacion/2021/08/ProyectoSEP/Imgs/"
        #path_WA_Image = "C:/Users/ceneval/Downloads/Documentacion/2021/08/ProyectoSEP/Imgs/WA_Img/"        
        
        #pathImage = pathImage + filename
        #path_WA_Image = path_WA_Image + filename

        #sFolio = []
        #sGenero = []
        #sPromedio = []
        #sTipoSecundaria = []
        #sModalidad = []
        #sTurno = []
        sAnswers = []
        pathImage = "test_images/000001_s001.jpg"
        OMR_Rastreo.get_Answers(pathImage,path_WA_Image,widthImg,heightImg, 825,140,938,314)    
        #ID
        #sFolio = []        
        #sFolio += OMR_Rastreo.get_Folio(pathImage,path_WA_Image,heightImg,widthImg, 825,140,938,314)    
        #sFolio += OMR_Rastreo.get_Folio(pathImage,path_WA_Image,heightImg,widthImg, 827,140,938,314)    
        #strFolio = ""
        #longitud = len(sFolio)

        print("Respuestas :", sAnswers)

        #np.savetxt("output_File_OMR", strFolio,delimiter=',')

        with open(output_File_OMR, mode='a', newline="") as employee_file:
            #employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            employee_writer = csv.writer(employee_file, delimiter='|', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            #employee_writer.writerow(['Folio','Genero','Promedio','Tipo Secundaria', 'Modalidad', 'Turno', 'Respuestas'])
            employee_writer.writerow([sAnswers])
            #employee_writer.writerow([strFolio,str(sGenero[0]),0,str(sTipoSecundaria[0]),strModalidad,str(sTurno[0]),strRespuesta])

    else:
        continue