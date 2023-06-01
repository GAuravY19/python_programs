import requests
import win32com.client as wincom 
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')

def news_read(query, lang, country, api_key):
    speak = wincom.Dispatch("SAPI.SpVoice")
    
    news = requests.get(f"https://gnews.io/api/v4/top-headlines?q={query}&lang={lang}&country={country}&max=10&apikey={api_key}").json()
    
    first = news['articles']
    
    for i in range(10):
        text = f" Today's {i+1}th headline. :- {first[i]['title']}"
        print(text)
        speak.Speak(text)
        
        sec = first[i]['description']
        print(sec)
        speak.Speak(sec)
        
        lst = f"from {first[i]['source']['name']}"
        print(lst)
        speak.Speak(lst)
        
        if i == 9:
            speak.Speak("Thanks for using me. Have a good day.")
            break
        
        x = int(input("Enter 1 to continue hearing or 0 to discontine :- "))
        if x == 0:
            break
        


query = input("Enter the topic you would like to read :- ")
lang = input("Enter the language code :- ")
country = input("Enter the country code :- ")
news_read(query, lang, country, api_key)

