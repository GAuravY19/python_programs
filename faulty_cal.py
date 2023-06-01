# PROBLEM STATEMENT 

'''Design a calculator which will correctly solve all the problems except the following ones :- 
1. 45 * 3 == 555,
2. 56 + 7 = 77,
3. 56/6 = 4

Your program should take operator and the two numbers as input from user and return the result.

'''

#SOLUTION

def matches(z,x,y):
    match z:
        case "+":
            print("result :- ",x+y)

        case "-":
            print("result :- ",x-y)
            
        case "/":
            print("result :- ",x/y)
            
        case "*":
            print("result :- ",x*y)
            

if __name__ == "__main__":
    x = int(input("Enter the first number :- "))
    y = int(input("Enter the second number :- "))
    z = input("Enter the operator to perform the information :-" )

    if (x == 45) and (y == 3) and (z == "*"):
        print("result :- 555")
    elif (x == 56) and (y == 7) and (z == "+"):
        print("result :- 77")
    elif (x == 56) and (y == 6) and (z == "/"):
        print("result :- 4")
    else:
        matches(z,x,y)