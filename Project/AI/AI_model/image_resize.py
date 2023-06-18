'''
입력크기에 맞는 이미지로 바꾸고 랜덤하게 이미지 순서를 섞는 코드
'''
import numpy as np
import cv2, os, random
from PIL import Image

new_path = './images/'

def Image_Resize_Fucntion(image_arr, path, original_path):
    for name in image_arr:
        img = Image.open('%s%s'%(original_path, name))
        img_array = np.array(img)
        img_size = img.size
        if img_size[0]*img_size[1] > 256*256:
            img_resize = cv2.resize(img_array, (256,256), interpolation = cv2.INTER_CUBIC)
        else:
            img_resize = cv2.resize(img_array, (256,256), interpolation = cv2.INTER_AREA)
        img = Image.fromarray(img_resize)
        try:
            img.save('%s%s'%(path,name))
        except:
            img = img.convert("RGB")
            img.save('%s%s'%(path,name))

### hair 이미지 분류
original_path = './datasets/tmp_images/hair2/'
img_list = os.listdir(original_path)
n = len(img_list)
random.shuffle(img_list)
print("hair의 총 이미지는 ",n,"장 입니다.")
num = int(0.7*n)
Image_Resize_Fucntion(img_list[:num], new_path+"train/hair/",original_path)
Image_Resize_Fucntion(img_list[num:], new_path+"test/hair/",original_path)

### hair_loss 이미지 분류
original_path = './datasets/tmp_images/hair_loss2/'
img_list = os.listdir(original_path)
n = len(img_list)
random.shuffle(img_list)
print("hair_loss의 총 이미지는 ",n,"장 입니다.")
num = int(0.7*n)

Image_Resize_Fucntion(img_list[:num], new_path+"train/hair_loss/",original_path)
Image_Resize_Fucntion(img_list[num:], new_path+"test/hair_loss/",original_path)