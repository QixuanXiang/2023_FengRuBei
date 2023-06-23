def classify(argmax):
    if argmax == 0:
        return "CW肺动脉反流影像 质量为A"
    elif argmax == 1:
        return "CW肺动脉反流影像 质量为B"
    elif argmax == 2:
        return "CW三尖瓣反流影像 质量为A"
    elif argmax == 3:
        return "CW三尖瓣反流影像 质量为B"
    elif argmax == 4:
        return "PW二尖瓣口影像"
    elif argmax == 5:
        return "PW肺动脉瓣口影像"
    elif argmax == 6:
        return "PW右室流出道影像"
    elif argmax == 7:
        return "PW主动脉瓣口影像"
    elif argmax == 8:
        return "PW左室流出道影像"
    elif argmax == 9:
        return "M三尖瓣环位移影像"
    elif argmax == 10:
        return "M左室长轴影像"
    elif argmax == 11:
        return "TDI二尖瓣侧壁影像"
    elif argmax == 12:
        return "TDI二尖瓣间隔影像"
    elif argmax == 13:
        return "TDI三尖瓣环影像"
    elif argmax == 14:
        return "2D大动脉短轴影像"
    elif argmax == 15:
        return "2D剑突下四腔心右影像"
    elif argmax == 16:
        return "2D四心腔右心影像"
    elif argmax == 17:
        return "2D四心腔左心影像"
    elif argmax == 18:
        return "2D下腔静脉长轴影像"
    elif argmax == 19:
        return "2D心尖两腔心影像"
    elif argmax == 20:
        return "2D心尖三腔心影像"
    elif argmax == 21:
        return "2D右室流入道影像"
    elif argmax == 22:
        return "2D左室短轴腱索影像"
    elif argmax == 23:
        return "2D左室短轴乳头肌影像"
    elif argmax == 24:
        return "2D左室短轴心尖影像"
    elif argmax == 25:
        return "2D左室长轴影像"
        
    return