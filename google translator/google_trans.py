from googletrans import Translator 
from lang_list import LANGUAGES as lang

def languages(dest):
    for i,k in lang.items():
        if dest == k:
            dest = i 

    return dest
    
def googleTrans():
    translater = Translator()
    word = translater.translate(text, dest)
    print(word.text)
    
    
print("Welcome to Personalised Google Translator.")
print("Here You can translate as many words without using Internet.")
text = input("Enter the text you want to translate :- ")
dest = input("Enter the language of translation :- ")


print(languages(dest))
googleTrans()


