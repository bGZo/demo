# http://202.207.12.156:9012/context/2e329756827e42330f7897cc9499588e
import requests
import json
import time

def playThatPlace(baseUrl, x,y):
    response=requests.get(baseUrl+x+y)
    if response.status_code!='200':
        print(response.status_code)
    return response

if __name__=='__main__':
    loginInfo='user=0191121339&password=0x2eeb96e90ef7d8c0b0ba220c943c2cb2a9de0148962183ffd8451e6652515c5c39cdd986e69f57d5b4657af535b5d84de709dfbf9d6110de4ca8895773e90d87f5dcb66a03ad3aa653911b23869a0541fed2a7cad215ed960abeaef464e173652f0b7cdff504e3f30c0ef0b167aa5692633bef0a8f822c99e827f49417edfeaa'

    response=requests.get('http://202.207.12.156:9012/join_game?data_type=json&'+loginInfo)
    gameIdJson=json.loads(response.text)
    gameId=gameIdJson['game_id']
    print('Have get the ticket:{0}'.format(gameId))

    cheakBase='http://202.207.12.156:9012/check_game/'+str(gameId)
    playBase='http://202.207.12.156:9012/play_game/'+str(gameId) + '?' + loginInfo +'&coord='

    nowStatus=requests.get(cheakBase)
    nowOpponent=json.loads(nowStatus)['opponent']

    while nowOpponent is 'None':
        time.sleep(5)
        print('Founding Opponent....')

    playing = 1

    while playing==1:
        nowStatus=requests.get(cheakBase)
        nowJson=json.loads(nowStatus)

        if nowJson['winner'] != 'None':
            print('ohhhhhhhh!!! winner is {0}'.format(nowJson['winner']))
            break

        if nowJson['current_turn'] != 'creator':
            time.sleep(10)
            print('waiting opponent playing...')

        # put your code
