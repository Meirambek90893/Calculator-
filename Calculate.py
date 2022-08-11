from multiprocessing.sharedctypes import Value
from tkinter import*
import tkinter 
from tkinter import messagebox
from unicodedata import name
from zipapp import ZipAppError

root = Tk()
root.title("Калькулятор ")
root.geometry('240x270')
root.resizable(width=False, height=False)


def degin_button(degit):
    return  Button(text=degit,bd=5,font=('Arial',13),command=lambda:add_degit(degit))
def operation_button(operation):
    return  Button(text=operation,bd=5,font=('Arial',13),fg="Red",command=lambda:add_operation(operation))
def calk_button(operation):
    return  Button(text=operation,bd=5,font=('Arial',13),fg="Red",command=addition)
def knopC(clear):
    
    return  Button(text=clear,bd=5,font=('Arial',13),fg = 'blue',command=add_clear)
def add_operation(operation):
    Value = numeral.get()
    if Value[-1] in '+-*/': # заменяет последную операцию на новую
        Value =Value[:-1]
    elif '+' in Value or '-' in Value or  '*' in Value or   '/' in Value:
        addition()
        Value = numeral.get()
    numeral.delete(0,tkinter.END)
    numeral.insert(0,Value+operation)

def add_clear():
    Value = numeral.get()
    numeral.delete(0,tkinter.END)
    numeral.insert(0,'0')

def add_degit(degit):
    Value = numeral.get()

    if Value[0] == '0'and len(Value)==1:
        Value =Value[1:]
    numeral.delete(0,tkinter.END)
    numeral.insert(0,Value+str(degit))

def addition():
    Value = numeral.get()
    if Value[-1] in '+-*/':
        Value = Value+Value[:-1]
    numeral.delete(0,tkinter.END)
    try: 
       numeral.insert(0,eval(Value))
    except(NameError,SyntaxError):
        messagebox.showinfo("ошибка отчета","недопустимы символ")
        numeral.insert(0,'0')
    except ZeroDivisionError:
        messagebox.showinfo("ошибка отчета","делит на 0 нельзя")
        numeral.insert(0,'0')     
def Key(event):
    if event.char.isdigit():
        add_degit(event.char)
    elif event.char in '-*/+': 
        add_operation(event.char)    
    # elif event.char in '=':
    #     addition()
    elif event.char == '\r':
        addition()

root.bind('<Key>',Key)

numeral = Entry(root,font=('Arial',15),width=15,justify=tkinter.RIGHT)
numeral.insert(0,'0')
numeral.grid(row=0,column=0,columnspan=4,stick="we")
degin_button("1").grid(row=1,column=0,stick = "wens",padx=5,pady=5)
degin_button("2").grid(row=1,column=1,stick = "wens",padx=5,pady=5)
degin_button("3").grid(row=1,column=2,stick = "wens",padx=5,pady=5)
degin_button("4").grid(row=2,column=0,stick = "wens",padx=5,pady=5)
degin_button("5").grid(row=2,column=1,stick = "wens",padx=5,pady=5)
degin_button("6").grid(row=2,column=2,stick = "wens",padx=5,pady=5)
degin_button("7").grid(row=3,column=0,stick = "wens",padx=5,pady=5)
degin_button("8").grid(row=3,column=1,stick = "wens",padx=5,pady=5)
degin_button("9").grid(row=3,column=2,stick = "wens",padx=5,pady=5)
degin_button("0").grid(row=4,column=0,stick = "wens",padx=5,pady=5)
operation_button("+").grid(row=1,column=3,stick = "wens",padx=5,pady=5)
operation_button("-").grid(row=2,column=3,stick = "wens",padx=5,pady=5)
operation_button("*").grid(row=3,column=3,stick = "wens",padx=5,pady=5)
operation_button("/").grid(row=4,column=3,stick = "wens",padx=5,pady=5)
calk_button("=").grid(row=4,column=2,stick = "wens",padx=5,pady=5)
knopC("C").grid(row=4,column= 1,stick = "wens",padx=5,pady=5)


root.grid_columnconfigure(0,minsize=60)
root.grid_columnconfigure(1,minsize=60)
root.grid_columnconfigure(3,minsize=60)
root.grid_columnconfigure(2,minsize=60)
root.grid_rowconfigure(1,minsize=60)
root.grid_rowconfigure(2,minsize=60)
root.grid_rowconfigure(3,minsize=60)
root.grid_rowconfigure(4,minsize=60)

root.mainloop()