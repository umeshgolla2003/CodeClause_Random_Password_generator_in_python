from tkinter import *
from random import randrange

def rand():
    small = ['k', 'a', 'q', 'd', 'l', 'f', 'x', 'r', 'z', 'e', 'o', 'y', 'w', 's', 'b', 'h', 'c', 'v', 'n', 't', 'j',
             'g', 'p', 'i', 'm', 'u']
    capital = ['U', 'H', 'A', 'G', 'D', 'Y', 'R', 'I', 'P', 'B', 'X', 'W', 'S', 'J', 'Q', 'E', 'V', 'T', 'O', 'Z', 'K',
               'U', 'M', 'C', 'F', 'L', 'N']
    num = ['0', '3', '1', '6', '2', '9', '5', '8', '4', '7']
    special = ['@', '#', '&', '_', '%', '*']

    n = leng.get()
    password = ""
    password += capital[randrange(0, 25)]
    password += special[randrange(0, 5)]
    n = n - 2
    while (n):
        if (n % 2 == 0):
            password += small[randrange(0, 25)]
        else:
            password += num[randrange(0, 9)]
        n -= 1
    output.set(password)

root = Tk()
root.geometry("415x525")
root.title("Random Password Generator")
output = StringVar()



pass_head = Label(root, text='Length of Required Password', font='arial 12 bold').pack(
    pady=10)

leng = IntVar()
length = Spinbox(root, from_=4, to_=32, textvariable=leng, width=24, font='arial 16').pack()



Button(root, text="Generate", command=rand, font="Arial 10", bg='lightblue', fg='black', activebackground="teal",
       padx=5, pady=5).pack(pady=20)

pass_label = Label(root, text='Generated Password', font='arial 12 bold').pack(pady="30 10")
Entry(root, textvariable=output, width=24, font='arial 16').pack()

root.mainloop()