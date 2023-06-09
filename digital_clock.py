from tkinter import Tk
from tkinter import Label
import time
import sys

root = Tk()
root.title("Clock")

def present_time_int():
    diplay_time = time.strftime("%H : %M : %S %p") #'%p' is for pm or am, '%i' is for indian format time, '%H' for international time format
    digi_clock.config(text=diplay_time)
    digi_clock.after(1000, present_time_int) 

def present_time_ind():
    diplay_time = time.strftime("%I : %M : %S %p") #'%p' is for pm or am, '%i' is for indian format time, '%H' for international time format
    digi_clock.config(text=diplay_time)
    digi_clock.after(1000, present_time_ind)
    

digi_clock = Label(root, font=("arail", 150), bg="blue", fg="white")



def main():
    x = int(input("Enter the 1 for Indian time format or 0 for international time format :- "))
    if x == 1:
        present_time_ind()
        digi_clock.pack()
        root.mainloop()
    elif x == 0:
        present_time_int()
        digi_clock.pack()
        root.mainloop()
        
main()





