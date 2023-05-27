import time
import pyttsx3
from plyer import notification

def Notification(name):
    notification.notify(
        title = 'Drink Water Remainder',
        message = f'{name}, please drink water',
        timeout = 10
    )
    


def speak(name):
    engine = pyttsx3.init()
    engine.say(f"{name}, It's time to drink water")
    engine.runAndWait()
    



if __name__ == "__main__":
    name = input("Enter Your Name :- ")
    while True:
        speak(name)
        Notification(name)
        time.sleep(10)
