#!/use/bin/python3
import os
import base64

def Encode_Pic_base64(PATH, SaveName='test'):# defult put latter
    textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
    is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))
    if is_binary_string(open(PATH, 'rb').read(1024)) is False:
        return
    # judge file is binary file or not, from
    # https://stackoverflow.com/questions/898669/
    # how-can-i-detect-if-a-file-is-binary-non-text-in-python

    newFileName = SaveName + '.txt'
    ff = open(newFileName, 'a', encoding='utf-8')
    # append mode to open file.
    # see more in https://www.w3schools.com/python/ref_func_open.asp

    f = open (PATH, 'rb')
    # rb means open with binary mode open file.
    # more in https://www.tutorialsteacher.com/python/python-read-write-file
    # https://stackoverflow.com/questions/42339876/
    # error-unicodedecodeerror-utf-8-codec-cant-decode-byte-0xff-in-position-0-in

    StrFormat = str(base64.b64encode(f.read()),'utf-8') 
    # rm prefix b'', see in
    # https://blog.csdn.net/qq_42731401/article/details/105039539
    # or you will see:
    # https://stackoverflow.com/questions/58323382/
    # binascii-error-invaild-base64-encoded-string-number-of-data-characters1957-c
    print(StrFormat, file=ff)
    # output to file using print with `file`

if __name__ =='__main__':
    DIR = os.getcwd()
    DirList = []
    FileNameList = []
    step=0

    for root, dirs, files in os.walk(DIR):
        for file in files:
            DirList.append(os.path.join(root,file))

            nowFileName = os.path.splitext(file)
            FileNameList.append(nowFileName[0]) 
            # get file without suffix name,
            # and nowFilename[1] means suffix name, see in 
            # https://www.geeksforgeeks.org/python-os-path-splitext-method/

    for i in range(len(DirList)):
        Encode_Pic_base64(DirList[i], FileNameList[i])
        step += 1


# I forgot to edit the suffix of file, then the raw is bigger, from 3M to 4M.
# Funnily, I runned again and again, untill the Vmmem is costed 5G RAM and file
# size bacame to 1GB, Ahhhh... Its still have thumbnail and I trust they could
# also open. Yet Honeyview can not open it. Ahhhh... like this:
# b'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'