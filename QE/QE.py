from tkinter import *

def solution():
    a = ent4.get()
    b = ent5.get()
    c = ent6.get()
    D = (int(b)*int(b)) - 4 * int(a) * int(c)
    x1 = (-(int(b)-int(D)**0.5)) / (2*int(a))
    x2 = (-(int(b)+int(D)**0.5)) / (2*int(a))
    if int(D) > 0 and x1 != -0 and x2 != -0:
        string_to_display =f"Discriminant is - {int(D)}\nFirst root is - {x1}\nSecond root is - {x2}"
        lb7 =Label(win,font=("Times",13,"bold"))
        lb7["text"]=string_to_display
        lb7.grid(row=11,column=0)
    elif int(D) > 0 and x1 == -0:
        string_to_display =f"Discriminant is - {int(D)}\nFirst root is - 0\nSecond root is - {x2}"
        lb7 =Label(win,font=("Times",13,"bold"))
        lb7["text"]=string_to_display
        lb7.grid(row=11,column=0)
    elif int(D) > 0 and x2 == -0:
        string_to_display = f"Discriminant is - {int(D)}\nFirst root is - {x1}\nSecond root is - 0"
        lb7 =Label(win,font=("Times",13,"bold"))
        lb7["text"]=string_to_display
        lb7.grid(row=11,column=0)
    elif int(D) < 0:
        string_to_display = "ERROR!\nDiscriminant is negative\nNot roots!\nSolution cant be."
        lb7 =Label(win,fg="red",font=("Times",13,"bold"))
        lb7["text"]=string_to_display
        lb7.grid(row=11,column=0)
    elif int(D) == 0:
        x1 = (-(int(b)-int(D)**0.5)) / (2*int(a))
        string_to_display = f"Discriminant is zero.\n Only one roots - {x1}"
        lb7 =Label(win,fg="green",font=("Times",13,"bold","underline"))
        lb7["text"]=string_to_display
        lb7.grid(row=11,column=0)
        
win = Tk ()
win.title("Quadratic equation ")
win.geometry("415x350")
lb1 = Label(win,text="Welcome!", font=("Times", 20)).grid()
lb2 = Label(win,text="We can help you with the solution of the quadratic equation", font=("Times", 13)).grid()
lb3 = Label(win, text="You must be to enter only coefficients A,B,C.", font=("Times", 13,"bold"), fg="red").grid()

lb4 = Label(win,text="A:", font=("Times", 13,"bold"), fg="blue")
lb4.grid(row=3,column=0)
ent4 = Entry(win)
ent4.grid(row=4,column=0)

lb5 = Label(win,text="B:", font=("Times", 13,"bold"), fg="blue")
lb5.grid(row=5,column=0)
ent5 = Entry(win)
ent5.grid(row=6,column=0)

lb6 = Label(win,text="C:", font=("Times", 13,"bold"), fg="blue")
lb6.grid(row=7,column=0)
ent6 = Entry(win)
ent6.grid(row=8,column=0)

Btn1 =Button(win,text="Solution", fg="green",command=solution)
Btn1.grid(row=10,column=0)
win.mainloop()


