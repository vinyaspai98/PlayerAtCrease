from pycricbuzz import Cricbuzz
import time
##Twilio setup
from twilio.rest import Client
account_sid = "AC8e8f915bf6d60208493114d1df182228"
auth_token  = "a056fc42ee363bb1c1803bc4d8159efa"
client = Client(account_sid, auth_token)


AllPlayers=[]
for i in range(2):
    player=input("Enter player name:")
    AllPlayers.append(player)

while len(AllPlayers)>0:
    c = Cricbuzz()
    matches=c.matches()
    for match in matches:
        messageBody = ""
        found=False
        #print(match)
        score=c.livescore(match['id'])
        #print(score)
        # checking for batsman

        if 'batting' in score:
            batting=score['batting']
            # print(batting['team'] + " : " + batting['score'][0]['runs'] + "/" + batting['score'][0][
            #     'wickets'] + " in " + batting['score'][0]['overs'] + " overs\n")
            messageBody = messageBody + batting['team'] + " : " + batting['score'][0]['runs'] + "/" + \
                          batting['score'][0]['wickets'] + " in " + batting['score'][0]['overs'] + " overs\n"
            if 'batsman' in batting:
                batsmen=batting['batsman']
                #print(batting['batsman'])
                for batsman in batsmen:
                    print("bat   "+batsman['name'])

                    if batsman['name'] in AllPlayers:
                        AllPlayers.remove(batsman['name'])
                        found=True
                        messageBody = messageBody + batsman['name'] + " is batting!!\n"

        # checking for bowler
        if 'bowling' in score:
            bowling=score['bowling']
            if 'bowler' in bowling:
                bowlers=bowling['bowler']
                #print(bowling['bowler'])
                for bowler in bowlers:
                    print("bowl   "+bowler['name'])
                    if bowler['name'] in AllPlayers:
                        AllPlayers.remove(bowler['name'])
                        found=True
                        messageBody = messageBody + bowler['name'] + " is bowling!!\n"

        if found:
            print(messageBody)
            message = client.messages.create(
                to="+917338324602",
                from_="+12077460733",
                body=messageBody)
            print(message.sid)
        else:
            print("Not found")

    time.sleep(60)
    currentTime = time.localtime()
    print("_________________"+str(time.strftime("%H:%M:%S", currentTime))+"________________")

