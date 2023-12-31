#!/usr/bin/env python
#from dataclasses import dataclass,field
#import numpy as np
#import math
#import time

from  module import initialize,csv_file_load,dframe_convert
from module.calculation import Calculation
from module import graph_plot
import csv
from module.graph_organizer import graph_organizer

#所要時間 CSV38ファイル、キロ程8700-9000：約20分、デバッグ有り
#outputファイルサイズ .pngで約300MB(7500ファイル)
#グラフ出力なければ一瞬です
#デバッグ無しならもっと早い

def main():
    ini_data=initialize.NonWearDataGroup
    ini_Setting=initialize.SettingGroup
    
    Non_Wear_data_List= ini_data.ARnW_offset
    Kirotei_range_settings=ini_Setting.Kirotei_range
    graph_foramat=ini_Setting.result_output_graph_format
    header_list = ['キロ程','右断面_Aレール面積','A面積比率','左断面_Bレール面積','B面積比率','データ欠損点数']
    
    for filename in ini_Setting.Analyze_list:
        df=csv_file_load.InputData.read_csv_files(filename,ini_Setting.dir_path)
        output_result_dict_list=[]
        result_dict={
            "キロ程":int,
            "右断面_Aレール面積":float,"A面積比率":float,"左断面_Bレール面積":float,"B面積比率":float,
            "データ欠損点数":int
            }
        for df_index in df.index:
            #print(df_index)
            #now=time.time()
            
            #キロ程設定値と行内キロ程を先読みして計算するかどうか判定する。
            Kirotei = df.iloc[:,0][df_index]
            match Kirotei_range_settings:
                case[0,0]:
                    pass
                case _:
                    if Kirotei_range_settings[0] < Kirotei < Kirotei_range_settings[1]:
                       pass
                    else :
                        continue
                        
            Wear_Calc=dframe_convert.DataframeConvert.dframe_convert(
                df,ini_Setting.abs_origin_X,ini_Setting.abs_origin_Y,ini_data.ARnW,ini_data.BRnW,df_index)
            A_Rail_Point_data=Wear_Calc["右断面_Aレール"]
            B_Rail_Point_data=Wear_Calc["左断面_Bレール"]
            dataneme=filename.split(".")[0]
            Nan_count=Wear_Calc["欠損値数"]

            #各_Rail_Point_dataに欠損値NaNが含まれているか確認しそれぞれの処理
            match Nan_count:
                case 0:#欠損値NaNが含まれていない場合
                    pass
                case 42: #欠損値NaNが42個であれば、処理をせず次の行へ
                    print("欠損値最大")
                    continue
                case _: #一部に欠損値NaNが含まれている場合、ファイル名へ出力
                    dataneme=dataneme+"欠損値あり"
                    print("欠損値あり")

            #面積計算、グラフ作成
            A_Rail_Area=Calculation.wear_area_calc(A_Rail_Point_data,"右断面_Aレール",ini_Setting.result_output_dir)
            graph_plot.graph_plot(Kirotei,dataneme,Non_Wear_data_List,graph_foramat,**A_Rail_Area)
            
            #面積計算、グラフ作成
            B_Rail_Area=Calculation.wear_area_calc(B_Rail_Point_data,"左断面_Bレール",ini_Setting.result_output_dir)
            graph_plot.graph_plot(Kirotei,dataneme,Non_Wear_data_List,graph_foramat,**B_Rail_Area)
            
            #1行の計算結果諸々を辞書にする。  
            result_dict["キロ程"]=Kirotei
            result_dict["右断面_Aレール面積"]=round(A_Rail_Area["XY_area"],3)
            result_dict["A面積比率"]=round(A_Rail_Area["XY_area_per_Non_Wear_data"]*100,3)
            result_dict["左断面_Bレール面積"]=round(B_Rail_Area["XY_area"],3)
            result_dict["B面積比率"]=round(B_Rail_Area["XY_area_per_Non_Wear_data"]*100,3)
            result_dict["データ欠損点数"]=Nan_count  
            output_result_dict_list.append(result_dict.copy())
            
            #elspased = time.time()-now
            #print(f"経過時間{elspased:.2f}sec")
        
        output_file_name = filename.split(".")[0]
        file_path=ini_Setting.result_output_dir+"/"+output_file_name+"_result.csv"

        with open(file_path, "w", encoding="utf-8",newline="") as f:
            writer=csv.DictWriter(f,fieldnames=header_list,lineterminator="\n")
            writer.writeheader()
            writer.writerows(output_result_dict_list)
    graph_organizer(ini_Setting.result_output_dir,graph_foramat)#グラフ出力が済んだら、フォルダへコピー、整理してくれるやつ       
         
if __name__ == '__main__':
    main()
    print("a")