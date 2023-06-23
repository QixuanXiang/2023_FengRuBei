import argparse
import os, sys
import random
import datetime
import time
from typing import List
import json
import numpy as np

import torch
import torch.nn as nn
import torch.nn.parallel
import torch.backends.cudnn as cudnn
import torch.distributed as dist
import torch.optim
import torch.utils.data
import torch.utils.data.distributed
import io
import _init_paths
from lib.dataset.get_dataset import get_datasets
import torchvision.transforms as transforms
from PIL import Image

import lib.models
import lib.models.aslloss
from lib.models.query2label import build_q2l
from lib.utils.misc import clean_state_dict
from lib.utils.slconfig import get_raw_dict
from lib.MyMethod.output1 import classify
import backstage2


def parser_args():
    parser = argparse.ArgumentParser(description='Query2Label for multilabel classification')

    args = parser.parse_args()

    with open('config1.json', 'r') as f:
        cfg_dict = json.load(f)
    for k, v in cfg_dict.items():
        setattr(args, k, v)

    return args


def get_args():
    args = parser_args()
    return args


def get_prediction(get_image):
    args = get_args()

    return main_worker(args, get_image)


def main_worker(args, get_image):
    # build model

    model = build_q2l(args)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    weights_path = "checkpoint/Q2L-SwinL-384/heart/26/model_best.pth.tar"
    if os.path.isfile(weights_path):
        checkpoint = torch.load(weights_path, map_location=device)
        state_dict = clean_state_dict(checkpoint)
        model.load_state_dict(state_dict, strict=True)
        del checkpoint
        del state_dict
        torch.cuda.empty_cache()

        # Data loading code
    image = Image.open(io.BytesIO(get_image))

    normTransform = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

    testTransform = transforms.Compose([transforms.Resize((448, 448)),
                                        transforms.CenterCrop(448),
                                        transforms.ToTensor(),
                                        normTransform])

    image = testTransform(image)
    image = torch.reshape(image, (1, 3, 448, 448))
    # for eval only
    model.eval()
    with torch.no_grad():
        output = model(image.to(device))
    result = classify(output.argmax(1))
    if output.argmax(1) == 2:
        if backstage2.get_level(get_image=get_image) == "三尖瓣反流程度：轻度":
            result = result + " 轻度反流"
        elif backstage2.get_level(get_image=get_image) == "三尖瓣反流程度：中度":
            result = result + " 中度反流"
        elif backstage2.get_level(get_image=get_image) == "三尖瓣反流程度：重度":
            result = result + " 重度反流"
    return result

# if __name__ == '__main__':
#    main()
