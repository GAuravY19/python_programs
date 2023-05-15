#EMAIL VALIDATION PROGRAM......
#conditions to be checked in the email validation process:
'''
1. length of the email should be greater than or equal to 6
2. First letter of the email should not be any special character or any number
3. "@" should be used only once in the email
4. "." should at the 3rd or 4th position from the backside of the emial
5. There should not be any spaces in the email.
6. Special characters like "!", "#", "$", "%", "&", "~"

'''

#-----------------------program-----------------------------------------
email=input(" Enter your Email address :- ")

k=0

special_char="!,#,$,%,&,~"

#conditions.....
if len(email)>=6: #1
    if (email.islower()==True) or (email.isupper()==True) or (email.isdigit()==True): #2
        if ("@" in email) and (email.count("@")==1):#3
            if email[-3]=="." or email[-4]==".":#4
               if " " not in email:
                    for i in email:
                        if i not in special_char:
                            k+=1 
                    if k==len(email):
                        print("Correct email id") 
                    else:
                        print("Wrong Email id")      
               else:
                   print("Wrong Email id")
            else:
                print(" Wrong Email id ")
        else:
            print(" Wrong Email id")
    else:
        print(" Wrong Email id")
else:
    print(" Wrong Email id")


