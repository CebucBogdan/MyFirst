from tkinter import *

window = Tk()
window.title('Calculator')

entry_box = Entry(window, width=30, borderwidth=10)
entry_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Define the operation
def button_introduce_num(num):
    current_value = entry_box.get()
    entry_box.delete(0, END)
    entry_box.insert(0, str(current_value) + str(num))


def button_clear_num():
    entry_box.delete(0, END)


def button_add_num():
    first_num = entry_box.get()
    global num_int
    global math_operator
    math_operator = 'add'
    num_int = int(first_num)
    entry_box.delete(0, END)


def button_substract_num():
    first_num = entry_box.get()
    global num_int
    global math_operator
    math_operator = 'substract'
    num_int = int(first_num)
    entry_box.delete(0, END)


def button_multiply_num():
    first_num = entry_box.get()
    global num_int
    global math_operator
    math_operator = 'multiplication'
    num_int = int(first_num)
    entry_box.delete(0, END)


def button_divide_num():
    first_num = entry_box.get()
    global num_int
    global math_operator
    math_operator = 'division'
    num_int = int(first_num)
    entry_box.delete(0, END)


def button_equal_num():
    second_num = entry_box.get()
    entry_box.delete(0, END)
    if math_operator == 'add':
        entry_box.insert(0, num_int + int(second_num))
    elif math_operator == 'substract':
        entry_box.insert(0, num_int - int(second_num))
    elif math_operator == 'division':
        entry_box.insert(0, num_int / int(second_num))
    elif math_operator == 'multiplication':
        entry_box.insert(0, num_int * int(second_num))


# Define button
button_1 = Button(window, text='1', padx=30, pady=15, command=lambda: button_introduce_num(1)).grid(row=3, column=0)
button_2 = Button(window, text='2', padx=30, pady=15, command=lambda: button_introduce_num(2)).grid(row=3, column=1)
button_3 = Button(window, text='3', padx=30, pady=15, command=lambda: button_introduce_num(3)).grid(row=3, column=2)
button_4 = Button(window, text='4', padx=30, pady=15, command=lambda: button_introduce_num(4)).grid(row=2, column=0)
button_5 = Button(window, text='5', padx=30, pady=15, command=lambda: button_introduce_num(5)).grid(row=2, column=1)
button_6 = Button(window, text='6', padx=30, pady=15, command=lambda: button_introduce_num(6)).grid(row=2, column=2)
button_7 = Button(window, text='7', padx=30, pady=15, command=lambda: button_introduce_num(7)).grid(row=1, column=0)
button_8 = Button(window, text='8', padx=30, pady=15, command=lambda: button_introduce_num(8)).grid(row=1, column=1)
button_9 = Button(window, text='9', padx=30, pady=15, command=lambda: button_introduce_num(9)).grid(row=1, column=2)
button_0 = Button(window, text='0', padx=30, pady=15, command=lambda: button_introduce_num(0)).grid(row=4, column=0)

button_add = Button(window, text='+', padx=29, pady=15, comman=lambda: button_add_num()).grid(row=4, column=1)
button_substract = Button(window, text='-', padx=30, pady=15, comman=lambda: button_substract_num()).grid(row=4,
                                                                                                          column=2)
button_multiply = Button(window, text='*', padx=31, pady=15, comman=lambda: button_multiply_num()).grid(row=5, column=1)
button_divide = Button(window, text='/', padx=31, pady=15, comman=lambda: button_divide_num()).grid(row=5, column=0)

button_equal = Button(window, text='=', padx=29, pady=15, comman=lambda: button_equal_num()).grid(row=5, column=2)
button_clear = Button(window, text='clear', padx=60, pady=20, comman=lambda: button_clear_num()).grid(row=6, column=0,
                                                                                                      columnspan=2)
window.mainloop()
