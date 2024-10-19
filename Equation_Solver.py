import tkinter as tk
from sympy import symbols, Eq, solve

def equation_solver_window():
    third_window = tk.Toplevel()
    third_window.title('Equation_Solver')
    third_window.configure(bg = 'lightgrey')
    third_window.geometry('1000x500')

    x = symbols('x') #Symbolic the 'x' so sympy knows how to manipulate it

    def solve_eq():
        equation = display.get()
        try:
            if '=' in equation:
                left_side, right_side = equation.split('=')

                sympyequation = Eq(eval(left_side), eval(right_side))
                solution = solve(sympyequation, x)

                display.delete(0, tk.END)
                display.insert(tk.END, solution)

            else:
                display.delete(0, tk.END)
                display.insert(tk.END, 'Invalid Equation')

        except Exception as e:
            print('Error', e)
            display.delete(0, tk.END)
            display.insert(tk.END, 'Error')


    title = tk.Label(third_window, text='Equation Solver', width=75, height=3, font=('', 20))
    title.place(x=10, y=20)

    display = tk.Entry(third_window, width=39, font=('', 40), relief='solid', justify='left', bg='red')
    display.place(x=10, y=100, height=100)

    solve_equation = tk.Button(third_window, width=38, font=('', 40), text='Solve!', command = solve_eq)
    solve_equation.place(x=10, y=210)

    back = tk.Button(third_window, width = 38, font=('', 40), text = 'Back', command = third_window.destroy)
    back.place(x=10, y=280)



