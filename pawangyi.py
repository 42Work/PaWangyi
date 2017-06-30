import requests
import bs4
from bs4 import BeautifulSoup as BP
import os
import time

def help():
    print('error~')
    exit(1)

def spider(url,rank_list_content):
    #time.sleep(3)
    r=requests.get(url,timeout=20)
    if r.status_code!=200:
        return 0
    else:
        print('访问成功！')
        soup=BP(r.text,"html.parser")
        rank_list=soup.table.contents
        for ln in rank_list:
            if isinstance(ln,bs4.element.Tag):
                if (ln.a):
                    rank_list_content.append(ln.a.string)


def create_text(conent_list,path):
    if not os.path.isfile(path):
        with open(path,'w',encoding='utf-8') as fl:
            for ln in conent_list:
                fl.write(ln)
                fl.write('\n')
        print('写入成功！')
    else:
        print('文件已存在！')
        help()


def spider_control(url_pre,year,month):
    if month<10:
        month=str(0)+str(month)
    date=str(year)+'-'+str(month)
    file_path='./DATA/'+date+'.txt'
    day=1
    rank_content_list=[]
    while int(day)<=31:
        if int(day)==24:
            day+=1
            continue
        if int(day)<10:
            day=str(0)+str(day)
        url=url_pre+date+'/'+str(day)+'/12.html'
        spider(url,rank_content_list)
        print('爬取'+str(day)+'天')
        if int(day)<10:
            day=int(day[-1])+1
        else:
            day+=1
    create_text(rank_content_list,file_path)


if __name__=="__main__":
    url_pre="http://post2.news.163.com/wgethtml/http+!!news.163.com!special!0001386F!index_rank.html!/"

    # for x in [2015,2016]:
    #     for y in range(1,13):
    #         spider_control(url_pre,x,y)
    #         time.sleep(60)


