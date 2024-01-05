#設定ファイルjsonを読み込み、諸々参照してレール摩耗なしのデータを読み込むモジュール
#解析対象ファイルをLogに書き出す、解析対象リストをmainに返す
import pandas as pd
from  module import Load_setting 
from  module import Logmaker as Lm
import dataclasses
from shapely.geometry import Polygon

#設定ファイル読み込み
setting_js = Load_setting.load_json('settings.json')

#摩耗なしのデータを読み込む
#データクラスによるクラス定義、初期値なのでイミュータブル(変更不可)として与える:(frozen=True)箇所で設定
@dataclasses.dataclass(frozen=True)
class NonWearDataGroup:
    #ARnW：A_Rail_non_Wearの略、Bも同様
    ARnW = pd.read_csv(setting_js['A_Rail_nonWear'],encoding="shift_jis",na_values=[0])
    BRnW = pd.read_csv(setting_js['B_Rail_nonWear'],encoding="shift_jis",na_values=[0]) 
    
    ARnW_XY_List= ARnW.values.tolist()
    ARnW_offset=ARnW.copy()
    ARnW_offset["X"]=ARnW_offset["X"].add(-32.5)#t0d0:グラフ出力への座標範囲をあわせている、定数じゃなくしたい
    ARnW_offset["Y"]=ARnW_offset["Y"].add(-120.5)#t0d0:同上
    
    #ポリゴンデータ生成し、摩耗なし断面の面積計算
    Non_wear_data_polygon = Polygon(ARnW_XY_List)
    Non_wear_data_area = Non_wear_data_polygon.area   

@dataclasses.dataclass(frozen=True)
class SettingGroup:
    #座標設定値を読み込み
    abs_origin_X = setting_js['origin_X']
    abs_origin_Y = setting_js['origin_Y']

    #解析対象CSVフォルダのディレクトリのiniファイルによる指定
    dir_path= setting_js['File_Directory']

    #解析対象キロ程レンジをiniファイルにより指定
    Kirotei_range= setting_js['kirotei_range']
    
    #解析結果の出力先ディレクトリのiniファイルによる指定
    result_output_dir= setting_js["Output_Directory"]
    
    #解析結果フラフ出力フォーマットのiniファイルによる指定
    result_output_graph_format= setting_js["Output_graph_format"]

    #解析対象ログを書き出し
    Analyze_list=Lm.log_maker(setting_js['File_Directory'],".CSV","Load_list_","解析対象ファイル数")
    



#以下はデータクラスモジュール使用しない場合の上記クラス定義の記述、Python3.7以前の書き方
# class Non_Wear_data:
#     def __init__(self):
#         self.testname="test"
#         self.ARnW = pd.read_csv(setting_js['A_Rail_nonWear'],encoding="shift_jis",na_values=[0])
#         self.BRnW = pd.read_csv(setting_js['B_Rail_nonWear'],encoding="shift_jis",na_values=[0])
#         #座標設定値を読み込み
#         self.abs_origin_X = setting_js['origin_X']
#         self.abs_origin_Y = setting_js['origin_Y']
#         #解析対象CSVフォルダのディレクトリを設定ファイルから読み込み
#         self.dir_path= setting_js['File_Directory']
#         #解析対象ログを書き出し
#         self.Analyze_list=Lm.log_maker(self.dir_path,".CSV","Load_list_","解析対象ファイル数")
       
