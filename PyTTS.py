#!/usr/bin/python

from gtts import gTTS
import os
from tkinter import *
import tkinter as tk
from tkinter import ttk, Label
from tkinter import scrolledtext


def make_ui():
    root = Tk()

    # This is the section of code which creates the main window
    root.geometry('450x250')
    root.configure(background='#F0F8FF')
    root.title('PyTSS')

    # This is the section of code which creates the a label
    Label(root, text='Welcome to PyTSS', bg='#F0F8FF',
          font=('arial', 19, 'normal')).place(x=10, y=10)

    # This is the section of code which creates the a label
    Label(root, text='Type here what you want to say', bg='#F0F8FF', font=(
        'arial', 12, 'normal')).place(x=10, y=50)

    # This is the section of code which creates a text input box
    # tInput = Entry(root)
    tInput = scrolledtext.ScrolledText(root,
                          wrap=tk.WORD,
                          width=40,
                          height=4,
                          font=("Times New Roman",
                                15))
    tInput.place(x=10, y=90)

    # This is the section of code which creates a button
    Button(root, text='Say', bg='#F0F8FF', font=('arial', 12, 'normal'),
           command=btnClickFunction).place(x=10, y=200)

    root.mainloop()


# this is a function to get the user input from the text input box
def getInputBoxValue():
    userInput = tInput.get()
    return userInput


# this is the function called when the button is clicked
def btnClickFunction():
    print('clicked')


def func(some_text="Here is some text default value!", file_name="tts_file.mp3"):
    language = "en"
    obj = gTTS(text=some_text, lang=language, slow=False)
    obj.save(file_name)
    os.system("mpg123 "+file_name)


if __name__ == "__main__":
    make_ui()
    func()
