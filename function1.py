#coding:utf-8
import gensim
import jieba
import numpy as np
from scipy.linalg import norm
import distance
from sklearn.feature_extraction.text import CountVectorizer
import math
import pickle
import re
import zhon.hanzi
import jieba
from pypinyin import lazy_pinyin,  Style
import copy
import re
import gensim
import jieba
import numpy as np
from scipy.linalg import norm

model = 1

# model_file = 'E:\\word2vec\\news_12g_baidubaike_20g_novel_90g_embedding_64.bin'
# model = gensim.models.KeyedVectors.load_word2vec_format(model_file, binary=True)



def get_q():
    with open('question.pkl','rb') as f:
        return pickle.load(f)

def get_d(d):

    detail = {}

    for i in range(len(d)):
        if 'B' in d[i][0] or 'C' in d[i][0] or 'D' in d[i][0]:
            detail[d[i][0]] = d[i-1][-1] + ''.join(d[i][1:])

    return detail

def check(str):  # 字符串预处理，去掉数字及字母
    str1 = ''
    for i in str:
        if bool(re.search('[0-9A-Za-z]',i)) \
                or i in zhon.hanzi.punctuation \
                or re.search('[\s+\.\!\/_,$%^*(+\"\'=——！\-，。？、~@#￥%……&*（）]',i)\
                or re.search('[与和的吗呢恩嗯啊阿]',i):
            continue
        str1 += i
    return str1


def edit_distance(s1, s2):
    return 1 - distance.levenshtein(s1, s2)/len(s2)


def jaccard_similarity(s1, s2):
    def add_space(s):
        return ' '.join(list(s))

    # 将字中间加入空格
    s1, s2 = add_space(s1), add_space(s2)
    # 转化为TF矩阵
    cv = CountVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]
    vectors = cv.fit_transform(corpus).toarray()
    # 求交集
    numerator = np.sum(np.min(vectors, axis=0))
    # 求并集
    denominator = np.sum(np.max(vectors, axis=0))
    # 计算杰卡德系数
    return 1.0 * numerator / denominator

def edit_distance(s1, s2):
    return 1 - distance.levenshtein(s1, s2)/len(s2)

def vector_similarity(s1, s2):
    def sentence_vector(s):
        words = jieba.lcut(s, cut_all=True)
        add = 0
        v = np.zeros(64)
        for word in words:
            try:
                v += model[word]
            except:
                try:
                    v += model[word[0]] + model[word[1]]
                    add += 1
                except:
                    add -= 1

        v /= len(words) + add
        return v

    v1, v2 = sentence_vector(s1), sentence_vector(s2)
    return np.dot(v1, v2) / (norm(v1) * norm(v2))

# 0.68 , 0.67
def count(s1, sentence, per=1, d=1, m=jaccard_similarity,near=False):

    s1 = check(s1)
    sentence = check(sentence)
    if near:
        s1,sentence = nearby(s1,sentence)
        # print(1)

    n = math.floor(len(s1)*per)

    l = len(sentence) + d
    max = 0
    j = 0
    for i in range(0, l - n, d):
        s2 = sentence[i:i + n]
        dis = m(s1, s2)
        if dis > max:
            max = dis
            j = i
    return [round(max,2), sentence[j:j + n] ,s1]

def count2(s2, sentence2, per=1, d=1,add=1, m=jaccard_similarity,near=False):

    s1 = check(s2)
    sentence = check(sentence2)
    near = True
    if near:
        s1,sentence = nearby(s1,sentence)

    n = math.floor(len(s1)*per) + add

    l = len(sentence)
    max = 0
    j = 0
    for i in range(0, l - n, d):
        s2 = sentence[i:i + n]
        dis = m(s1, s2)
        if dis > max:
            max = dis
            j = i
    # print(sentence[j:j+n],max)
    ma = '[\s+\.\!\/_,$%^*(+\"\'=——！\-，。？、~@#￥%……&*（）0-9A-Za-z与和的吗呢恩嗯啊阿]*'.join(sentence[j:j+n])
    re_find = re.search(ma,sentence2)
    if re_find:
        bg = re_find.start()
        ed = re_find.end()
    else:
        bg=0
        ed=0
    # print(bg,ed)
    return [sentence2[:bg], sentence2[bg:ed] ,sentence2[ed:],round(max,2)]

def comp(w1,w2):  # 拼音比对函数

    if w1 == w2 or len(w1) != 2 or len(w2) != 2:
        return False
    count = 0
    a = lazy_pinyin(w1, style=3)
    b = lazy_pinyin(w1, style=5)
    c = lazy_pinyin(w2, style=3)
    d = lazy_pinyin(w2, style=5)
    try:
        for i in range(2):
            if a[i] == c[i]:
                count += 1
            if b[i] == d[i]:
                count += 1
    except:
        print(w1,w2,a,b,c,d)
    # return count
    if count >= 3:
        return True
    else:
        return False


def nearby(s1,s2):  # 需要copy一份

    s2 = list(s2)
    sc2 = copy.copy(s2)
    sc1 = []
    for i in range(len(s1)-1):
        sc1.append(s1[i:i+2])

    for i in jieba.cut(s1, cut_all=True):
        for j in range(len(s2) - 1):
            s = s2[j] + s2[j+1]
            try:
                sb = s2[j - 1] + s2[j]  # 前一个词
            except:
                sb = ''
            try:
                sa = s2[j + 1] + s2[j + 2]  # 后一个词
            except:
                sa = ''

            if comp(i, s) and s not in sc1 and sa not in sc1 and sb not in sc1:
                # print(i, s)
                sc2[j] = i[0]
                sc2[j+1] =i[1]

    return s1,''.join(sc2)

