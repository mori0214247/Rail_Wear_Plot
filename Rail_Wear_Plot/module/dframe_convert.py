from module.calculation import Calculation
import dataclasses
import numpy as np

#左断面=Bレール
#右断面=Aレール
@dataclasses.dataclass
class DataframeConvert:

    def dframe_convert(df,origin_X,origin_Y,ARnW,BRnW,df_index):
        #df_indexがcsvファイル行です。df_indexの値に追従してキロ程が増加していく
        kiro_tei = df.iloc[:,0][df_index]
        dict_W_A_plot=dict()
        dict_W_B_plot=dict()
        Nan_count=0
        
        #step_tupple_listの動きが謎....
        A_RnW_step = [i for i in range(20,-1,-1)] #20~0の21step  
        B_RnW_step = [i for i in range(0,21)] #0~20の21step
        A_step_point = [i for i in range(22,44)] #22~43の21step
        B_step_point = [i for i in range(1,22)] #1~21の21step
        step_theata =[th for th in range(0,181,9)] #0~180を含む9°/stepで21step
        #ステップのタプルを作成、AとBを同関数内で計算する
        #[(20, 0, 22, 1, 0), (19, 1, 23, 2, 9), (18, 2, 24, 3, 18)...  とタプルのリストになる。)
         #t0d0：あんまり良い実装に見えないので、直すかも:24/01/04
         #print(list(step_tupple_list))
        step_tupple_list=zip(A_step_point,B_step_point,A_RnW_step,B_RnW_step,step_theata)

        for i_A,i_B,A_RnW,B_RnW,i_theata in step_tupple_list:
                    nX=BRnW.X[B_RnW]-origin_X
                    nY=BRnW.Y[B_RnW]-origin_Y
                    Wear=df.iloc[:,i_B][df_index]
                    #csvで読み込んだ摩耗量の一部がNaNであれば0埋めする
                    if np.isnan(Wear):
                        Wear=0
                        Nan_count=Nan_count+1
                    col_name_temp = df.columns[i_B]+"_"+str(i_theata)+"度"#名前を作成してるだけ
                    
                    #【important】三角関数で摩耗量から座標に換算する↓
                    W_B_plot=Calculation.sin_calc(i_theata,nX,nY,Wear,col_name_temp)
                    dict_W_B_plot[col_name_temp]=W_B_plot
            
                    nX=ARnW.X[A_RnW]-origin_X
                    nY=ARnW.Y[A_RnW]-origin_Y
                    Wear=df.iloc[:,i_A][df_index]
                    #csvで読み込んだ摩耗量の一部がNaNであれば0埋めする
                    if np.isnan(Wear):
                        Wear=0
                        Nan_count=Nan_count+1
                    col_name_temp = df.columns[i_A]+"_"+str(i_theata)+"度"
                    
                    #【important】三角関数で摩耗量から座標に換算する↓
                    W_A_plot=Calculation.sin_calc(i_theata,nX,nY,Wear,col_name_temp)
                    dict_W_A_plot[col_name_temp]=W_A_plot

        dict_calc_after={"キロ程":kiro_tei,"右断面_Aレール":dict_W_A_plot,"左断面_Bレール":dict_W_B_plot,"欠損値数":Nan_count}
        return dict_calc_after