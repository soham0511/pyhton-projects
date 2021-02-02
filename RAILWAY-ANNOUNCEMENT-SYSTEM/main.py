import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text,filename):
    mytext=str(text)
    language='hi'
    myobj=gTTs(text=mytext,lang=language,slow=True)
    myobj.save(filename)

def mergeAudios(audios):
    combined=AudioSegment.empty()
    for audio in audios:
        combined=AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    audio=AudioSegment.from_mp3('railway.mp3')
    #Attention drawing Initial Line
    start=88000
    finish=90200
    audioProcessed=audio[start:finish]
    audioProcessed.export("1_hindi.mp3",format="mp3")
    #from city

    #generating "se chalkar"
    start=91000
    finish=92200
    audioProcessed=audio[start:finish]
    audioProcessed.export("3_hindi.mp3",format="mp3")

    #via city


    #generating "ke raste"
    start=94000
    finish=95000
    audioProcessed=audio[start:finish]
    audioProcessed.export("5_hindi.mp3",format="mp3")

    #to city

    #generating "ko jane walli ki sankhiya"
    start=96000
    finish=98900
    audioProcessed=audio[start:finish]
    audioProcessed.export("7_hindi.mp3",format="mp3")

    #generating train number and name
    
    #generating "kuch hi samai mein platform sankhya"
    start=105500
    finish=108200
    audioProcessed=audio[start:finish]
    audioProcessed.export("9_hindi.mp3",format="mp3")

    #generating platform number

    #generating "par a rahi hai"
    start=10900
    finish=112250
    audioProcessed=audio[start:finish]
    audioProcessed.export("11_hindi.mp3",format="mp3")


def generateAnnouncement(filename):
    df=pd.read_excel(filename)
    for index , item in df.iterrows():
        # 2 - Generate from-city
        textToSpeech(item['from'],'2_hindi.mp3')
        # 4 - Generate via-city
        textToSpeech(item['via'],'4_hindi.mp3')
        # 6 - Generate to-city
        textToSpeech(item['to'],'6_hindi.mp3')
        # 8 - Generate train no and name
        textToSpeech(item['train_no']+" "+item['train_name'],'8_hindi.mp3')
        # 10 - Generate platform number
        textToSpeech(item['platform'],'10_hindi.mp3')

        audios=[f"{i}_hindi.mp3" for i in range(1,12)]
        announcement=mergeAudios(audios)
        announcement.export(f'announcement_{index+1}.mp3',format="mp3")


if __name__=="__main__":
    print("Generating Skeleton")
    generateSkeleton()
    print("Now Gnerating Announcement")
    generateAnnouncement("announce_hindi.xlsx")