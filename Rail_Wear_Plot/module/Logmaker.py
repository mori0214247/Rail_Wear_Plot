#解析対象リストをログとして書き出す
#あんまり用途が決まっていないが、後々必要になったらここで色々するかも

import os
import datetime as dtime

def log_maker(dir_path,serch_text,Logfilename,File_count):
    file_list_log = os.listdir(dir_path)
    dt_now = dtime.datetime.now()
    p_new=dir_path+"/"+Logfilename+(dt_now.strftime('%Y%m%d_%H%M%S'))+".log"
    with open(p_new,mode='w') as f_open_Log:
        f_open_Log.write(dt_now.strftime('%Y%m%d_%H%M%S')+"\n")
        l_in = [s for s in file_list_log if serch_text in s]
        f_open_Log.write(File_count+":"+str(len(l_in))+"\n")
        f_open_Log.write("\n".join(l_in))
    return(l_in)