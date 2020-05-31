from ffmpy import FFmpeg
from pydub import AudioSegment
from pydub.silence import detect_silence
import sys


def transform(filename,type='wav'):
    try :
        print('正在转换格式：aac->',type,'-----------')
        name = filename.split('.')[0]
        ff = FFmpeg(inputs={name+'.'+'aac': None}, outputs={name+'.'+type: None})
        ff.run()
        newfilename = name+'.'+type
        print('转换成功：',newfilename)
    except Exception as e:
        print(e)
        print('格式转换出错,可能文件已存在')
        # sys.exit()
        newfilename = name + '.' + type
    return newfilename

def silence_cut(filename):
    # 切分出名称和类型
    name = filename.split('.')[0]
    type = filename.split('.')[-1]
    sound = AudioSegment.from_file(filename, format=type)
    print('正在检测静默------------')
    # start_end = detect_silence(sound,500,-66,1)
    start_end = detect_silence(sound, 5000, -1000, 1)

    for i in start_end:
        if (i[1] - i[0]) > 1000:
            i[1] -= 200

    sound2 = sound[0:1]
    sound3 = sound[0:1]
    sum = 0
    bg = 0
    for i in start_end:
        sum += i[1] - i[0]
        sound2 += sound[bg:i[0]]
        sound3 += sound[i[0]:i[1]]
        bg = i[1]
    sound2 += sound[bg:]
    newfilename = name + '_1.' + type
    sound2.export(newfilename, format=type)
    print('已生成',newfilename)
    #返回，删除时间的列表，总删除时间ms，新生成文件名称
    return start_end, sum, newfilename