import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Arial"

#Create a new sub-window
def graph_window():
    second_window = tk.Toplevel()
    second_window.title('Graph')
    second_window.configure(bg = 'lightgrey')
    second_window.geometry('1000x500')

    def plot_graph():
        formula = display.get()
        x = np.linspace(-10, 10, 400) #generate value between -10 and 10, 400 of them with equal space
        try:
            y = eval(formula.replace('x', 'x'))
            #plot the graph
            plt.figure(figsize = (8,6)) #new canvas with 8 and 6 inches
            plt.plot(x, y, label = 'y = ' + formula)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title(f"Graph of y = {formula}")
            plt.legend()
            plt.grid(True)
            plt.show()
        except Exception as e:
            print('Error', e)

    title = tk.Label(second_window, text='Graph', width=75, height=3, font=('', 20))
    title.place(x=10, y=20)

    display = tk.Entry(second_window, width=39, font=('', 40), relief='solid', justify='left', bg='red')
    display.place(x=10, y=100, height=100)

    plot_button = tk.Button(second_window, width=38, font = ('', 40), text='Plot Graph', command = plot_graph)
    plot_button.place(x=10, y=210)

    back = tk.Button(second_window, width = 38, font = ('', 40), text = 'Back', command = second_window.destroy)
    back.place(x=10, y=280)










