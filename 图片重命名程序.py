import os

from PIL import Image


def sect(data_path,save_path):

    dirs = os.listdir(data_path)
    # print(dirs)
    a = 0
    for dir_name in dirs:
        subject_dir_path = data_path+"/"+dir_name
        print(subject_dir_path)
        im1 = Image.open(subject_dir_path)
        im1 = im1.convert('RGB')
        im1.save(save_path + str(a) + ".jpg")
        a+=1

if __name__ == '__main__':
    data_path = "pictures_train/遵义会议/"
    save_path = 'pictures_train/Zunyi/'
    sect(data_path,save_path)