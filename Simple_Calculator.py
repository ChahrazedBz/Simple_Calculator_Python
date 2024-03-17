from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(0, 0)
root.config(bg="Black")
e = Entry(root, bd="10", width="30", font="Arial 21", bg="Light Grey")
e.pack()


def click(number):
    e.insert(32, number)


def add():
    e.insert(32, "+")


def clear():
    e.delete(0, END)


def equal():
    current = e.get()
    numbers = [int(num) for num in current.split("+")]
    result = sum(numbers)
    clear()
    e.insert(0, result)


btn7 = Button(
    root,
    text="7",
    bd="10",
    font="Arial 19 bold",
    bg="Grey",
    padx="10",
    pady="5",
    command=lambda: click(7),
)
btn7.place(x="10", y="60")
btn8 = Button(
    root,
    text="8",
    bd="10",
    font="Arial 19 bold",
    bg="Grey",
    padx="10",
    pady="5",
    command=lambda: click(8),
)
btn8.place(x="85", y="60")
btn9 = Button(
    root,
    text="9",
    bd="10",
    font="Arial 19 bold",
    bg="Grey",
    padx="10",
    pady="5",
    command=lambda: click(9),
)
btn9.place(x="160", y="60")
btn4 = Button(
    root,
    text="4",
    bd="10",
    font="Arial 19 bold",
    bg="Grey",
    padx="10",
    pady="5",
    command=lambda: click(4),
)
btn4.place(x="10", y="145")
btn5 = Button(
    root,
    text="5",
    bd="10",
    font="Arial 19 bold",
    bg="Grey",
    padx="10",
    pady="5",
    command=lambda: click(5),
)
btn5.place(x="85", y="145")
btn6 = Button(
    root,
    text="6",
    bd="10",
    font="Arial 19 bold",
    bg="Grey",
    padx="10",
    pady="5",
    command=lambda: click(6),
)
btn6.place(x="160", y="145")
btn1 = Button(
    root,
    text="1",
    bd="10",
    font="Arial 19 bold",
    bg="Grey",
    padx="10",
    pady="5",
    command=lambda: click(1),
)
btn1.place(x="10", y="230")
btn2 = Button(
    root,
    text="2",
    bd="10",
    font="Arial 19 bold",
    bg="Grey",
    padx="10",
    pady="5",
    command=lambda: click(2),
)
btn2.place(x="85", y="230")
btn3 = Button(
    root,
    text="3",
    bd="10",
    font="Arial 19 bold",
    bg="Grey",
    padx="10",
    pady="5",
    command=lambda: click(3),
)
btn3.place(x="160", y="230")
btn0 = Button(
    root,
    text="0",
    bd="10",
    font="Arial 19 bold",
    bg="Grey",
    padx="10",
    pady="5",
    command=lambda: click(0),
)
btn0.place(x="10", y="315")

btnsum = Button(
    root,
    text="+",
    bd=10,
    height=5,
    font="Arial 19 bold",
    bg="Sky Blue",
    width=3,
    command=add,
)
btnsum.place(x="235", y="60")

btnequ = Button(
    root,
    text="=",
    bd=10,
    height=4,
    font="Arial 19 bold",
    bg="crimson",
    width=3,
    command=equal,
)
btnequ.place(x="235", y="240")


btnclr = Button(
    root,
    text="C",
    bd=10,
    width=8,
    pady="5",
    font="Arial 19 bold",
    bg="yellow",
    command=clear,
)
btnclr.place(x="85", y="315")


root.mainloop()
