#摩耗なしデータを継承、設定値を読み込み
#csvファイルを1つ読み込んでpandaでデータフレームとして取得
#上の2つのあれを合わせてInputDataクラスとして定義

import pandas as pd
from module import initialize
from dataclasses import dataclass

@dataclass
class InputData:
    NWD = initialize.NonWearDataGroup
    Setting =initialize.SettingGroup
    
    filename:str
    data:Setting.Analyze_list
    dir_path:Setting.dir_path

    def read_csv_files(filename,dir_path):
        with open(dir_path+"/"+filename) as f:
         df_csv = pd.read_csv(f,encoding="shift_jis",skiprows=1)
        return df_csv
