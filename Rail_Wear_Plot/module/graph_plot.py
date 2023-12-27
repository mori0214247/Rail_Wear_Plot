import matplotlib.pyplot as plt
from module import initialize

# 面積比較図を作成する
def graph_plot(kirotei,dataname,Non_Wear_data_List,**Rail_Area):
    output_dir_result=Rail_Area["result_output_dir"]
    vertices_XY=Rail_Area["vertices_XY"]
    XY_area_per_Non_Wear_data=Rail_Area["XY_area_per_Non_Wear_data"]
    XY_area=Rail_Area["XY_area"]
    Area_name=Rail_Area["Area_name"]
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.add_patch(plt.Polygon(vertices_XY, color='green', alpha=0.7))
    ax.autoscale_view()
    plt.xlim([-35,35])
    plt.ylim([0,40])
    
    # テキストを追加する
    plt.text(
        0.5, 1.1, "断面積:"+str(round(XY_area,2)),va='top', ha='center', fontsize=12, color='red', fontname='MS Gothic',transform=ax.transAxes)
    plt.text(
        0.1, 1.1, "キロ程:"+str(kirotei),va='top', ha='left', fontsize=12, color='red', fontname='MS Gothic',transform=ax.transAxes)
    plt.text(
        0.1, 1.3, "data:"+dataname+"_"+Area_name,va='top', ha='center', fontsize=12, color='red', fontname='MS Gothic',transform=ax.transAxes)
    plt.text(
        0.8, 1.1, "断面積比率:"+str(round(XY_area_per_Non_Wear_data*100,3))+"%",va='top', ha='center', fontsize=12, color='red', fontname='MS Gothic',transform=ax.transAxes)
    # 図を画像ファイルとして保存する
    #fig.subplots_adjust(left=0, right=1, bottom=0, top=1)いらないはず
    plt.grid(axis="x")
    plt.minorticks_on()
    plt.grid(which = "both", axis="x")
    plt.grid(which = "both", axis="y")
    ax.add_patch(plt.Polygon(Non_Wear_data_List, color='blue', alpha=0.3))
    fig.savefig(output_dir_result+"/"+dataname+"_"+"キロ程"+str(kirotei)+"_"+Area_name+'_polygon.jpg')
    plt.clf()
    plt.close()