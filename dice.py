import tkinter
import random
root = tkinter.Tk()
root.geometry('600x600')
root.title('rolling dice')
label = tkinter.Label(root,text='',font=('Helvetica',260))
label1 = tkinter.Label(root,text='welcome to the project click here to roll the dice',font=('Helvetica',10))
label1.place(x=150,y=400)
def roll_dice():
    value = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    result = random.choice(value)
    label.config(text=result)
    label.pack()
    if (result == '\u2680'):
        label2 = tkinter.Label(root,text ='you rolled one! click here to roll again',font=('Helvetica',10))
        label2.place(x=150,y=450)
    if (result == '\u2681'):
        label2 = tkinter.Label(root,text ='you rolled two! click here to roll again',font=('Helvetica',10))
        label2.place(x=150,y=450)
    if (result == '\u2682'):
        label2 = tkinter.Label(root,text ='you rolled Three! click here to roll again',font=('Helvetica',10))
        label2.place(x=150,y=450)
    if (result == '\u2683'):
        label2 = tkinter.Label(root,text ='you rolled Four! click here to roll again',font=('Helvetica',10))
        label2.place(x=150,y=450)
    if (result == '\u2684'):
        label2 = tkinter.Label(root,text ='you rolled Five! click here to roll again',font=('Helvetica',10))
        label2.place(x=150,y=450)
    if (result == '\u2685'):
        label2 = tkinter.Label(root,text ='you rolled Six! click here to roll again',font=('Helvetica',10))
        label2.place(x=150,y=450)
button = tkinter.Button(root,text='roll sice',foreground='red',command=roll_dice)
button.pack()
root.mainloop()
    
        