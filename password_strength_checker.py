from password_strength import PasswordPolicy, PasswordStats
import time

def password_policy():
    policy = PasswordPolicy.from_names(
        length = 8, #min length of the password  
        uppercase = 2, #min UPPERCASE letter in the password
        numbers = 2, #,min NUMBERS in the password 
        special = 2,  #min SPECIAL CHARACTERS in the password
        nonletters = 2
    )
    
    if policy.test(password):
        return True 
    else:
        return False 
    

def password_test():
    password_strenght = PasswordStats(password)
    stats = password_strenght.strength()
    strength = stats*100
    if strength>30 and strength<=75:
        return f"Your `{password}` is moderately strong with strenght of {strength:.2f}%"
    elif strength>75 and strength<=90:
        return f"Your `{password}` is strong with strenght of {strength:.2f}%"
    elif strength>90:
        return f"Your `{password}` is very strong with strenght of {strength:.2f}%"
    else:
        return f"Your `{password}` is weak with strenght of {strength:.2f}%"


    
if __name__ =="__main__":
    print("Welcome to the Password Strenght Checker.")
    
    time.sleep(1)

    password = input("Enter your password :- ")
    if password_policy:
        print("Your Password passed the minimum requirements.")
    else:
        print("Your Password didn't passed the minimum requirements.")

    print(password_test())