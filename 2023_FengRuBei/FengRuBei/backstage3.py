from mmdet.apis import init_detector, inference_detector
import io
from PIL import Image
import mmcv
def get_pressure(get_image):
    config_file = 'faster_rcnn_r50_fpn_1x_coco.py'
    checkpoint_file = 'latest.pth'
    model = init_detector(config_file, checkpoint_file, device='cuda:0')

    # img = ('test.jpg')
    # 或者 img = mmcv.imread(img)，这样图片仅会被读一次
    # image = 'test.jpg'
    image = Image.open(io.BytesIO(get_image))
    image.save("test.jpg")
    image = 'test.jpg'
    result = inference_detector(model, image)

    # 将可视化结果保存为图片
    model.show_result(image, result, out_file='static/images/result.jpg')

    # 计算并返回压力差
    height = 0
    for index in range(len(result[0])):
        height += (result[0][index][3] - result[0][index][1])
    height /= len(result[0])
    height *= 0.0081
    pressure = 4 * height * height
    return "反流压力差为：" + str(int(pressure)) + "mmHg"    
   
    # 输出标注信息
    # print(result)
    # 在一个新的窗口中将结果可视化
    # show_result_pyplot(model, img, result)
