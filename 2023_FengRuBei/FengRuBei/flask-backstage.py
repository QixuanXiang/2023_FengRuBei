import torch.utils.data.distributed
from flask import Flask, request, render_template
from flask_cors import CORS
import backstage1
import backstage2
import backstage3

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
@torch.no_grad()
def predict():
    image = request.files["file"]
    img_bytes = image.read()
    info = backstage1.get_prediction(get_image=img_bytes)

    info_pre = [(info)]
    info_dic = {"result": info_pre}

    return info_dic

@app.route("/level", methods=["POST"])
@torch.no_grad()
def level():
    image = request.files["file"]  # 从前端读取图片
    img_bytes = image.read()  # 不用管
    info = backstage2.get_level(get_image=img_bytes)  # 调用后台二(backstage2),将图片传给后台二，经过处理后返回预测结果

    # 更改返回结果的格式，使之与up.html相匹配
    info_pre = [(info)]
    info_dic = {"result": info_pre}

    return info_dic  # 返回更改格式后的预测结果

@app.route("/pressure", methods=["POST"])
@torch.no_grad()
def pressure():
    image = request.files["file"]  # 从前端读取图片
    img_bytes = image.read()  # 不用管
    info = backstage3.get_pressure(get_image=img_bytes)  # 调用后台二(backstage2),将图片传给后台二，经过处理后返回预测结果

    # 更改返回结果的格式，使之与up.html相匹配
    info_pre = [(info)]
    info_dic = {"result": info_pre}

    return info_dic  # 返回更改格式后的预测结果



@app.route("/", methods=["GET", "POST"])
def root():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8097)

