import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import openai
import datetime
from config import apikey
import random


chatstr = ""


def chat(query):

    global chatstr
    openai.api_key = apikey
    chatstr += f"Abhishek: {query}\n Jarvis"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "write a letter to the boss"
            },
            {
                "role": "user",
                "content": ""
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        say(response["messages"][0]["content"])
        chatstr += f"{response['choices'][0]['text']}\n"
        return response["choices"][0]["text"]
        # if not os.path.exists("Openai"):
        #     os.mkdir("Openai")

        with open(f"Openai/prompt- {random.randint(1, 345678876)}", "w") as f:
            f.write(text)
    except KeyError:
        print("An error occurred while accessing the response data.")

def ai(prompt, chatStr=None):
    
    openai.api_key = os.getenv(apikey)
    text = f"OpenAI response for prompt: {prompt} \n*************************************\n\n"

    response = openai.ChatCompletion.create(
        
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "write a letter to the boss"
            },
            {
                "role": "user",
                "content": ""
            },
            {
                "role": "assistant",
                "content": "Subject: Resignation Letter\n\nDear [Boss's Name],\n\nI hope this email finds you well. I wanted to talk to you personally but due to unforeseen circumstances, I am unable to have a proper face-to-face conversation right now. Therefore, I am writing to inform you of my decision to resign from my position at [Company Name], effective [Last Working Day, typically two weeks from the date"
            }
        ],
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    try:
        print(response["messages"][0]["content"])
        text += response["messages"][0]["content"]
        if not os.path.exists("Openai"):
            os.mkdir("Openai")

        with open(f"Openai/prompt- {random.randint(1, 345678876)}", "w") as f:
            f.write(text)
    except KeyError:
        print("An error occurred while accessing the response data.")


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognising....")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry"


if __name__ == '__main__':
    print('PyCharm')
    say("Hello I am Hactiv Assistant")
    while True:
        print("Listening....")
        query = takeCommand()
        sites = [["youtube","https://youtube.com"],["google","https://google.com"],["wikipedia","https://wikipedia.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "open music" in query:
            musicPath = "D:\Songs and movies\Music\Genda Phool - Badshah.mp3"
            os.startfile(musicPath)

        elif "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time is {strfTime}")

        elif "Using openai".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatstr = ""

        else:
            print("Chatting....")
            chat(query)