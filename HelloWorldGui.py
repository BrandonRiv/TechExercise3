import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("Hello World Program")
window.geometry("800x600")

hello_message = tkinter.Message(window, text="Hello World!")
hello_message.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


def show(): 
    label.config( text = clicked.get() )


# Dropdown menu options 
options = [ 
    "Green", 
    "Blue", 
    "Red", 
    "Yellow", 
    "Purple", 
    "Pink", 
    "Orange"
] 
  
# datatype of menu text 
clicked = StringVar() 
  
# initial menu text 
clicked.set( "Choose color" ) 
  
# Create Dropdown menu 
drop = OptionMenu( window , clicked , *options ) 
drop.pack() 


# Create button, it will change label text 
button = Button( window , text = "Modify Color" , command = show ).pack() 

# Create Label 
label = Label( window , text = " ") 
label.pack() 

window.mainloop()


