# url: http://202.207.12.156:9012/context/701672826a45d8d2d998b3a3f66166bf
import requests
import json
import re

def printBoard(board):
    ans=""
    for i in range(len(board)):
        for j in range(len(board[i])):
            # ans += board[i][j]
            print(board[i][j], end=' ')
        print('')
    return ans

def firstPrint(board, x, y):
    ans = ''
    moveList = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    for i in range(len(moveList)):
        if x+moveList[i] > 14:
            continue
        if x+moveList[i] < 0:
            continue
        ans+=board[x+moveList[i]][y]
    return ans
def secondPrint(board, x, y):
    ans = ''
    moveList = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    for i in range(len(moveList)):
        if x+moveList[i] > 14:
            continue
        if x+moveList[i] < 0:
            continue
        if y-moveList[i] > 14:
            continue
        if y-moveList[i] < 0:
            continue
        ans+=board[x+moveList[i]][y-moveList[i]]
    return ans
def thirdPrint(board, x, y):
    ans = ''
    moveList = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    for i in range(len(moveList)):
        if y+moveList[i] > 14:
            continue
        if y+moveList[i] < 0:
            continue
        ans+=board[x][y+moveList[i]]
    return ans
def fourthPrint(board, x, y):
    ans = ''
    moveList = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    for i in range(len(moveList)):
        if x-moveList[i] > 14:
            continue
        if x-moveList[i] < 0:
            continue
        if y-moveList[i] > 14:
            continue
        if y-moveList[i] < 0:
            continue
        # if x==1 and y==13:
            # print(x-moveList[i], end=' ')
            # print(y-moveList[i])
        ans+=board[x-moveList[i]][y-moveList[i]]
    return ans


def getStrScore(String): # 匹配两次??
    score=0
    if re.search(r'CMMMM', String) or re.search(r'MCMMM', String) or re.search(r'MMCMM', String)\
        or re.search(r'MMMCM', String) or re.search(r'MMMMC', String):
            score+=10000

    if re.search(r'COOOO', String) or re.search(r'OOOOC', String):
        score+=6000

    if re.search(r'\.CMMM\.', String) or re.search(r'\.MCMM\.', String) or re.search(r'\.MMCM\.', String)\
        or re.search(r'\.MMMC\.', String):
            score+=5000

    if re.search(r'COOO\.', String) or re.search(r'\.OOOC', String) or re.search(r'\.OOCO\.', String)\
        or re.search(r'\.OCOO\.', String):
            score+=5000

    if re.search(r'OCMMM\.', String) or re.search(r'OMCMM\.', String) or re.search(r'OMMCM\.', String)\
        or re.search(r'OMMMC\.', String) or re.search(r'\.CMMMO', String) or re.search(r'\.MCMMO', String)\
            or re.search(r'\.MMCMO', String) or re.search(r'\.MMMCO', String):
                score+=2000

    if re.search(r'\.MMC\.', String) or re.search(r'\.MCM\.', String) or re.search(r'\.CMM\.', String):
        score+=400

    if re.search(r'\.OOC', String) or re.search(r'COO\.', String) or re.search(r'MOOOC', String)\
        or re.search(r'COOOM', String):
            score+=400

    if re.search(r'\.MMCO', String) or re.search(r'\.MCMO', String) or re.search(r'\.CMMO', String) \
        or re.search(r'OMMC\.', String) or re.search(r'OMCM.', String) or re.search(r'OCMM\.', String)\
            or re.search(r'MOOC', String) or re.search(r'COOM', String):
                score+=200

    if re.search(r'\.MC\.', String) or re.search(r'\.CM\.', String):
        score+=50

    score+=20

    return score


if __name__=='__main__':

    _ans=''
    respond=requests.get('http://202.207.12.156:9012/step_08')
    data = (json.loads(respond.text))['questions']

    base='http://202.207.12.156:9012/step_08?questions={'+str(data) +'}'

    for i in range(len(data)):
    # for i in range(0,1):
        nowList = data[i]
        # print(nowList)
        nextBlackOrWhite = 0 if (len(nowList)//2)%2!=0 else 1
        # x+y must be even number
        # odd is block(1), next is white(0).
        # even is white(0), next is black(1).

        whiteLocations=[]
        blackLocations=[]

        for i in range(len(nowList)//2): # 偶数次循环
            xLocation = i*2
            yLocation = i*2+1
            if i%2 == 0:
                blackLocations.append((ord(nowList[xLocation])-ord('a'), \
                    ord(nowList[yLocation])-ord('a')))
            else:
                whiteLocations.append((ord(nowList[xLocation])-ord('a'), \
                    ord(nowList[yLocation])-ord('a')))
        # if blackOrWhite==1:
        #     i = len(nowList)//2
        #     xLocation = i*2
        #     yLocation = i*2+1
        #     blackLocations.append((ord(nowList[xLocation])-ord('a'), \
        #             ord(nowList[yLocation])-ord('a')))

        board = [['.' for i in range(15)] for j in range(15)]

        firstInit='M'
        secondInit='O'
        if nextBlackOrWhite == 0:
            firstInit='O'
            secondInit='M'
        for i in range(len(blackLocations)):
            board[blackLocations[i][0]] [blackLocations[i][1]]=firstInit
        for i in range(len(whiteLocations)):
            board[whiteLocations[i][0]] [whiteLocations[i][1]]=secondInit

        # print(len(nowList)//2)
        # print(nextBlackOrWhite)
        # printBoard(board)

        maxX, maxY, maxScore=0,0,0
        boardScore = [[0 for i in range(15)] for j in range(15)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    continue
                # nowBackup=board[i][j]
                board[i][j]='C'
                tempSco=0
                tempStr=firstPrint(board, i, j)
                tempSco+=getStrScore(tempStr)

                tempStr=secondPrint(board, i, j)
                tempSco+=getStrScore(tempStr)

                tempStr=thirdPrint(board, i, j)
                tempSco+=getStrScore(tempStr)
                
                tempStr=fourthPrint(board, i, j)
                tempSco+=getStrScore(tempStr)

                boardScore[i][j]=tempSco
                if tempSco>maxScore:
                    maxScore=tempSco
                    maxX=i
                    maxY=j
                # board[i][j]=nowBackup
                board[i][j]='.'

        if _ans!='':
            _ans+=','
        _ans+=chr(maxX+ord('a'))+chr(maxY+ord('a'))
        # _ans+=str(maxX)+','+str(maxY)

        # _ans+= (maxX+ord('a'))
        # print(maxX)
        # print(maxY)
        # print(maxScore)

        # board[7][5]='C'
        # print(thirdPrint(board, 7, 5))

        # printBoard(boardScore)

    # print(board[9][9])
    # print(_ans)
    _ans='&ans='+_ans
    respond=requests.get(base+_ans)
    print(base+_ans)
    print(respond.text)
