import pandas as pd
from sumy.parsers.plaintext import PlaintextParser #We're choosing a plaintext parser here, other parsers available for HTML etc.
from sumy.nlp.tokenizers import Tokenizer 
from sumy.summarizers.lsa import LsaSummarizer #We're choosing Luhn, other algorithms are also built in
from nltk.tokenize import RegexpTokenizer

#cache
import pickle
import os
import sys
import gensim
from gensim.models import Word2Vec


def getWords(pos,neg):
    try:
        res=model.most_similar(positive= [x.lower() for x in pos],negative= [x.lower() for x in neg], topn=3, restrict_vocab=None, indexer=None)
        res = [res[0][0],res[1][0],res[2][0]]
    except:
        res = ["error:"+ str(sys.exc_info()[1])]
    return res


def getSummary(keyword):
    keyword = keyword.lower()
    if keyword == None:
        return None
    val = checkCache(keyword)
    if val != None:
        return val
    key=df[df.Title.str.contains(keyword, regex= True, na=False,case=False)]
    # print(len(key))
    max_art = 350
    if len(key) > max_art:
        key = key[:max_art]
    key_Abs =  key[key.Abstract.str.contains(keyword, regex= True, na=False,case=False)]
    key_Abs =  key_Abs[['Title','Abstract']]
    Abstract = key_Abs['Abstract'].str.cat(sep=',')
    parser = PlaintextParser(Abstract, Tokenizer("english"))
    summarizer_lsa = LsaSummarizer()
    summary_2 =summarizer_lsa(parser.document,5) #Summarize the document with 5 sentences
    if summary_2 == ():
        return None
    summary = []
    for sentence in summary_2:
        summary.append(str(sentence))
    return summary


def getCache():
    files = os.listdir("./cache/")
    files.sort()
    for f in files:
        fdisc = open("./cache/"+f,'rb')
        data = pickle.load(fdisc)
        for k in data.keys():
            cache[k] = data[k]

def checkCache(word):
    retval = []
    if word in cache.keys():
        # print("hit")
        for s in cache[word]:
            retval.append(str(s))
        return retval
    else:
        return None


model = Word2Vec.load("word2vec_whoData_paper.model")
df = pd.read_csv('WHO_paper.csv')
cache = {}
getCache()