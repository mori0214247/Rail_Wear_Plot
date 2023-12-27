import pandas as pd
from module import initialize
from dataclasses import dataclass

@dataclass
class inputdata:
    NWd = initialize.NonWeardata_Group
    Setting =initialize.Setting_Group
    
    filename:str
    data:Setting.Analyze_list
    dir_path:Setting.dir_path

    def read_csv_files(filename,dir_path):
        with open(dir_path+"/"+filename) as f:
         df_csv = pd.read_csv(f,encoding="shift_jis",skiprows=1)
        return df_csv


             
            
             
             




# # CSVファイルを読み込み、データフレームにする
# def csv_fileload(dir_path,Analyze_file):
#     temp = dir_path+"/"+ Analyze_file
#     df_ymd = pd.read_csv(temp,encoding="shift_jis",nrows=1,header=None) 
#     df_csv = pd.read_csv(temp,encoding="shift_jis",skiprows=1) 
#     col_leng=len(df_csv.index)
#     return df_csv,df_ymd