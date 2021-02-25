from tkinter import *

root = Tk()
root.title('Simple Calculator')

e = Entry(root, width=35, borderwidth=5, fg="blue", bg="white")
e.grid(row=0, column=0, columnspan=3)

	
def clicked(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def clearbutton():
	e.delete(0, END)

def addbutton():
	first_number = e.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_number)
	e.delete(0, END)

def equalbutton():
	second_number = e.get()
	e.delete(0, END)

	if math == 'addition':
		e.insert(0, f_num + int(second_number))
	elif math == 'subtraction':
		e.insert(0, f_num - int(second_number))
	elif math == 'multiplication':
		e.insert(0, f_num * int(second_number))
	elif math == 'division':
		e.insert(0, f_num / int(second_number))

def subtractbutton():
	first_number = e.get()
	global f_num
	global math
	math = "subtraction"
	f_num = int(first_number)
	e.delete(0, END)

def multiplybutton():
	first_number = e.get()
	global f_num 
	global math
	math = "multiplication"
	f_num = int(first_number)
	e.delete(0, END)

def dividebutton():
	first_number = e.get()
	global f_num
	global math
	math = "division"
	f_num = int(first_number)
	e.delete(0, END)

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: clicked(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: clicked(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: clicked(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: clicked(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: clicked(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: clicked(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: clicked(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: clicked(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: clicked(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: clicked(0))
button_add = Button(root, text="+", padx=39, pady=20, command=addbutton)
button_equal = Button(root, text="=", padx=91, pady=20, command=equalbutton)
button_clear = Button(root, text="Clear!", padx=79, pady=20, command=clearbutton)

button_subtract = Button(root, text="-", padx=41, pady=20, command=subtractbutton)
button_multiply = Button(root, text="*", padx=40, pady=20, command=multiplybutton)
button_divide = Button(root, text="/", padx=41, pady=20, command=dividebutton)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)


root.mainloop()
