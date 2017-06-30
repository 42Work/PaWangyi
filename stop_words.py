import pickle

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


if __name__=="__main__":
    get_stopwords('./DEAL/ALL/store.txt','./static/stop_words.pkl','./DEAL/ALL/cut.txt')