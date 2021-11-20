import os, base64, fnmatch

def Decode_Pic_base64(PATH):
    f = open(PATH, 'r').read()
    # PATH file con not contained prefix b'', or youo will see
    # https://stackoverflow.com/questions/58323382/
    # binascii-error-invaild-base64-encoded-string-number-of-data-characters1957-c
    imgdata = base64.b64decode(f)
    return imgdata

def Get2Dir(DIR):
    DirList = []
    includes = ['*.py', '*.png']
    # block file
    # see https://www.coder.work/article/83598
    # https://www.osgeo.cn/post/635gg
    for root, dirs, files in os.walk(DIR):
        for file in files:
            flag = 1
            for pattern in includes:
                if fnmatch.fnmatch(file, pattern):
                    flag = 0
                    break
            if flag == 1:
                DirList.append(os.path.join(root,file))
    return DirList

def Get2DirName(DIR):
    DirListName = []
    includes = ['*.py', '*.png']
    # block file
    # see https://www.coder.work/article/83598
    # https://www.osgeo.cn/post/635gg
    for root, dirs, files in os.walk(DIR):
        for file in files:
            flag = 1
            for pattern in includes:
                if fnmatch.fnmatch(file, pattern):
                    flag = 0
                    break
            if flag == 1:
                nowFileName = os.path.splitext(file)
                DirListName.append(nowFileName[0])
                # nowFileName is a dict,use index to locate ahhhh....T_T
    return DirListName

if __name__ == '__main__':
    DIR = Get2Dir(os.getcwd())
    DIRNAME = Get2DirName(os.getcwd())

    for i in range(len(DIR)):
        imgdata = Decode_Pic_base64(DIR[i])
        NewName = str(DIRNAME[i]) + '.png'
        # see https://stackoverflow.com/questions/17203690/
        # typeerror-can-only-concatenate-tuple-not-str-to-tuple-error/17203756
        file = open(NewName, 'wb')
        # should use binary w/r, firstly used a report error.
        file.write(imgdata)
        file.closed