import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

MASTER = "Shuvam"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning"+ MASTER)
    elif hour>=12 and hour<18:
        speak("Good Afternoon"+ MASTER)
    else:
        speak("Good Evening"+ MASTER)
    
    #speak("I am VA. How may I help you?")
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            print(f"user said: {query}\n")
        except Exception as e:
            print("Say that gain please")    
            query=None
        return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gail.com','password')
    server.sendmail("xxx@gmail.com",to,content)
    server.close()
 
def main():
    
    speak("Initializing VA")
    wishMe()
    query = takeCommand()
    
    if 'wikipedia' in query.lower():
        speak('searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query,sentences=2)
        speak(results)
     
    elif 'open youtube' in query.lower():
        url = "youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' 
        webbrowser.get(chrome_path).open(url)
    
    elif 'open youtube' in query.lower():
        url = "google.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' 
        webbrowser.get(chrome_path).open(url)
    
    elif 'play music' in query.lower():
        songs_dir = "C:\\Users\\Shuvam\\Music"
        songs = os.listdir(songs_dir)
        os.startfile(os.path.join(songs_dir,songs[3]))
    
    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is  {strTime}")
        
    elif 'email to gokul' in query.lower():
        try:
            speak("what should I send")
            content = takeCommand()
            to = "gokul@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent successfully")
            
        except Exception as e:
            print(e)
        
main()










