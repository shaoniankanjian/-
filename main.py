import os
import function
import sys
import video2json
import log2txt
import time

def run(base_dir):

    file = 'rec-1.aac'
    # base_dir = '1312'
    silence = False


    files = os.listdir(base_dir)
    for f in files:
        if f == file:
            filename = os.path.join(base_dir,f)
        elif 'log.txt' in f:
            log = os.path.join(base_dir,f)

    print(filename)
    new_filename1 = function.transform(filename)


    if silence:
        cut_list, sum, new_filename2 = function.silence_cut(new_filename1)
        print(sum)
    else:
        new_filename2 = new_filename1
        cut_list = []

    api = video2json.RequestApi(appid="5c7c913f", secret_key="720590985438df0c701b9ab4e3e0e124",
                                upload_file_path=new_filename2, base_dir=base_dir)
    result = api.all_api_request()

    return log2txt.log2txt(result,log,cut_list,base_dir)


if __name__ == '__main__':
    all = 0
    now = time.time()
    for i in os.listdir('data/'):
        run('data/' + i)
        all += 1
        print('已完成:',all)
        print('用时：',time.time()-now)
        now = time.time()


