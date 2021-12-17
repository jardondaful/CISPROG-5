import tkinter as tk
from functools import partial
values = "Celsius"

def record_temp(temp1):
  global values
  values = temp1
def tmp1(lbl1, lbl2, inputn):
  tmp = inputn.get()
  if values == 'Celsius':
    fah = float((float(tmp) * 9 / 5) + 32)
    kelvin = float((float(tmp) + 273.15))
    lbl1.config(text="%f Degrees Fahrenheit" % fah)
    lbl2.config(text="%f Degrees Kelvin" % kelvin)
  if values == 'Fahrenheit':
    celcius = float((float(tmp) - 32) * 5 / 9)
    kelvin = celcius + 273
    lbl1.config(text="%f Degrees Celsius" % celcius)
    lbl2.config(text="%f Degrees Kelvin" % kelvin)
  if values == 'Kelvin':
    celcius = float((float(tmp) - 273.15))
    fah = float((float(tmp) - 273.15) * 1.8000 + 32.00)
    lbl1.config(text="%f Degrees Celsius" % celcius)
    lbl2.config(text="%f Degrees Fahrenheit" % fah)
  return
  
root = tk.Tk()
root.bind('<Return>', (lambda event: tmp1()))  
root.geometry('400x150+100+200')
root.title('Temperature Converter')
root.configure(background='#09A3BA')
root.resizable(width=False, height=False)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
inp = tk.StringVar()
var = tk.StringVar()
lbl3 = tk.Label(root, text="Enter temperature", background='#09A3BA', foreground="#FFFFFF")
ent = tk.Entry(root, textvariable=inp)
lbl3.grid(row=1)
ent.grid(row=1, column=1)
lbl4 = tk.Label(root, background='#09A3BA', foreground="#FFFFFF")
lbl4.grid(row=3, columnspan=4)
lbl5 = tk.Label(root, background='#09A3BA', foreground="#FFFFFF")
lbl5.grid(row=4, columnspan=4)
ddl = ["Celsius", "Fahrenheit", "Kelvin"]
dd = tk.OptionMenu(root, var, *ddl, command=record_temp)
var.set(ddl[0])
dd.grid(row=1, column=3)
dd.config(background='#09A3BA', foreground="#FFFFFF")
dd["menu"].config(background='#09A3BA', foreground="#FFFFFF")
tmp1 = partial(tmp1, lbl4, lbl5, inp)
btn = tk.Button(root, text="Convert", command=tmp1, background='#09A3BA', foreground="#FFFFFF")
btn.grid(row=2, columnspan=4)

root.mainloop()
