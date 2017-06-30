# -*- coding: utf-8 -*-

import jieba
import os
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
from os import path
from scipy.misc import imread
import pickle


#dir_path:要拼接的文件夹路径；
#拼接该文件夹下所有文件，输出到sumfile.txt；

def sum_file(dir_path):
    sum_file_path=dir_path+'/sumfile.txt'
    sf=open(sum_file_path,'w',encoding='utf-8')
    for filename in os.listdir(dir_path):
        if filename !='sumfile.txt':
            with open(os.path.join(dir_path,filename),'r',encoding='utf-8')as fl:
                sf.write(fl.read())
    sf.close()

#file_data:要分词的文件路径；
#cut_store:分词后的保存文件；

def cut_words(file_data,cut_store):
    cut_file=open(cut_store,'w',encoding='utf-8')
    with open(file_data,encoding='utf-8') as fd:
        for ln in fd:
            ct=' '.join(jieba.cut(ln))
            cut_file.write(ct)
    cut_file.close()

#删除停用词
#text_path:需要处理的文件路径
#words_path:停用词表路径
#cutstopfile:处理后保存的文件路径

def get_stopwords(text_path,words_path,cutstopfile):
    all_words=[]
    with open(words_path,'rb') as wp:
        data=pickle.load(wp)
    with open(text_path,'r',encoding='utf-8') as file:
        for ln in file:
            con=ln.split(' ')
            all_words+=con
    for stopword in data:
        for word in all_words:
            if word == stopword:
                all_words.remove(word)
    cutstopfile=open(cutstopfile,'w',encoding='utf-8')
    for x in all_words:
        cutstopfile.write(x)
        cutstopfile.write('\n')
    cutstopfile.close()

#file_path:需要词云化的文件完整路径；
#背景图片、输出的图片均放在./img下；
#bac_img:背景图片名；
#img_nama:输出文件名；

def creat_img(file_path,bac_img,img_name):
    d = path.dirname(__file__) + './img'
    bac = imread(path.join(d, bac_img))
    fdata = open(file_path, encoding='utf-8').read()
    wordcloud = WordCloud(font_path="ss.ttf", background_color="white", mask=bac, max_font_size=70).generate(fdata)
    image_color = ImageColorGenerator(bac)
    plt.imshow(wordcloud.recolor(color_func=image_color), interpolation='bilinear')
    plt.axis("off")
    wordcloud.to_file(path.join(d, img_name))


if __name__=="__main__":

    # sum_file('./DEAL/EXAMPLE/WM')
    # cut_words('./DEAL/EXAMPLE/WM/sumfile.txt','./DEAL/EXAMPLE/WM/store.txt')
    # get_stopwords('./DEAL/ALL/store.txt', './static/stop_words.pkl', './DEAL/ALL/cut.txt')


    ALL_PATH='./DEAL/ALL/store.txt'
    BAC_NAME_CHINA='china.png'
    ALL_IMGNAME='all.png'
    CHUNJIE_PATH='./DEAL/EXAMPLE/CJ/store.txt'
    CJ_IMGNAME='CJ.png'
    BAC_NAME_CJ='chunjie.png'
    WM_PATH='./DEAL/EXAMPLE/WM/store.txt'
    WM_IMGNAME='WM.png'
    BAC_NAME_WM='wang.png'

    creat_img(WM_PATH,BAC_NAME_WM,WM_IMGNAME)