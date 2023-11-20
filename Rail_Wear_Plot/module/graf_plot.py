import matplotlib.pyplot as plt
#from tkinter import filedialog
import numpy as np
import scipy.interpolate as scipl
from scipy.interpolate import lagrange
#import csv
from scipy import signal, interpolate

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