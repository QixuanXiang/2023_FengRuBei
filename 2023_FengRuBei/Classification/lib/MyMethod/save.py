if output.argmax(1) == 0:
        print("这张图片是--CW肺动脉反流且质量为A")
    elif output.argmax(1) == 1:
        print("这张图片是--CW肺动脉反流且质量为B")
    elif output.argmax(1) == 2:
        print("这张图片是--CW三尖瓣反流且质量为A")
    elif output.argmax(1) == 3:
        print("这张图片是--CW三尖瓣反流且质量为B")
    elif output.argmax(1) == 4:
        print("这张图片是--PW二尖瓣口")
    elif output.argmax(1) == 5:
        print("这张图片是--PW肺动脉瓣口")
    elif output.argmax(1) == 6:
        print("这张图片是--PW右室流出道")
    elif output.argmax(1) == 7:
        print("这张图片是--PW主动脉瓣口")
    elif output.argmax(1) == 8:
        print("这张图片是--PW左室流出道")
    elif output.argmax(1) == 9:
        print("这张图片是--M三尖瓣环位移")
    elif output.argmax(1) == 10:
        print("这张图片是--M左室长轴")
    elif output.argmax(1) == 11:
        print("这张图片是--TDI二尖瓣侧壁")
    elif output.argmax(1) == 12:
        print("这张图片是--TDI二尖瓣间隔")
    elif output.argmax(1) == 13:
        print("这张图片是--TDI三尖瓣环")
    elif output.argmax(1) == 14:
        print("这张图片是--2D大动脉短轴")
    elif output.argmax(1) == 15:
        print("这张图片是--2D剑突下四腔心右")
    elif output.argmax(1) == 16:
        print("这张图片是--2D四心腔右心")
    elif output.argmax(1) == 17:
        print("这张图片是--2D四心腔左心")
    elif output.argmax(1) == 18:
        print("这张图片是--2D下腔静脉长轴")
    elif output.argmax(1) == 19:
        print("这张图片是--2D心尖两腔心")
    elif output.argmax(1) == 20:
        print("这张图片是--2D心尖三腔心")
    elif output.argmax(1) == 21:
        print("这张图片是--2D右室流入道")
    elif output.argmax(1) == 22:
        print("这张图片是--2D左室短轴腱索")
    elif output.argmax(1) == 23:
        print("这张图片是--2D左室短轴乳头肌")
    elif output.argmax(1) == 24:
        print("这张图片是--2D左室短轴心尖")
    elif output.argmax(1) == 25:
        print("这张图片是--2D左室长轴")