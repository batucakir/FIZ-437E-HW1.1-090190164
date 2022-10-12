#BATUHAN CAKIR 090190164
import random
import numpy as np
import glob
from PIL import Image

#data road
egitim_agac_yolu = glob.glob('C:/Users/BATUHAN/Desktop/grey-Source/egitim_seti/agac_egitimi/*')
egitim_top_yolu  = glob.glob('C:/Users/BATUHAN/Desktop/grey-Source/egitim_seti/top_egitimi/*')
test_agac_yolu   = glob.glob('C:/Users/BATUHAN/Desktop/grey-Source/test_seti/agac_testi/*')
test_top_yolu    = glob.glob('C:/Users/BATUHAN/Desktop/grey-Source/test_seti/top_testi/*')
"""data graying
def grilestirme(path)
    for i in os.listdir(path):
        if i.endswith('jpg'):
            img = Image.open(i)
            imgGray = img.convert('L')
            imgGray.save(i)
"""

# function input and calculate density of the data 
def image_input(path):
    sum_array = np.zeros((100,100))
    for foto in path: 
        image = Image.open(foto).convert('L')  
        sum_array = sum_array + image 
    return sum_array

array_image_egitim_agac = image_input(egitim_agac_yolu)/450              
array_image_egitim_top  = image_input(egitim_top_yolu)/450      #divided number of the data, density matrix

# function input and calculate density of the data , i used k = 4
def kNN_pixel(path, sinif):
    olasilik = 0
    for foto in path:
        row = round(random.uniform(1,98))
        column = round(random.uniform(1,98)) #98+1=99. last index
        image = Image.open(foto).convert('L') 
        test_data = np.asarray(image)
        #random pixel around 4 pixel 
        sag_row = row
        sag_column = column+1
        sol_row = row
        sol_column = column-1
        ust_row = row-1
        ust_column = column
        alt_row = row+1
        alt_column = column
        
        test_data_row_yogunluk = int(test_data[sag_row][sag_column])+int(test_data[sol_row][sol_column])
        test_data_column_yogunluk = int(test_data[ust_row][ust_column])+int(test_data[alt_row][alt_column])   
        test_data_yogunluk = (test_data_row_yogunluk+test_data_column_yogunluk)/4    #k = 4 divided 
        if (sinif == "agac"):
            if (abs(array_image_egitim_agac[row][column]-test_data_yogunluk)<abs(array_image_egitim_top[row][column]-test_data_yogunluk)):
                #That is probably a tree
                olasilik += 1
        if (sinif == "top"):
            if (abs(array_image_egitim_top[row][column]-test_data_yogunluk)<abs(array_image_egitim_agac[row][column]-test_data_yogunluk)):
                #That is probably a ball
                olasilik += 1
    return olasilik

olasilik1 = kNN_pixel(test_agac_yolu, "agac")
olasilik2 = kNN_pixel(test_top_yolu, "top")
toplam_olasilik = olasilik1 + olasilik2

print("Algorithm predicted trees %",olasilik1*2,"correct")
print("Algorithm predicted balls %",olasilik2*2,"correct")
print("Algorithm predicted classes %",toplam_olasilik, "correct")
