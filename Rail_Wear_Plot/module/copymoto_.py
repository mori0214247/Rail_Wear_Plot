import pandas as pd
import matplotlib.pyplot as plt
#from tkinter import filedialog
import os
import math
import numpy as np
import scipy.interpolate as scipl
from scipy.interpolate import lagrange
#import csv
from scipy import signal, interpolate

dir = 'C:/'
#fld = filedialog.askdirectory(initialdir = dir) 
fld = "D:/202310_断面摩耗データ解析/千代田線断面摩耗データ"
print(fld)

A_Rail_nonWear = "D:/202310_断面摩耗データ解析/A_Rail_nonWear.csv"
B_Rail_nonWear = "D:/202310_断面摩耗データ解析/B_Rail_nonWear.csv"

ARnW = pd.read_csv(A_Rail_nonWear,encoding="shift_jis",na_values=[0])
BRnW = pd.read_csv(B_Rail_nonWear,encoding="shift_jis",na_values=[0])

origin_X = 32.5
origin_Y = 120.5

dir_path = fld
files = os.listdir(dir_path) 
#print(files)

def sin_plot(theta,nX,nY,Wear,col_name_temp):
    nW_C = nY/math.sin(math.radians(theta))
    W_C = nW_C- Wear
    W_X = round(W_C*math.cos(math.radians(theta)),4)
    W_Y = round(W_C*math.sin(math.radians(theta)),4)
    if nY == 0.0:
       W_Y=0
       W_X=nX-Wear
    
    return Wear,W_X,W_Y,col_name_temp

# プロット作成
#図内タイトル準備※改行join
def plot_wear_first(list_W,A_B):

    f_a =f
    F_name = f_a.replace(".CSV","") + "_"+str(kiro_tei)     
    plt.figure(figsize=(5,5))
    l=list_W
    l_X=[i[1] for i in l]
    l_Y=[i[2] for i in l]
    x=l_X
    
    xnew = np.linspace(min(x), max(x), 10)
    #f_lag=lagrange(l_X,l_Y)  #ラグランジュ補間
    f_sci=interpolate.interp1d(l_X,l_Y,kind='cubic')#スプライン補間
    #plt.plot(l_X,l_Y,'-r')#,xnew,f_sci(xnew)
    plt.plot(xnew,f_sci(xnew),'-b')
    plt.title(A_B,size=10,loc="left",fontname="MS Gothic")
    plt.xlim(-50,50)
    plt.ylim(0,50)
    plt.grid()
    # プロット出力
    plt.savefig(fld+"/"+A_B+F_name+".svg")     
    plt.close()

# CSVファイルを読み込み、データフレームにする
files_file = [
    f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))
]
for  f in files_file:
    temp = fld+"/"+ f
    df_ymd = pd.read_csv(temp,encoding="shift_jis",nrows=1,header=None) 
    df = pd.read_csv(temp,encoding="shift_jis",skiprows=1) 

    step_num = 0
    col_leng=len(df.index)
    for dfline in range(0,50):#col_leng+1):
        kiro_tei = df.iloc[:,0][dfline]
        list_W_B_plot=list()
        list_W_A_plot=list()

        for theta in range(0,181,9):
            nX=BRnW.X[step_num]-origin_X
            nY=BRnW.Y[step_num]-origin_Y
            Wear=df.iloc[:,step_num+1][dfline]
            col_name_temp = df.columns[step_num+1]+"_"+str(theta)+"度"
            W_B_plot=sin_plot(theta,nX,nY,Wear,col_name_temp)
            list_W_B_plot.append(W_B_plot)
            #list_W_B_plot.append("")
            step_num=step_num + 1
        #Nan避け
        l=list_W_B_plot
        l_X=[i[1] for i in l]
        No_List_W_B = np.nanmax(l_X)
        if No_List_W_B > 0:
            plot_wear_first(list_W_B_plot,"B")
        step_num = 0
        
        for theta in range(0,181,9):
            nX=ARnW.X[step_num]-origin_X
            nY=ARnW.Y[step_num]-origin_Y
            Wear=df.iloc[:,step_num+22][dfline]
            col_name_temp = df.columns[step_num+22]+"_"+str(theta)+"度"
            W_A_plot=sin_plot(theta,nX,nY,Wear,col_name_temp)
            list_W_A_plot.append(W_A_plot)
            step_num=step_num + 1
        #Nan避け
        l=list_W_A_plot
        l_X=[i[1] for i in l]
        Sum_List_W_A = np.nanmax(l_X)
        
        if Sum_List_W_A > 0:
            plot_wear_first(list_W_A_plot,"A")
        step_num = 0
        #F_name = f.replace(".CSV","") + "_"+str(kiro_tei)
        #with open(fld+"/"+F_name+".csv","w",newline="") as f:
            #writer = csv.writer(f)
            #writer.writerow(list_W_B_plot)
            #writer.writerow(list_W_A_plot)
    

#断面情報リストを読み込み、データフレームにする
#namedf = pd.read_csv('D:/2211_レールCSV/2309_part2_bunki/Neme_List.csv',encoding="utf-8")

#print(namedf.loc[3])