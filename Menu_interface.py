import tkinter as tk
from Arithmetic_Operation import arithmetic_window
from Graph import graph_window
from Equation_Solver import equation_solver_window


#Create a window in tkinter
mainWindow = tk.Tk()
mainWindow.configure(bg = 'lightgrey')
mainWindow.title('Mathematical Scientific Calculator')


#Menu title
Title = tk.Label(mainWindow, text= 'Mathematical Scientific Calculator', width = 40, height = 6, font = ('', 30))
Title.grid(row = 0, column = 0, columnspan = 3, ipadx = 20)


#Setting up the buttons
Option1 = tk.Button(mainWindow, text = 'Arithmetic Operation', width = 20, height = 3, font = ('', 20), command = arithmetic_window)
Option1.grid(row= 1, column =0)
Option2 = tk.Button(mainWindow, text = 'Graph', width = 20, height = 3, font = ('', 20), command = graph_window)
Option2.grid(row= 1, column =1)
Option3 = tk.Button(mainWindow, text = 'Equation Solver', width = 20, height = 3, font = ('', 20), command = equation_solver_window)
Option3.grid(row= 1, column =2)

#Abandoned: Option4 = tk.Button(mainWindow, text = 'Calculus and Derivative Solver', width = 20, height = 3, font = ('', 20)) Option4.grid(row= 2, column =0) Option5 = tk.Button(mainWindow, text = 'Equation Storage', width = 20, height = 3, font = ('', 20)) Option5.grid(row= 2, column =1) Option6 = tk.Button(mainWindow, text = 'Table', width = 20, height = 3, font = ('', 20)) Option6.grid(row= 2, column =2)

#Main the grid expands as you resize the windows
mainWindow.grid_columnconfigure(0, weight = 1)
mainWindow.grid_columnconfigure(1, weight = 1)
mainWindow.grid_columnconfigure(2, weight = 1)
mainWindow.grid_rowconfigure(0, weight = 1)
mainWindow.grid_rowconfigure(1, weight = 1)
mainWindow.grid_rowconfigure(2, weight = 1)

#Run the window infinite times until user closes it
mainWindow.mainloop()

