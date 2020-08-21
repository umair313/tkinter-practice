# it's day one i am learning about tkinter to make some GUI application
# to start we have to import tkinter its built in python
# so you really dont need to install it
# lets import it we are goin to import every thing from tkinter

from tkinter import *


# now we have to create main window object to render
# our window and every thing to render on it
# Tk() is a class we are creating an object of class Tk and assign it to MainWindow

MainWindow = Tk()

# set title for window
MainWindow.title('MainWindow')


# display 'Hello world' on window
# for we need label Widget in tkinter every thing is just a widget
# so use Label() widget by passing MainWindow as
# first argument so in that way tkinter will know
# we want to render on main window
# then we need to pack it because tkinter
# don't know in main where to render it
# it will display text hello world
# tkinter is OOP os we can do it like this


HelloWorld = Label(MainWindow, text="Hello World").pack()
# we need

# lets add some color to hello world text
# we use fb='color name' and pass it as argument
# fg for fore ground (face color)
HelloWorld = Label(MainWindow, text="Hello World", fg='red').pack()

# lets add some background to hello world
# we use bg='color name' and pass it as arugemnt
# bg for background
HelloWorld = Label(MainWindow, text="Hello World", bg='black', fg='white').pack()


# let's add some padding to text
# before that we will add some space here
# if we dont use this space here you will notice that
# above line and below lines have same black background
# we need to see it clear
space = Label(MainWindow, text="               ").pack()
# we use padx and pady for this
# padx is for padding x-axis
# pady is for padding y-axis

HelloWorld = Label(MainWindow, text="Abdul Rehman", bg='black', fg='white', padx=10, pady=10).pack()
#add some space
space = Label(MainWindow, text="               ").pack()
# now take the whole row and fill it with color
# by passing fill='x' will will hold all the space in x-axis and filled with bg color
# it also hold whole when resizing
# also chamge the font size
HelloWorld = Label(MainWindow, text="resize wont affect on vertical", font='Cursive', bg='black', fg='white', padx=10, pady=10).pack(fill='x')

# lets see some Entry (Input Fields)
inputField = Entry(MainWindow).pack()


# loop to main window to render and keep track of every thing at every time
# its an event loop keeps cycling
MainWindow.mainloop()

