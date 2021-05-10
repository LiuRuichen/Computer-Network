from lxml import etree
import requests
from urllib.request import urlopen

def Work_Download_PPT():
    url = r'https://sc.chinaz.com/ppt/free.html'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    }
    page_text = requests.get(url=url, headers=header).text
    etree_ppt = etree.HTML(page_text)
    # 每个ppt的url
    ppt_url = etree_ppt.xpath("//div[@class='bot-div']/a/@href")
    print(ppt_url)

    for each_url in ppt_url:
        # 每个ppt的完整下载url
        each_url = r'https://sc.chinaz.com' + each_url
       
        ppt_text = urlopen(each_url,timeout = 10).read().decode('utf-8')  
        '''
        time.sleep(1)
        ppt_page_text = requests.get(url=each_url, headers=header)
        ppt_page_text.encoding = "utf-8"
        ppt_text = ppt_page_text.text
        '''
        ppt_etree = etree.HTML(ppt_text)
        # 每个ppt的名字
        ppt_name = ppt_etree.xpath("//h1[@class='title']/text()")[0]
        print(ppt_name)
        # 每个ppt的下载链接
        ppt_download_url = ppt_etree.xpath("//div[@class='download-url']/a[1]/@href")[0]
        print(ppt_download_url)
        # 下载获取二进制数据
        ppt_data = requests.get(ppt_download_url, headers=header).content
        with open("ppt_container/" + ppt_name + '.rar', 'wb') as f:
            f.write(ppt_data)
    return

if __name__ == '__main__':
    Work_Download_PPT()