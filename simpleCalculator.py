#tutorial from John Elder
# Dec 14, 2021
from tkinter import *

#must use this code to run Tkinter widgets
root = Tk()
#title the application
root.title("Simple Calculator")

#provides a text input box
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=15, pady=15)

def button_equal():
    secomd_num = e.get()    #var for the second number entered
    e.delete(0,END)         #clears the textbox
    
    if math == "addition":
        e.insert(0, f_num + int(secomd_num)) 
    if math == "subtraction":
        e.insert(0, f_num - int(secomd_num))
    if math == "multiplication":
        e.insert(0, f_num * int(secomd_num))
    if math == "division":
        e.insert(0, f_num / int(secomd_num))  

def button_clear():
    #clears entry textbox
    e.delete(0, END)
    

def button_click(num):
    #get info from textbox
    current = e.get()
    #delete everyting in entry textbox
    e.delete(0, END)
    #insert the string version of user entry and number passed in
    e.insert(0, str(current) + str(num))
    

def button_add():
    first_num = e.get() #assign a variable to what is entered
    global f_num        #global variable for the first number
    global math
    math = "addition"
    f_num = int(first_num)  #assign the global to the entry variable
    e.delete(0,END)     #clear value from the textbox
    
def button_sub():
    first_num = e.get() #assign a variable to what is entered
    global f_num        #global variable for the first number
    global math
    math = "subtraction"
    f_num = int(first_num)  #assign the global to the entry variable
    e.delete(0,END)     #clear value from the textbox

def button_mult():
    first_num = e.get() #assign a variable to what is entered
    global f_num        #global variable for the first number
    global math
    math = "multiplication"
    f_num = int(first_num)  #assign the global to the entry variable
    e.delete(0,END)     #clear value from the textbox
    
def button_div():
    first_num = e.get() #assign a variable to what is entered
    global f_num        #global variable for the first number
    global math
    math = "division"
    f_num = int(first_num)  #assign the global to the entry variable
    e.delete(0,END)     #clear value from the textbox


#define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

#function buttons

button_equal = Button(root, text="=", padx=90, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=90, pady=20, command=button_clear)
button_sub = Button(root, text="-", padx=40, pady=20, command=button_sub)
button_mult = Button(root, text="*", padx=40, pady=20, command=button_mult)
button_div = Button(root, text="/", padx=40, pady=20, command=button_div)
button_add = Button(root, text="+", padx=40, pady=20, command=button_add)

#put the buttons on the screen
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=1, columnspan=2)
button_sub.grid(row=5, column=0)
button_mult.grid(row=6, column=0)
button_div.grid(row=6, column=1)
button_add.grid(row=6, column=2)





root.mainloop()
