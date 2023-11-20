#!/usr/bin/env python
from  module import initialize
from  module import calculation as calc
from  module import csv_file_load
from  module import dframe_convert as dfc

# hogehoge.py を取り込む

def main():
   Analyz_ini = initialize.initialize()
   ARnW = Analyz_ini[3] 
   BRnW = Analyz_ini[4] 
   origin_X= Analyz_ini[5] 
   origin_Y= Analyz_ini[6] 
   dir_path=Analyz_ini[1]
   counter = 0
   for Analyz_data in (Analyz_ini[2])  :
        counter = counter + 1
        df=csv_file_load.csv_fileload(dir_path,Analyz_data)
        
        #print("csv読んだ"+str(counter)+"回目")
        dfc.dframe_convert(df,origin_X,origin_Y,ARnW,BRnW)
    
    
    
if __name__ == '__main__':
    main()