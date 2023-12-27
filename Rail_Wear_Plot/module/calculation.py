import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import dataclasses
from module import initialize

@dataclasses.dataclass(frozen=True)
class Calculation:
   Non_Wear_data_aera=initialize.NonWeardata_Group.Non_wear_data_area
   
   def sin_calc(theta,nX,nY,Wear,col_name_temp):
      nW_C = nY/math.sin(math.radians(theta))
      W_C = nW_C- Wear
      W_X = round(W_C*math.cos(math.radians(theta)),4)
      W_Y = round(W_C*math.sin(math.radians(theta)),4)
      if nY == 0.0:
         W_Y=0
         W_X=nX-Wear-32.5
      Wear_plot_dict={"Wear":Wear,"W_X":W_X,"W_Y":W_Y,"col_name_temp":col_name_temp,"csv_x":nX,"csv_Y":nY}
      return Wear_plot_dict
   
   def Wear_area_calc(Wear_Calc_data,Area_name,output_dir):#,Non_Wear_data_aera):
      
      vertices_X = [Wear_Calc_data[key]["W_X"] for key in Wear_Calc_data.keys()]
      vertices_Y = [Wear_Calc_data[key]["W_Y"] for key in Wear_Calc_data.keys()]
      vertices_XY = [(vertices_X[i], vertices_Y[i]) for i in range(len(vertices_X))]
      
      polygon = Polygon(vertices_XY)
      XY_area = polygon.area
      XY_area_per_Non_Wear_data=XY_area/Calculation.Non_Wear_data_aera
      dict_Wear_area_calc_result={
         "XY_area":XY_area,"polygon":polygon,"XY_area_per_Non_Wear_data":XY_area_per_Non_Wear_data,"vertices_XY":vertices_XY,"Area_name":Area_name,"result_output_dir":output_dir}
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