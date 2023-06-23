def classify(argmax):
    if argmax == 0:
        return "这张图片是--CW肺动脉反流且质量为A"
    elif argmax == 1:
        return "这张图片是--CW肺动脉反流且质量为B"
    elif argmax == 2:
        return "这张图片是--CW三尖瓣反流且质量为A"
    elif argmax == 3:
        return "这张图片是--CW三尖瓣反流且质量为B"
    elif argmax == 4:
        return "这张图片是--PW二尖瓣口"
    elif argmax == 5:
        return "这张图片是--PW肺动脉瓣口"
    elif argmax == 6:
        return "这张图片是--PW右室流出道"
    elif argmax == 7:
        return "这张图片是--PW主动脉瓣口"
    elif argmax == 8:
        return "这张图片是--PW左室流出道"
    elif argmax == 9:
        return "这张图片是--M三尖瓣环位移"
    elif argmax == 10:
        return "这张图片是--M左室长轴"
    elif argmax == 11:
        return "这张图片是--TDI二尖瓣侧壁"
    elif argmax == 12:
        return "这张图片是--TDI二尖瓣间隔"
    elif argmax == 13:
        return "这张图片是--TDI三尖瓣环"
    elif argmax == 14:
        return "这张图片是--2D大动脉短轴"
    elif argmax == 15:
        return "这张图片是--2D剑突下四腔心右"
    elif argmax == 16:
        return "这张图片是--2D四心腔右心"
    elif argmax == 17:
        return "这张图片是--2D四心腔左心"
    elif argmax == 18:
        return "这张图片是--2D下腔静脉长轴"
    elif argmax == 19:
        return "这张图片是--2D心尖两腔心"
    elif argmax == 20:
        return "这张图片是--2D心尖三腔心"
    elif argmax == 21:
        return "这张图片是--2D右室流入道"
    elif argmax == 22:
        return "这张图片是--2D左室短轴腱索"
    elif argmax == 23:
        return "这张图片是--2D左室短轴乳头肌"
    elif argmax == 24:
        return "这张图片是--2D左室短轴心尖"
    elif argmax == 25:
        return "这张图片是--2D左室长轴"
        
    return