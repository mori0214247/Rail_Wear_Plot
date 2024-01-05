import os
import shutil

#画像結合→実用性低いと感じ断念→画像整理(ディレクトリ分け)ソフトに切り替えた。
#import glob
#from PIL import Image
#import numpy as np
#import cv2

#とても単純、画像のファイルリストを取得、
# 名前から適したディレクトリを作成して、作成したディレクトリへ画像をコピーする。
def graph_organizer(graphs_dir_path,graph_foramat):
    graphs_list=[_ for _ in os.listdir(graphs_dir_path) if _.endswith(graph_foramat)]
    for di in graphs_list:
        graph_name=di.split("_")
        line_name=""
        if "A線" in graph_name[0]:
            line_name ="A線"
        if "B線" in graph_name[0]:
            line_name ="B線"
        new_folder_path = graphs_dir_path+'/'+line_name+'/'+line_name+'_'+graph_name[1]+'/'+graph_name[3]
        if not os.path.exists(new_folder_path):#フォルダがまだ無いなら作成する。
            os.makedirs(new_folder_path)
        shutil.copyfile(graphs_dir_path+'/'+di,new_folder_path+'/'+di)
        

#画像結合→実用性低い、労力に見合わないと感じ断念→画像整理(ディレクトリ分け)ソフトに切り替えた残骸(24/01/05)
#cv2実は日本語画像ファイルの扱いがとても面倒

#     A_line_kirotei_list=[]
#     B_line_kirotei_list=[]
#     s = set()
#     for kirotei in graphs_list:
#         onlist_kirotei =kirotei.split("_")[1]
#         if "A線" in kirotei:
#             A_line_kirotei_list.append(onlist_kirotei)
#         if "B線" in kirotei:   
#             B_line_kirotei_list.append(onlist_kirotei)
    
#     A_line_copy_target_list=list(set([x for x in A_line_kirotei_list if x in s or s.add(x)]))
#     A_line_copy_target_list.sort()
#     B_line_copy_target_list=list(set([x for x in B_line_kirotei_list if x in s or s.add(x)]))
#     B_line_copy_target_list.sort()   
    
#     for target in A_line_copy_target_list:
#         A_line_target_graphs = list(filter(lambda x : x.find(target) != -1,graphs_list))
#         A_line_target_graphs.sort()
        
#     for target in B_line_copy_target_list:
#         B_line_target_graphs = list(filter(lambda x : x.find(target) != -1,graphs_list))
#         B_line_target_graphs.sort()        
    
#     for mkdir in A_line_copy_target_list:
#         new_folder_path = graphs_dir_path+'/'+ 'A線/A線_'+mkdir
#         if not os.path.exists(new_folder_path):
#             os.makedirs(new_folder_path+'/A_Rail')
#             os.makedirs(new_folder_path+'/B_Rail')
            
#     for mkdir in B_line_copy_target_list:
#         new_folder_path = graphs_dir_path+'/'+ 'B線/B線_'+mkdir
#         if not os.path.exists(new_folder_path):
#             os.makedirs(new_folder_path+'/A_Rail')
#             os.makedirs(new_folder_path+'/B_Rail')

    #os.chdir(new_folder_path)
        
        

    #     dir_add_list_A =[]
    #     dir_add_list_B =[]
    #     for dir_add in connect_target_graphs:
    #         dir_add = graphs_dir_path + "/" + dir_add 
    #         img = np.array(Image.open(dir_add))
    #         cv2_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #         if dir_add.find("Aレール"):
    #             dir_add_list_A.append(cv2_img)
    #         if dir_add.find("Bレール"):
    #             dir_add_list_B.append(cv2_img)
            
    #     connect_image_list_A=cv2.vconcat(dir_add_list_A)
    #     connect_image_list_B=cv2.vconcat(dir_add_list_B)
        
        
    #     connect_image=Image.new('RGB',(connect_image_list_A.shape[1]*2,connect_image_list_A.shape[0]))
    #     connect_image.paste(connect_image_list_A,(0,0))
    #     connect_image.paste(connect_image_list_B,(connect_image_list_A.shape[1],0))
        
    #     image_name = graphs_dir_path + "/"+connect_target+"_結合図."+graph_foramat
        
    #     pil_img = Image.fromarray(cv2.cvtColor(connect_image, cv2.COLOR_BGR2RGB))
    #     pil_img.save(image_name)
        
    #     #cv2.imwrite(image_name,connect_image_list)
        
    #     print(connect_target_graphs)
