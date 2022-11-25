import os
from skimage import data,exposure,img_as_float
from PIL import Image,ImageFilter
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def sect(data_path,save_path):
    dirs = os.listdir(data_path)
    i = 49
    for dir_name in dirs:
        subject_dir_path = data_path+"/"+dir_name
        figure = Image.open(subject_dir_path)  # 读取图片
        image = img_as_float(figure)
        # figure_adjust_low = exposure.adjust_gamma(image, 7)  # 图片调暗
        figure_adjust_high = exposure.adjust_gamma(image, 0.7)  # 图片调亮
        # matplotlib.image.imsave(save_path + str(i) + "暗"+".jpg", figure_adjust_low)
        matplotlib.image.imsave(save_path + str(i) + "亮" + ".jpg", figure_adjust_high)
        i+=1

if __name__ == '__main__':
    data_path = "遵义会议/"
    save_path = 'E:/deep learn/6/'
    sect(data_path,save_path)