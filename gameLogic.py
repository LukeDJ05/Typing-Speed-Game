from tkinter import Tk, Canvas, PhotoImage, Button, Label
import random
from tkinter.constants import W
import tkinter.font as tkFont
import time
import os


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


def initialiseGame():
    file = open("words.txt", "rt")
    dictionaryWords = file.read().split("\n")
    file.close()
    wordsAnswered = False
    score = 0
    possibilities = 0
    timeout = 60
    timeStart = time.time()

window.mainloop()




# while wordsAnswered is False and  time.time() < timeStart + timeout:
#     wordsTest = []
#     i = 0
#     str = " "
#     while i < 3:
#         wordsTest.append(dictionaryWords[random.randint(0, len(dictionaryWords))])
#         i+=1
#     print(str.join(wordsTest))
#     wordsAnswered = True
#     attempt = input()
#     attemptedAnswers = attempt.split()
#     j = 0
#     for j in range(3):
#         while True:
#             try:
#                 if attemptedAnswers[j] == wordsTest[j]:
#                     score+=1
#                     print(score)
#                 possibilities+=1
#                 break
#             except IndexError:
#                 print("Please attempt all 3 words")
#                 attempt = input()
#                 attemptedAnswers = attempt.split()
#                 continue
#         wordsAnswered = False
