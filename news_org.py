import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')


def news(query, API_Key):
    new = requests.get(f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&language=en&apiKey={API_Key}").json()
    
    for i in range(10):
        print(f"Page {i+1}")   
        print("source name : ",new.get('articles')[i].get('source').get('name'))
        print("author : ",new.get('articles')[i].get('author'))
        print("title : ",new.get('articles')[i].get('title'))
        print("description : ",new.get('articles')[i].get('description'))
        print("url : ",new.get('articles')[i].get('url'))
        print("publishdate : ",new.get('articles')[i].get('publishedate'))
        print("content : ",new.get('articles')[i].get('content'))
        
        print("-----------------------------------------------------")
        if i == 9:
            break
        x = int(input("Enter 1 to continue or 0 to discontinue : "))
        if x == 0:
            break 
          
        
             
    
query = input("Enter your query :- ")
news(query, api_key)

