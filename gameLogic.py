from tkinter import *
import random
from tkinter.constants import W
import tkinter.font as tkFont
import time
import os

def initialiseGame():
    global wordsTest, entry1, textbox, timeStart
    file = open("words.txt", "rt")
    dictionaryWords = file.read().split("\n")
    file.close()
    wordsAnswered = False
    timeout = 60
    timeStart = time.time()

    while wordsAnswered is False and  time.time() < timeStart + timeout:
        window.update()
        wordsTest = []
        i = 0
        str = " "
        while i < 3:
            wordsTest.append(dictionaryWords[random.randint(0, len(dictionaryWords))])
            i+=1
        testWords = canvas.create_text(920, 360, text=str.join(wordsTest), fill='white',
                                anchor='center', font="Verdana, 50",
                                justify="center")
        wordsAnswered = True
        getText()
        canvas.delete(testWords)
        canvas.delete(textbox)
        canvas.update()
        wordsAnswered = False
    displayResults()
        

def getText():
    global entry1, wordsTest, score, possibilities, correctScore, possibleScore, textbox, timeStart, timeKeeping
    entry1 = Entry(window, justify="center", font="Ariel, 50") 
    textbox = canvas.create_window(920, 500, height=100, width=1500, window=entry1)
    entry1.focus_set()
    while True:
        attempt = entry1.get()
        window.update()
        canvas.itemconfig(timeKeeping, text=int(time.time() - timeStart))
        if attempt.count(' ') == 3:
            break
        else:
            continue
    attemptedAnswers = attempt.split()
    j = 0
    for j in range(3):
        while True:
            try:
                if attemptedAnswers[j] == wordsTest[j]:
                    score+=1
                    possibilities+=1
                    canvas.itemconfig(correctScore, text=int(score))
                    canvas.itemconfig(possibleScore, text=int(possibilities))
                    break
                else:
                    possibilities+=1
                    canvas.itemconfig(possibleScore, text=int(possibilities))
                    break
            except IndexError:
                attemptedAnswers.append("null")
                continue
 
def displayResults():
    global score, possibilities
    canvas.create_text(920, 515, text="You attempted " + str(possibilities) + " words\nYou correctly entered " + str(score), fill='white',
                              anchor='center', font="Verdana, 70",
                              justify="center")
    ######################################################################################################################################################### " words\n Your CPM is " + str("{:.2f}".format(score / 60))
    return


def setWindowDimensions(w, h):
    window = Tk()
    window.title("Typing Speed Game")
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    return window

# CANVAS DETAILS #
width = 1920
height = 1080
window = setWindowDimensions(width, height)
canvas = Canvas(window, width=width, height=height)
canvas.pack()
canvas.config(bg="black")
img = PhotoImage(file=os.getcwd()+ '\\typing.png').subsample(3)
img2 = canvas.create_image(1800, 110, image=img)
canvas.create_rectangle(10, 105, 140, 115,
    outline="white", fill="#FF5F1F")
canvas.create_text(920, 115, text="Typing Speed Game", fill='#FF5F1F',
                              anchor='center', font="Verdana, 120",
                              justify="center")



score = 0
possibilities = 0

correctScore = canvas.create_text(75, 65, text=score, fill='#32CD32',
                              anchor='center', font="Arial, 50",
                              justify="center")
possibleScore = canvas.create_text(75, 160, text=possibilities, fill='red',
                              anchor='center', font="Arial, 50",
                              justify="center")

timeKeeping = canvas.create_text(1810, 1000, text="0", fill='white',
                              anchor='center', font="Arial, 90",
                              justify="center")


initialiseGame()
window.mainloop()