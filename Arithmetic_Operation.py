import tkinter as tk
import math
from fractions import Fraction

last_answer = None

#Create a new sub-window
def arithmetic_window():
    global last_answer
    first_window = tk.Toplevel()
    first_window.title('Arithmetic Operation')
    first_window.configure(bg= 'lightgrey')
    first_window.geometry('1000x500')

    title = tk.Label(first_window, text = 'Arithmetic_Operation', width = 75, height = 3, font = ('',20))
    title.place(x = 10, y = 20)

    def button_click(value):
        current = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, current + str(value))

    def power():
        current = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, current + '^')

    def square_root():
        current = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, current + 'sqrt(')

    def euler():
        current = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, current + 'e')

    def pi():
        current = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, current + 'π')

    def log():
        current = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, current + 'log(')

    def natural_log():
        current = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, current + 'ln(')

    def trig_function(name):
        current = display.get()
        display.delete(0, tk.END)
        display.insert(tk.END, current + name + '(')

    def storage():
        global last_answer
        if last_answer is not None:
            current = display.get()
            display.delete(0, tk.END)
            display.insert(tk.END, current + str(last_answer))

    def convert():
        global last_answer
        try:
            if isinstance(last_answer, (int, float)) and last_answer is not None:
                fraction = Fraction(last_answer).limit_denominator()
                display.delete(0, tk.END)
                display.insert(tk.END, str(fraction))
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END,'Error')

    def clear():
        display.delete(0, tk.END)

    def delete():
        current = display.get()
        current = current[0:-1]
        display.delete(0, tk.END)
        display.insert(tk.END, current)

    def radians():
        global last_answer
        try:
            if isinstance(last_answer, (int, float)) and last_answer is not None:
                rad = last_answer * 3.1415926 / 180
                display.delete(0, tk.END)
                display.insert(tk.END, str(rad))
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, 'Error')

    def degree():
        global last_answer
        try:
            if isinstance(last_answer, (int, float)) and last_answer is not None:
                deg = last_answer * 180 / 3.1415926
                display.delete(0, tk.END)
                display.insert(tk.END, str(deg))
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, 'Error')

    def calculate():
        global last_answer
        try:
            expression = display.get()
            # Convert ^ to ** for the eval to understand power calculations
            expression = expression.replace("^", "**")
            expression = expression.replace('sqrt', 'math.sqrt')
            expression = expression.replace('e', '2.718281828459045')
            expression = expression.replace('π', '3.1415926')
            expression = expression.replace('log(', 'math.log')
            expression = expression.replace('ln(', 'math.log')
            expression = expression.replace('sin', 'math.sin')
            expression = expression.replace('cos', 'math.cos')
            expression = expression.replace('tan', 'math.tan')
            expression = expression.replace('arcsin', 'math.asin')
            expression = expression.replace('arccos', 'math.acos')
            expression = expression.replace('arctan', 'math.atan')
            # eval() will do the calculation
            result = eval(expression)
            last_answer = result
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception:
            display.delete(0, tk.END)
            display.insert(tk.END, 'Error')




    #Display Window (Relief creates a 3D boarder and Justify makes the input and output to the left
    display = tk.Entry(first_window, width = 25, font = ('', 40), relief = 'solid', justify = 'left', bg = 'red')
    display.place(x = 10, y = 100, height = 100)

    convert = tk.Button(first_window, text = 'Convert', font = ('', 20), command = convert)
    convert.place(x = 660, y = 110)
    clear = tk.Button(first_window, text='Clear', font=('', 20), command = clear)
    clear.place(x=780, y=110)
    delete = tk.Button(first_window, text='Delete', font=('', 20), command = delete)
    delete.place(x=880, y=110)
    radians = tk.Button(first_window, text='Radians', font=('', 20), command = radians)
    radians.place(x=660, y=160)
    degree = tk.Button(first_window, text='Degree', font=('', 20), command = degree)
    degree.place(x=780, y=160)
    back = tk.Button(first_window, text='Back', font=('', 20), command = first_window.destroy)
    back.place(x=900, y=160)

    # Button layout
    buttons_num = [
        '7', '8', '9', '^', 'sin', 'cos', 'tan', 'ans',
        '4', '5', '6', 'x', '/', 'arcsin', 'arccos','arctan',
        '1', '2', '3', '+', '-', 'a^b', 'sqrt', ')',
        '0', '.', '=', 'log', 'ln', 'e', 'π', '(',
    ]

    x = 10
    y = 210

    for index, button in enumerate(buttons_num):
        if button == '=':
            btn = tk.Button(first_window, text = button, font = ('', 14), command = calculate)
        elif button == 'a^b':
            btn = tk.Button(first_window, text = button, font = ('', 14), command = power)
        elif button == 'sqrt':
            btn = tk.Button(first_window, text = button, font = ('', 14), command = square_root)
        elif button == 'e':
            btn = tk.Button(first_window, text = button, font = ('', 14), command = euler)
        elif button == 'π':
            btn = tk.Button(first_window, text = button, font = ('', 14), command = pi)
        elif button == 'log':
            btn = tk.Button(first_window, text = button, font = ('', 14), command = log)
        elif button == 'ln':
            btn = tk.Button(first_window, text = button, font = ('', 14), command = natural_log)
        elif button in ['sin' or 'cos' or 'tan' or 'arcsin' or 'arccos' or 'arctan']:
            btn = tk.Button(first_window, text = button, font = ('', 14), command = lambda name = button: trig_function(name))
        elif button == 'ans':
            btn = tk.Button(first_window, text = button, font = ('', 14), command = storage)
        else:
            btn = tk.Button(first_window, text = button, font = ('', 14), command = lambda a = button: button_click(a))

        btn.place(x = x, y = y, width = 100, height = 50)

        x += 120

        #switching column
        if (index + 1) % 8 == 0:
            x = 10
            y += 70












