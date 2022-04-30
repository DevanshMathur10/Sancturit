from tkinter import *
import webbrowser
import random

def donate():
    url = ["https://allabouthappiness.in/Donate","https://www.nostoshomes.org/donate","https://goonj.org/donate/"]
    webbrowser.open(url[random.randint(0,len(url)-1)])