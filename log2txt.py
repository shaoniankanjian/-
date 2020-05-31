import json
import re
import os
import pickle

def get_time(now):  #计算时间
    global begin
    h = int(now[0:2]) - int(begin[0:2])
    m = int(now[3:5]) - int(begin[3:5])
    s = int(now[6:]) - int(begin[6:])
    return h*3600 + m*60 + s

def log2txt(data,log,cut,base_dir):


    data = eval(data['data'])

    f = open(log,encoding='utf-8')

    lines = f.readlines()
    flag = False
    question = []
    for line in lines:
        if 'rec-1' in line and 'start' in line:
            global begin
            begin = line[11:19]
            flag = True
        if flag:
            if 'question' in line:
                question.append(line)
    q_list = []
    for q in question:
        ss = re.findall(' ([0-9]{2}\-[0-9]{2}\-[0-9]{2}).*question:(.+?):',q)
        q_list.append(list(ss[0]))
    # ('20-22-55', 'A3', '您的户口是否在本市？') 第一个是结束时间
    # print(q_list)
    # print(get_time(q_list[0][0]))

    for d in data:
        d['ed'] = int(d['ed'])
        d['bg'] = int(d['bg'])
        for c in cut:
            reduce = c[1] - c[0]
            if d['ed'] >= c[0]:
                d['bg'] += reduce
                d['ed'] += reduce

    bg = 0
    long = len(data)
    index = 0

    list1 = [[] for _ in range(len(q_list))]

    for i in range(len(q_list)):
        ed = get_time(q_list[i][0])
        list1[i].append(q_list[i][1])
        # print(bg,int(data[index]['bg'])/1000)
        while (index <= long-1) and (int(data[index]['bg'])/1000 <= ed - 0.7 ):
            list1[i].append(data[index]['onebest'])
            index += 1
        bg = ed  #更新开始时间

    print(list1)
    f.close()
    # for i in range(len(list1)):
    #     list1[i] = str(list1[i])
    # print(list1)

    with open(os.path.join(base_dir,'compare.txt'),'w') as f:
        for i in list1:
            for j in range(len(i)):
                if j == 0:
                    f.write(' '*30)
                    f.write('*' * 30)
                    f.write(' ' * 5)
                f.write(i[j])
                f.write('\n')
            f.write('-'*100)
            f.write('\n')

    # with open('question_'+base_dir+'.pkl','wb') as f:
    #     pickle.dump(list1,f)
    return list1
