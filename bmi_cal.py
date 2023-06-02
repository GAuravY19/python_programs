def metric_bmi():   
    height = float(input("Enter Your height in meters :- "))
    weight = float(input("Enter Your wieght in kilogram(kg) :- "))

    bmi = weight / (height**2)
    
    if bmi <= 18.5:
        print('Your BMI is', bmi,'which means you are underweight.')

    elif bmi > 18.5 and bmi < 25:
        print('Your BMI is', bmi,'which means you are normal.')

    elif bmi > 25 and bmi < 30:
        print('your BMI is', bmi,'overweight.')

    elif bmi > 30:
        print('Your BMI is', bmi,'which means you are obese.')

    else:
        print('There is an error with your input')
        print('Please check you have entered whole numbers\n'
              'and decimals were asked.')
    
    

def imperial_bmi():
    height = float(input("Enter Your height in lbs :- "))
    weight = float(input("Enter Your wieght in inches :- "))

    bmi = (703*weight) / (height**2) 
    
    if bmi <= 18.5:
        print('Your BMI is', bmi,'which means you are underweight.')

    elif bmi > 18.5 and bmi < 25:
        print('Your BMI is', bmi,'which means you are normal.')

    elif bmi > 25 and bmi < 30:
        print('Your BMI is', bmi,'which means you are overweight')

    elif bmi > 30:
        print('Your BMI is', bmi,'which means you are obese.')

    else:
        print('There is an error with your input')
        print('Please check you have entered whole numbers\n'
              'and decimals were asked.')
        
        
if __name__ == '__main__':
    print("Welcome to the BMI Calculator")
    
    x = input("Do you want to calculate your BMI in metric or imperial_bmi :- ")
    if x == "metric":
        metric_bmi()
    elif x == "imperial":
        imperial_bmi()
    else:
        print("Invalid input...!!")



