import requests
import os
import re
import time

def filename_regularized(url):
    filename = url.split('/')[-1]
    if ".jpg" in filename:
        filename = filename[:filename.find(".jpg") + len(".jpg")]
    elif ".png" in filename:
        filename = filename[:filename.find(".png") + len(".png")]
    elif ".css" in filename:
        filename = filename[:filename.find(".css") + len(".css")]
    elif '.js' in filename:
        filename = filename[:filename.find(".js") + len(".js")]
    elif ".mp4" in filename:
        filename = filename[:filename.find(".mp4") + len(".mp4")]
    return filename


def Get_DownLoad_SZU():

    url = r'https://www.szu.edu.cn/'   
    # UsserAgent代表使用浏览器内核，在爬取数据时不断切换浏览器内核可起到一定的伪装作用
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    }

    reply = requests.get(url=url, headers=header)    
    reply.encoding = 'utf-8'  
    reply = reply.text   #获取网页文本信息 
    with open("SZUpage.html", 'w', encoding='utf-8') as f:
        f.write(reply)   
    
 
    filelist = re.findall('src="([^\"]*)"', reply)  
    list1 = re.findall('<link.*href="([^\"]*)"', reply)     
    list2 = re.findall('style="background-image:url\((.*)\);"', reply)     
    list3 = re.findall('style=" background-image:url\((.*)\);"', reply)     
    list4 = re.findall('style="background-image: url\((.*)\);"', reply)    
    #list5 = re.findall('<a.*href="([^\"]*)"', reply)
    filelist.extend(list1)
    filelist.extend(list2)
    filelist.extend(list3)
    filelist.extend(list4)     

    filelist = list(set(filelist))  
    filelist.remove("")    
    final_list = filelist.copy()   
    for i, src in enumerate(filelist):      
        if src[0] != '/':
            final_list[i] = '/'+src

    filep = []
    for file_url in final_list:
        file_divided = file_url.split('/')
        filep.append(file_divided[1])
    
    size = {}
    file_divided_new = []
    for file_url in filep:
        if file_url not in file_divided_new: 
            file_divided_new.append(file_url)
            size[file_url] = 0     
    
    for file_url in final_list:
        make_folder = []   #新建文件夹
        path = 'https://www.szu.edu.cn' + file_url   
        file_name = filename_regularized(file_url)   
        #构造初始文件相对路径
        file_path = '.'     
        for i, folder in enumerate(file_url.split('/')):
            if i != len(file_url.split('/'))-1 and i != 0:
                file_path = file_path + '/' + folder  
                make_folder.append(file_path)  
        for folder in make_folder:      
            if not os.path.exists(folder):
                os.mkdir(folder)
        if "mp4" not in file_name: 
            time.sleep(1)
            res = requests.get(url=path, headers=header).content
            with open(file_path+'/'+ file_name,'wb') as f:
                print(file_path+'/'+ file_name)
                f.write(res)
        else:   
            res = requests.get(url=path, headers=header, stream=True)
            chunk_size = 1024
            with open(file_path+'/'+ file_name, 'wb') as f:
                print(file_path+'/'+ file_name)
                for chunk in res.iter_content(chunk_size=chunk_size):
                    f.write(chunk)

    for f in size.keys():
        if len(f.split('.')) == 1:
            size[f] = calculate_total_size('./' + f)/1024
        else:
            size[f] = os.path.getsize("./" + f)/1024
    
    for f in size.items():
        print("The size of the folder/document " + f[0] + " is " + str(f[1]) + " KB")


def calculate_total_size(folder_path):
    total_size = 0
    for file_name in os.listdir(folder_path):
        path = os.path.join(folder_path, file_name)
        if os.path.isdir(path):  # 递归调用，计算子孙文件夹中所包含的文件总大小
            total_size = total_size + calculate_total_size(path)
        if os.path.isfile(path):  # 直接计算
            total_size = total_size + os.path.getsize(path)
    return total_size



def main():
    # Get_IP()
    Get_DownLoad_SZU()
    return


if __name__ == '__main__':
    main()
