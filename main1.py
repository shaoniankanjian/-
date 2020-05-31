#coding:utf-8
import function1 as fc1
import os
import time
import pandas as pd
import json
import pickle

q = fc1.get_q()  # 获取问题集

def run(d,method=fc1.jaccard_similarity,near=True):
    detail = fc1.get_d(d)

    list1 = []
    list2 = []
    error = []
    for i, j in detail.items():
        list1.append(fc1.count2(q[i], j, near=True, m=method) + [i])

        for k in q:
            if i + '-' in k:
                # list2.append(fc.count2(q[k],j,near=True,m=fc.edit_distance)+[k])
                list2.append(fc1.count2(q[k], j, near=True) + [k])

    dict1 = {}
    for i in list1:
        dict1[i[-1]] = i[:-1]

    for i in list2:
        print(i[-1])
        dict1[i[-1]] = i[:-1]

    # with open('1.pkl', 'wb') as f:
    #     pickle.dump(dict1, f)

    for i in dict1:
        dict1[i] = str(dict1[i])

    with open('./用于审核的json记录/展示数据.json', 'w') as f:
        f.write(json.dumps(dict1))

    dict2 = {}
    for i in list1:
        dict2[i[-1]] = [q[i[-1]],i[1],i[-2]]

    for i in list2:
        dict2[i[-1]] = [q[i[-1]], i[1], i[-2]]


    return dict2


if __name__ == '__main__':
    print(fc1.get_q())


