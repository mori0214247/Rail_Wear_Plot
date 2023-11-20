import pandas as pd

from  module import Load_setting 
from  module import Logmaker as Lm

def initialize():
#設定ファイル読み込み
    setting_js = Load_setting.load_json('settings.json')

    #摩耗なしデータを読み込み
    ARnW = pd.read_csv(setting_js['A_Rail_nonWear'],encoding="shift_jis",na_values=[0])
    BRnW = pd.read_csv(setting_js['B_Rail_nonWear'],encoding="shift_jis",na_values=[0])
    #座標設定値を読み込み
    abs_origin_X = setting_js['origin_X']
    abs_origin_Y = setting_js['origin_Y']

    #解析対象CSVフォルダのディレクトリを設定ファイルから読み込み
    dir_path= setting_js['File_Directory']

    #解析対象ログを書き出し、解析対象リストを渡す
    Analyze_list=Lm.log_maker(dir_path,".CSV","Load_list_","解析対象ファイル数")

    return setting_js,dir_path,Analyze_list,ARnW,BRnW,abs_origin_X,abs_origin_Y