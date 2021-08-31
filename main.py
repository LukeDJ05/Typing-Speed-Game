from tkinter import Tk, Canvas, PhotoImage, Button, Label
import tkinter.font as tkFont
import time
import os

def welcome():
    global start_button, controls_button, results_button, main_msg, sub_msg
    textFont = tkFont.Font(family="Arial", size=100, weight="bold", slant="italic")
    main_msg = canvas1.create_text(960, 100, text='Typing Speed Test',
                                   fill='orange', anchor='center',
                                   font=textFont)

    start_button = Button(window1, text='Start', bg='grey', font='Arial, \
                          80', activebackground='orange', activeforeground='white')
    start_button.pack()
    start_button.place(x=800, y=850)

    canvas1.update()
    return

def setWindowDimensions(w, h):
    window1 = Tk()
    window1.title("Typing Speed Test")
    ws = window1.winfo_screenwidth()
    hs = window1.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window1.geometry('%dx%d+%d+%d' % (w, h, x, y))
    return window1


# CANVAS DETAILS #
width = 1920
height = 1080
window1 = setWindowDimensions(width, height)
canvas1 = Canvas(window1, width=width, height=height)
canvas1.pack()
canvas1.config(bg="black")

img = PhotoImage(file=os.getcwd()+ '\\typing.png')
canvas1.create_image(950, 500, image=img)


welcome()
window1.mainloop()

