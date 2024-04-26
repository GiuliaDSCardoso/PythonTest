from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Calculadora")

# Funções
def clickpoint():
    visor.insert(END, ".")

def clickmult():
    firstnum = visor.get()
    global p_num
    global math
    math = "multiplicacao"
    p_num = float(firstnum)
    visor.delete(0, END)

def clickdiv():
    firstnum = visor.get()
    global p_num
    global math
    math = "divisao"
    p_num = float(firstnum)
    visor.delete(0, END)

def clicksub():
    firstnum = visor.get()
    global p_num
    global math
    math = "subtracao"
    p_num = float(firstnum)
    visor.delete(0, END)

def clicksum():
    firstnum = visor.get()
    global p_num
    global math
    math = "soma"
    p_num = float(firstnum)
    visor.delete(0, END)

def clickequal():
    secondnum = visor.get()
    visor.delete(0, END)
    if math == 'soma':
        visor.insert(0, p_num + float(secondnum))
    if math == 'subtracao':
        visor.insert(0, p_num - float(secondnum))
    if math == 'multiplicacao':
        visor.insert(0, p_num * float(secondnum))
    if math == 'divisao':
        visor.insert(0, p_num / float(secondnum))

def deletar():
    visor.delete(0, END)

def clickbutton(num):
    atual = visor.get()
    visor.delete(0, END)
    visor.insert(END, str(atual) + str(num))

lb1 = Label(root, text="Calculadora", font=("verdana", 20, "bold"), pady=10)
lb1.pack()
visor = Entry(root, bg="#E6E6FA")
visor.pack()

# Fileira 1
bt1 = Button(root, text="1", bg="#C6C6F7", fg="black", pady=14, padx=14, bd=4,relief="ridge", command=lambda: clickbutton(1))
bt1.place(x=10, y=100)

bt2 = Button(root, text="2", bg="#C6C6F7", fg="black", pady=14, padx=14, bd=4,relief="ridge", command=lambda: clickbutton(2))
bt2.place(x=60, y=100)

bt3 = Button(root, text="3", bg="#C6C6F7", fg="black", pady=14, padx=14, bd=4,relief="ridge", command=lambda: clickbutton(3))
bt3.place(x=110, y=100)

bt0 = Button(root, text="0", bg="#C6C6F7", fg="black", pady=14, padx=14, bd=4,relief="ridge", command=lambda: clickbutton(0))
bt0.place(x=160, y=100)

# Fileira 2
bt4 = Button(root, text="4", bg="#C6C6F7", fg="black", pady=14, padx=14, bd=4,relief="ridge", command=lambda: clickbutton(4))
bt4.place(x=10, y=155)

bt5 = Button(root, text="5", bg="#C6C6F7", fg="black", pady=14, padx=14, bd=4,relief="ridge", command=lambda: clickbutton(5))
bt5.place(x=60, y=155)

bt6 = Button(root, text="6", bg="#C6C6F7", fg="black", pady=14, padx=14, bd=4,relief="ridge", command=lambda: clickbutton(6))
bt6.place(x=110, y=155)

btpoint = Button(root, text=".", bg="#C6C6F7", fg="black", pady=14, padx=14.5,bd=4,relief="ridge", command=clickpoint)
btpoint.place(x=10, y=270)

# Fileira 3
bt7 = Button(root, text="7", bg="#C6C6F7", fg="black", pady=14, padx=14, bd=4,relief="ridge", command=lambda: clickbutton(7))
bt7.place(x=10, y=210)

bt8 = Button(root, text="8", bg="#C6C6F7", fg="black", pady=14, padx=14, bd=4,relief="ridge", command=lambda: clickbutton(8))
bt8.place(x=60, y=210)

bt9 = Button(root, text="9", bg="#C6C6F7", fg="black", pady=14, padx=14, bd=4,relief="ridge", command=lambda: clickbutton(9))
bt9.place(x=110, y=210)

# Fileira 4
btsum = Button(root, text="+", bg="#C6C6F7", fg="black", pady=14, padx=13, bd=4,relief="ridge", command=clicksum)
btsum.place(x=160, y=210)

btsub = Button(root, text="-", bg="#C6C6F7", fg="black", pady=14, padx=14, bd=4,relief="ridge", command=clicksub)
btsub.place(x=160, y=270)

btmul = Button(root, text="x", bg="#C6C6F7", fg="black", pady=14, padx=14, bd=4,relief="ridge", command=clickmult)
btmul.place(x=210, y=100)

btdiv = Button(root, text="/", bg="#C6C6F7", fg="black", pady=13.5, padx=14, bd=4,relief="ridge", command=clickdiv)
btdiv.place(x=160, y=155)

# Botão de CE
btCE = Button(root, text="CE", bg="#C6C6F7", fg="black", pady=14, padx=10, bd=4,relief="ridge", command=deletar)
btCE.place(x=58, y=270)

# Botão de igual
btequal = Button(root, text="=", bg="#C6C6F7", fg="black", pady=14, padx=13, bd=4,relief="ridge", command=clickequal)
btequal.place(x=110, y=270)

root.resizable(False, False)
root.geometry("280x380")
root.mainloop()