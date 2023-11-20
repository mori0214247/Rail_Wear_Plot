import pandas as pd

# CSVファイルを読み込み、データフレームにする
def csv_fileload(dir_path,Analyze_file):
    temp = dir_path+"/"+ Analyze_file
    df_ymd = pd.read_csv(temp,encoding="shift_jis",nrows=1,header=None) 
    df_csv = pd.read_csv(temp,encoding="shift_jis",skiprows=1) 
    col_leng=len(df_csv.index)
    return df_csv