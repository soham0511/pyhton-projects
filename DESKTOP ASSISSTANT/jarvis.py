import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyaudio
# import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello! I am Jarvis, your personalized AI assisstant. Please tell me what can I do for you.")
    speak("Hello! Mai Jarvis hoon, apka apna AI assisstant. Mai kaise apki sahayeta kar sakti hoon")
def takeCommand():
    #it takes input through microphone and returns as string
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please....")
        return "None"
    return query
# def sendEmail(to,content):
#     server=smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.login('my-email@gmail.com','my-password')
#     server.sendmail('youremail@gmail.com',to,content)
#     server.close()
def concern(query):
    if 'break up' in query:
        speak('''Don't worry there is always someone for you, out there.Seems that God did not want both of you to be together. Just get over her and start your work. Until you find someone you will always have be by your side''')
    elif 'angry' in query:
        speak('''Don't be angry at anyone, because by doing so you are only harming yourself and your capacity to think, it's always better to forgive them and move on...... Here I found some great articles so that you might understand the benefits of forgiving.''')
        webbrowser.open("https://sunshynegray.com/benefits-of-forgiveness/#:~:text=What%20are%20the%20benefits%20of%20forgiveness%3F%201%20Blessings.,Healing.%20...%207%20Living%20in%20the%20Present.%20")
    elif 'sad' in query:
        speak('''Don't be so silly to be sad. Just count on the good things of your life and move on.......Here are some movies that you can watch to smile again!''')
        webbrowser.open('https://collider.com/best-feel-good-movies/#:~:text=The%2025%20Best%20Feel-Good%20Movies%20to%20Watch%20When,%205%20School%20of%20Rock.%20%20More%20items')
    elif 'happy' in query:
        speak('''Ooh Great! I am glad to hear that. Well, now is not the time to sit back at home let's celebrate! Here are some of the nearest resturants near you.''')
        webbrowser.open('https://www.bing.com/maps?q=restaurants+near+me&cvid=07f6da05325d400291c383688013a911&aqs=edge.1.69i57j0l6.4271j0j1&pglt=931&FORM=ANNTA1&PC=W069')
    else: 
        speak('''Sorry but since I am a machine I am unable to understand your feelings right now. Humans are animals with complex emotions I think you should see a Therapist, who might help you.''')
if __name__=="__main__":

    speak("Srimany is a good boy")
    wishMe()
    while True:
        query=takeCommand().lower()
        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\soham\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open inkscape' in query:
            codepath="C:\\Program Files\\Inkscape\\bin\\inkscape.exe"
        elif 'I want to talk to you' in query:
            concern(query)
        # elif 'email to harry' in query:
        #     try:
        #         speak('What should I say?')
        #         content=takeCommand()
        #         to="sohamEmail@gmail.com"
        #         sendEmail(to,content)
        #         speak('Email has been sent!')
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry Boss! Unable to send this email at the moment")
        else:
            speak('Sorry Boss could not recognize your language, can you please repeat preferebly in english and a bit slowly.')