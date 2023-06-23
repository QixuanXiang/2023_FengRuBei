def classify(argmax):
    if argmax == 0 :
        return "三尖瓣反流程度：轻度"
    elif argmax == 1 :
        return "三尖瓣反流程度：中度"
    elif argmax == 2 :
        return "三尖瓣反流程度：重度"