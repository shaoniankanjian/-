# coding:utf-8
from werkzeug.utils import secure_filename
from flask import Flask,render_template,jsonify,request,send_from_directory,make_response
import time
import os
import base64
import json
import numpy
from flask_script import Manager

import pandas as pd
import zipfile
import os
import numpy as np
import time

import main
import main1
import face

#标准开头
app = Flask(__name__)
manager = Manager(app)
#配置文件
UPLOAD_FOLDER='upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JSON_AS_ASCII'] = False
app.config.update(DEBUG=True)


basedir = os.path.abspath(os.path.dirname(__file__))    #获得绝对地址
ALLOWED_EXTENSIONS = set(['zip','rar'])

# 用于判断文件后缀
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

# 收到get请求，返回json文件
@app.route('/',methods=['GET'],strict_slashes=False)
def get_json():
    return jsonify({"error": 'you should use post not get'})


# 收到post请求，上传文件到本地
@app.route('/',methods=['POST'],strict_slashes=False)
def api_upload():
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    try:
        f = request.files['file']  # 从表单的file字段获取文件，file为该表单的name值
    except:
        return jsonify({"error": 'you should post a file,the key named file'})

    if f and allowed_file(f.filename):  # 判断是否是允许上传的文件类型

        azip = zipfile.ZipFile(f)
        fname = secure_filename(f.filename)
        fname = fname.split('.')[0]  # 调查问卷名称
        for file in azip.namelist():
            azip.extract(file,r'./data/' + fname)
        azip.close()

    a = face.face('data\\'+fname+'\\'+'pic-0.jpg')
    print(a)

    return jsonify({'人数':a})

@app.errorhandler(500)
def service_error(error):
    return make_response(jsonify({'error': 'service_error'}), 500)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=10000,threaded=True)

    # manager.run()  # 可以同时处理多个请求

    #  进入命令行文0 -p 10000 -d -r --thread    ,host='0.0.0.0',port='5000'件夹下输入   python3 app3.py runserver -h 0.0.0.