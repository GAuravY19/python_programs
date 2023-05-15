#-------------------CODE LANGUAGE PROGRAM-------------------------
'''
--RULES FOR THE CODE LANGUAGE PROGRAM:-
-------------------CODING-------------------------------
1. If the word contains atleast 3 character, remove the 
first letter and append() it at the end.
2. Now append three random characters at the starting
and end 

------------------DECODING-----------------------------
1. If the word contains less than 3 characters, reverse it
2. Else remove the 3 random characters from start and end.
Now remove the last letter andappend it to the beginning.

NOTE:- YOUR PROGRAM SHOULD ASK WHETHER YOU WAN'T TO CODE
OR DECODE

'''


msg=input("Enter the characters :-")  #input the message to be coded or decoded
t=int(input("Enter 1 for coding and 0 for decoding :-"))
nxt=msg.split() # using split method to convert the str type to list type.

#CODING
if t==1:
    for j in nxt: #starting for the loop
        if len(j)<=3: #condition for checking the length of the word
            new=j[-1::-1] #reversing the  words
            print(new,end=" ") #printing the words the in the reverse direction
        else:
            new= "xmg" + j[-1::-1] + "ugn" #for the words the having more than 3 words
            #first it is reversed and then 3 words are added at the end and 3 words at the 
            # the end of the words 
            print(new,end=" ") #printing the final output
#DECODING
elif t==0:
    for k in nxt: #running a for loop in the message
        if len(k)<=3: # condition to be checked
            new=k[-1::-1] # printing the words with less than three 
            #words in reverse order
            print(new,end=" ")
        else:
            new=k[3:-3] #slicing the first and last three words of the  string having length 
            #greater than 3. 
            new_dug=new[-1::-1] #printing the remaining words in reverse in order
            print(new_dug,end=" " ) #printing the final words
else:
    print("not a valid input")
