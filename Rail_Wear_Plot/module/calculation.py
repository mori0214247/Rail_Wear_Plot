import math
from shapely.geometry import Polygon #https://pypi.org/project/polygon/
import dataclasses
from module import initialize

@dataclasses.dataclass(frozen=True)
class Calculation:
   #t0d0:Non_Wear_data_areaをまた読んでるのが冗長な気がする
   Non_Wear_data_area=initialize.NonWearDataGroup.Non_wear_data_area
   
   #三角関数で摩耗量からXY座標を算出するメソッド
   def sin_calc(theta,nX,nY,Wear,col_name_temp):
      #NonWear_calc：摩耗なしY座標(対辺長さ)とΘの組み合わせで斜辺を求める。
      NW_C = nY/math.sin(math.radians(theta))
      
      #斜辺から摩耗量を引いた長さを求める
      W_C = NW_C- Wear
      
      #W_Cに同Θをそれぞれ組み合わせて、XY座標へ変換する
      W_X = round(W_C*math.cos(math.radians(theta)),4)
      W_Y = round(W_C*math.sin(math.radians(theta)),4)
      
      #角度Θが0°か180°の場合は、三角関数使わずにnXを計算する
      if theta == 0 or theta ==180:
         W_Y=0
         W_X=nX-Wear-32.5#マジックナンバーではない
      
      Wear_plot_dict={"Wear":Wear,"W_X":W_X,"W_Y":W_Y,"col_name_temp":col_name_temp,"csv_x":nX,"csv_Y":nY}
      return Wear_plot_dict
   
   #XY座標21点からポリゴンを作成して面積を求めるメソッド
   def wear_area_calc(Wear_Calc_data,Area_name,output_dir):
      vertices_X = [Wear_Calc_data[key]["W_X"] for key in Wear_Calc_data.keys()]
      vertices_Y = [Wear_Calc_data[key]["W_Y"] for key in Wear_Calc_data.keys()]
      vertices_XY = [(vertices_X[i], vertices_Y[i]) for i in range(len(vertices_X))]
      
      polygon = Polygon(vertices_XY)
      XY_area = polygon.area
      XY_area_per_Non_Wear_data=XY_area/Calculation.Non_Wear_data_area
      dict_Wear_area_calc_result={
         "XY_area":XY_area,"polygon":polygon,"XY_area_per_Non_Wear_data":XY_area_per_Non_Wear_data,
         "vertices_XY":vertices_XY,"Area_name":Area_name,"result_output_dir":output_dir}
      return dict_Wear_area_calc_result
   
         # #検算ケース100(単位)^2になる
      # points = {
      #    'A': (0, 0),
      #    'B': (10, 0),
      #    'C': (10, 10),
      #    'D': (0, 10)

      # }
      # # 4点を反時計回りに並べる
      # vertices = [points[key] for key in sorted(points.keys())]
      # # 多角形を作成する
      # polygon = Polygon(vertices)
      # #検算ケース終わり