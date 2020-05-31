import grequests
import os
import time

base_dir = './test2'
files = os.listdir(base_dir)

req_list = []

now = time.time()
for file in files:
    dir = os.path.join(base_dir,file)
    req_list.append(grequests.post('http://127.0.0.1:10000',
                                   files=[('file',open(dir,'rb'))]))



res_list = grequests.map(req_list)    # 并行发送，等最后一个运行完后返回
print(res_list[0].text)  # 打印第一个请求的响应文本
print(time.time()-now)