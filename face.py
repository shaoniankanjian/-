import cv2

from scipy import misc
import tensorflow as tf
import numpy as np
import sys
import os
import copy
import argparse
import facenet
import align.detect_face
import pickle
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

void = []

print('Creating networks and loading parameters')
with tf.Graph().as_default():
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=1.0)
    sess = tf.Session(config=tf.ConfigProto(gpu_options=None, log_device_placement=False))
    with sess.as_default():
        pnet, rnet, onet = align.detect_face.create_mtcnn(sess, None)

def face(image):
    # image = 'E:\\wenjuan\\find_face\\input\\110101004003-180622145208_pic-2.jpg'

    minsize = 12  # minimum size of face
    threshold = [0.5, 0.6, 0.7]  # three steps's threshold
    factor = 0.709  # scale factor



    try :
        img = misc.imread(os.path.expanduser(image), mode='RGB')
    except:
        print(image,'is wrong')

    bounding_boxes, _ = align.detect_face.detect_face(img, minsize, pnet, rnet, onet, threshold, factor)
    count = len(bounding_boxes)

    return count

if __name__ == '__main__':

    base_dir = 'E:\\河北data\\全部'

    dict1 = {}

    files = os.listdir(base_dir)

    long = len(files)
    count = 0

    for file in files:

        list1 = []

        all_dir = os.path.join(base_dir,file)

        files1 = os.listdir(all_dir)

        for file1 in files1:
            if 'pic-' in file1:
                list1.append(face(os.path.join(all_dir,file1)))

        dict1[file] = list1

        count += 1
        print('\r完成度 %d/%d' % (count, long), end='')

    with open('2.pkl','wb') as f:
        pickle.dump(dict1,f)