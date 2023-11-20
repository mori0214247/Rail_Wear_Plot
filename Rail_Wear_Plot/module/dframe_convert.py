from module import  calculation

#左断面=Bレール
#右断面=Aレール
def dframe_convert(df,origin_X,origin_Y,ARnW,BRnW):
    step_num = 0
    col_leng=len(df.index)
    kiro_tei = df.iloc[:,0][0]
    for dfline in range(1,21):#col_leng+1):
            
            list_W_B_plot=list()

            for theta in range(0,181,9):
                nX=BRnW.X[step_num]-origin_X
                nY=BRnW.Y[step_num]-origin_Y
                Wear=df.iloc[:,step_num+1][dfline]
                col_name_temp = df.columns[step_num+1]+"_"+str(theta)+"度"
                W_B_plot=calculation.sin_calc(theta,nX,nY,Wear,col_name_temp)
                list_W_B_plot.append(W_B_plot)
                
                step_num=step_num + 1
            #Nan避け
            l=list_W_B_plot
    
    step_num = 0        
    for dfline in range(22,42):#col_leng+1)
                    
            list_W_A_plot=list()

            for theta in range(0,181,9):
                nX=ARnW.X[step_num]-origin_X
                nY=ARnW.Y[step_num]-origin_Y
                Wear=df.iloc[:,step_num+1][dfline]
                col_name_temp = df.columns[step_num+1]+"_"+str(theta)+"度"
                W_A_plot=calculation.sin_calc(theta,nX,nY,Wear,col_name_temp)
                list_W_A_plot.append(W_A_plot)
                
                step_num=step_num + 1
            #Nan避け
            l=list_W_B_plot