import os
import numpy as np

path = '/home/zyr/darknet/archive/labels'

with open('/home/zyr/darknet/archive/train.txt', 'w') as tr:
    for filename in os.listdir(path):
        with open(filename, 'a') as f:
            content = ''
            tr.write('/home/zyr/darknet/archive/train_dataset/train_images/' + filename[0:5] + '.jpg')
            tr.write('\n')