import tkinter as tk
from tkinter import *
import tkinter.messagebox
root = tk.Tk()
root.title("Currency Converter")
Tops = Frame(root,bg='#fffde7',pady=2,width=1850,height=100,relief="ridge")
Tops.grid(row=0,column=0)
headlabel = tk.Label(Tops,font =('lato black',19,'bold'),text='Currency Converter',bg="#80deea",fg='black')
headlabel.grid(row=1,column=0,sticky=W)
variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)
variable1.set("currency")
variable2.set("currency")
def realtimecurrencyconversion():
    rates = {"USD":{"INR":83.0,"EUR":0.92},
             "INR":{"USD":0.012,"EUR":0.011},
             "EUR":{"USD":0.012,"INR":0.011}}
    from_currency = variable1.get()
    to_currency = variable2.get()
    if(Amount1_field.get() == ""):
        tkinter.messagebox.showinfo("Error !!","Amount not entered.\n please enter a valid amount")
    elif(from_currency=="currency" or to_currency=="currency"):
        tkinter.messagebox.showinfo("Error !!","Currency not selected.\n please select a From and To currency from menu")
    else:
        try:
            amount = float(Amount1_field.get())
            if from_currency in rates and to_currency in rates[from_currency]:
                new = amount*rates[from_currency][to_currency]
                Amount2_field.delete(0,tk.END)
                Amount2_field.insert(0,str(round(new,4)))
            else:
                tkinter.messagebox.showinfo("Erroe !!","conversion rate is not avaliable")
        except:
            tkinter.messagebox.showinfo("Eroor !!","Invalid Amount entered")
def clear_all():
    Amount1_field.delete(0,tk.END)
    Amount2_field.delete(0,tk.END)
currencycode_list = ["INR","USD","EUR"]
root.configure(background="#e6ee9c")
root.geometry("700x400")
label1 = tk.Label(root,font=('lato black',15,'bold'),text="\t Amount :",bg="#e6ee9c",fg="black")
label1.grid(row= 2,column=0,sticky=W)
Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2,column=0,sticky=E,ipadx=28)
Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8,column=0,sticky=E,ipadx=31)
FromCurrency_option = tk.OptionMenu(root,variable1,*currencycode_list)
ToCurrency_option = tk.OptionMenu(root,variable2,*currencycode_list)
FromCurrency_option.grid(row=3,column=0,sticky=E,ipadx=45)
ToCurrency_option.grid(row=4,column=0,sticky=E,ipadx=45)
Label_9 = Button(root,font=('arial',15,'bold'),text="Convert",padx=2,pady=2,bg="lightblue",fg="white",command=realtimecurrencyconversion)
Label_9.grid(row=6,column=0)
Label_9 = Button(root,font=('arial',15,'bold'),text="Clear",padx=2,pady=2,bg="lightblue",fg="white",command=clear_all)
Label_9.grid(row=10,column=0)
root.mainloop()