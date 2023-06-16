from ast import FloorDiv 
from random import randint 
import copy 

print("welcome to the Mad Libs Game ")
playing = input('Lets play, shall we \n')

if playing.lower() != 'yes':
    quit()

print("Okay, Let's play the game. " )

noun1 = input("Enter your name :- ")
noun2 = input('Enter your friends name :- ')
noun3 = input('Enter your another friends name :- ')

place = input('Enter a place name :- ')

adjective1 = input('Enter an Adjective :- ')    
adjective2 = input('Enter another Adjective :- ')
adjective3 = input("Enter one more Adjective :- ")

adverb1 = input("Enter an Adverb :- ")
adverb2 = input("Enter another Adverb :- ")
adverb3 = input('Enter one more Adverb :- ')

exclamation = input('Enter an Emotion :- ')

print(
    f""" One day \t {noun1} went to a {place}. \n 
    He felt lonely, even though the view was {adjective1}. \n
    He decided to call his two best friends {noun2} and {noun3}. \n
    when they came they told {noun1} something {adjective2} \n 
    had happened {noun1} went there very {adverb1}. \n
    when he came he found out that his other Friend was falling off a cliff.\n  
    {noun3} managed to save him. \n
    {noun1} said {exclamation}. Inside he was feeling {adjective3}.\n 
    {noun1} managed to save him.\n 
    After that they had a {adverb2} celebration and they all laughed.
    """
)



