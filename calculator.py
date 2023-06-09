import tkinter as tk
import numexpr as ne

calculation = ' '

def add_to_calculation(symbol):
    global calculation #calculation variable is declared as the global variable to use it further
    calculation += str(symbol) #here the operator is added to the calculation varaible by typecasting it into string datatype
    text_result.delete(1.0, "end") #the entered values in the text area will get deleted
    text_result.insert(1.0, calculation) #the entered values are the inserted the variable calculation
    


def evaluate_calculation():
    global calculation #calculation variable is declared as the global variable to use it further
    try: #try and except block is used inorder to avoid some mistaken calculation inputs like divide by 0
        result =str(eval(calculation)) 
        calculation = " "
        '''the eval function can also be used to evaluate the input of the expression in calculation varaible.
        since it has security issues it is not prescribed to used for those application which are to be used by different people.
        hence function which can used is numexpr.evaluate()'''
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
        
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ' '
    text_result.delete(1.0, "end")


root = tk.Tk()
root.geometry("300x275") #this is going to fix the screen size of the calculator window

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24)) #this will create the text field for the result to be displayed 
text_result.grid(columnspan=5) #this will create a grid of column spaning upto 5 grids

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=6, font=("Arial",15))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=6, font=("Arial",15))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=6, font=("Arial",15))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=6, font=("Arial",15))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=6, font=("Arial",15))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=6, font=("Arial",15))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=6, font=("Arial",15))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=6, font=("Arial",15))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=6, font=("Arial",15))
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=6, font=("Arial",15))
btn_0.grid(row=5, column=2)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=6, font=("Arial",15))
btn_plus.grid(row=2, column=4)

btn_subtract = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=6, font=("Arial",15))
btn_subtract.grid(row=3, column=4)

btn_multiply = tk.Button(root, text="X", command=lambda: add_to_calculation("*"), width=6, font=("Arial",15))
btn_multiply.grid(row=4, column=4)

btn_divide = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=6, font=("Arial",15))
btn_divide.grid(row=5, column=4)

btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=6, font=("Arial",15))
btn_open.grid(row=5, column=1)

btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=6, font=("Arial",15))
btn_close.grid(row=5, column=3)

btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=13, font=("Arial",15))
btn_equals.grid(row=6, column=1, columnspan=2)

btn_clear = tk.Button(root, text="C", command=clear_field, width=13, font=("Arial",15))
btn_clear.grid(row=6, column=3, columnspan=2)



root.mainloop() # this will run the main loop for the program