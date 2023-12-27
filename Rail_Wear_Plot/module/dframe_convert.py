from module import  calculation
import dataclasses
import numpy as np


#左断面=Bレール
#右断面=Aレール
@dataclasses.dataclass
class Dataframe_Convert:
    def __init__(self,name):
        self.name = name
        
    B_RnW_step = [i for i in range(0,21)] #0~20の21step
    A_RnW_step = [i for i in range(20,-1,-1)] #20~0の21step
    B_step_point = [i for i in range(1,22)] #1~21の21step
    A_step_point = [i for i in range(22,44)] #22~43の21step
    step_theata =[th for th in range(0,181,9)] #0180含む21step

    def dframe_convert(df,origin_X,origin_Y,ARnW,BRnW,df_index):
        
        kiro_tei = df.iloc[:,0][df_index]
        dict_W_A_plot=dict()
        dict_W_B_plot=dict()
        Nan_count=0
        
        for i_A,i_B,A_RnW,B_RnW,i_theata in zip(
            Dataframe_Convert.A_step_point, Dataframe_Convert.B_step_point,Dataframe_Convert.A_RnW_step,Dataframe_Convert.B_RnW_step,Dataframe_Convert.step_theata):
                    nX=BRnW.X[B_RnW]-origin_X
                    nY=BRnW.Y[B_RnW]-origin_Y
                    Wear=df.iloc[:,i_B][df_index]
                    #csv摩耗量の一部がNaNであれば0埋めする
                    if np.isnan(Wear):
                        Wear=0
                        Nan_count=Nan_count+1
                    col_name_temp = df.columns[i_B]+"_"+str(i_theata)+"度"
                    W_B_plot=calculation.Calculation.sin_calc(i_theata,nX,nY,Wear,col_name_temp)
                    dict_W_B_plot[col_name_temp]=W_B_plot
            
                    nX=ARnW.X[A_RnW]-origin_X
                    nY=ARnW.Y[A_RnW]-origin_Y
                    Wear=df.iloc[:,i_A][df_index]
                    #csv摩耗量の一部がNaNであれば0埋めする
                    if np.isnan(Wear):
                        Wear=0
                        Nan_count=Nan_count+1
                    col_name_temp = df.columns[i_A]+"_"+str(i_theata)+"度"
                    W_A_plot=calculation.Calculation.sin_calc(i_theata,nX,nY,Wear,col_name_temp)
                    dict_W_A_plot[col_name_temp]=W_A_plot

        dict_calc_after={"キロ程":kiro_tei,"右断面_Aレール":dict_W_A_plot,"左断面_Bレール":dict_W_B_plot,"欠損値数":Nan_count}
        return dict_calc_after