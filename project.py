from tkinter import *
import functions as f

master = Tk()
master.title("Bioinformatics Toolkit")
master.geometry("500x400")
master.resizable(0, 0)

# define canvas for background image
canvas_1 = Canvas(master, width=1400, height=700)
canvas_1.pack()
# assign image
bg_1 = PhotoImage(file="python_bioinformatics.png")
# insert image
canvas_1.create_image(245, 140, image=bg_1)


# function for buttons with 2 or more functions
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


def desMaster():
    master.destroy()


# Start button
startButton = Button(master, text="START", command=combine_funcs(
    desMaster, f.create_dna), width=15, height=2, activebackground="#33B5E5")
startButton_window = canvas_1.create_window(
    190, 300, anchor='nw', window=startButton)


master.mainloop()
