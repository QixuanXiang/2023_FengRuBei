import torch
import sys, os

import torchvision.datasets as dset
import torchvision.transforms as transforms
import torch.utils.data as data
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import numpy as np
import json
import random
from tqdm import tqdm
import time

# modify
# CAT2IDX = {'CW_sanjianbanfanliu_A':0,'CW_sanjianbanfanliu_B':1}
CAT2IDX = {'CW_feidongmaiA':0,'CW_feidongmaiB':1,'CW_sanjianbanA':2,'CW_sanjianbanB':3,
           'PW_erjianbankou':4,'PW_feidongmaiban':5,'PW_youshiliuchu':6,'PW_zhudongmaiban':7,
           'PW_zuoshiliuchu':8,'M_sanjianban':9,'M_zuoshichangzhou':10,'TDI_erjianbancebi':11,
           'TDI_erjianbanjiange':12,'TDI_sanjianbanhuan':13,'2D_dadongmaiduanzhou':14,
           '2D_jiantusiyou':15,'2D_siqiangxinyou':16,'2D_siqiangxinzuo':17,'2D_xiaqiangjingmai':18,
           '2D_liangqiangxin':19,'2D_sanqiangxin':20,'2D_youshiliuru':21,'2D_zuoshiduanzhoujian':22,
           '2D_zuoshiduanzhouru':23,'2D_zuoshiduanzhouxin':24,'2D_zuoshichangzhou':25}

def image_loader(path,transform):
    try:
        image = Image.open(path)
    except FileNotFoundError: # weird issues with loading images on our servers
        # print('FILE NOT FOUND')
        time.sleep(10)
        image = Image.open(path)

    image = image.convert('RGB')

    if transform is not None:
        image = transform(image)

    return image

class heartTUDataset(data.Dataset):
    def __init__(self, split, num_labels, root, img_root, transform=None,  testing=False):
        self.root = root
        self.phase = split
        self.img_list = []
        self.get_anno()
        self.num_classes = num_labels
        self.img_root = img_root
        self.transform = transform
        self.testing = testing
        self.epoch = 1

    def get_anno(self):
        self.img_list = json.loads(open(os.path.join(self.root,'heartTU_annotation.json'), 'r').read())[self.phase]
        self.cat2idx = CAT2IDX

    def __len__(self):
        return len(self.img_list)

    def __getitem__(self, index):
        if torch.is_tensor(index):
            index = index.tolist()
        item = self.img_list[index]

        return self.get(item)

    def get(self, item):
        image_ID = item
        img_name = os.path.join(self.img_root, image_ID)
        image = image_loader(img_name, self.transform)

        # modify
        labels_index = self.cat2idx['_'.join(image_ID.split('_')[:2])]
        labels = np.zeros(self.num_classes, np.float32)
        labels[labels_index] = 1
#         return image,labels
        return image, labels


