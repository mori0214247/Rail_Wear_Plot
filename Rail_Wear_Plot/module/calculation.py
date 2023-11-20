import math

def sin_calc(theta,nX,nY,Wear,col_name_temp):
    nW_C = nY/math.sin(math.radians(theta))
    W_C = nW_C- Wear
    W_X = round(W_C*math.cos(math.radians(theta)),4)
    W_Y = round(W_C*math.sin(math.radians(theta)),4)
    if nY == 0.0:
       W_Y=0
       W_X=nX-Wear
    
    return Wear,W_X,W_Y,col_name_temp