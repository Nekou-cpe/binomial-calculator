from tkinter import *
import tkinter as tk
from tkinter import ttk
import scipy.stats as stats
#binomial calcuating function
def calculate_cumulative_prob():
    n = int(n_entry.get())
    p = float(p_entry.get())
    x = int(x_entry.get())

    cumulative_prob = stats.binom.cdf(x, n, p)
    result_label.config(text=f'P(X ≤ {x}) = {cumulative_prob:.4f}')
#screan shapes
root = tk.Tk()
root.title("Binomial Calculator")
w=400
h=400
ws=root.winfo_screenwidth()
hs=root.winfo_screenheight()
x=(ws/2)-(w/2)
y=(hs/2)-(h/2)
root.geometry('%dx%d+%d+%d'%(w,h,x,y))
frame1=Frame(root,width='400',height='400',bg='#FFCCE5')
frame1.pack()
n_label = ttk.Label(master=frame1, text="Number of Trials (n):")
n_label.place(x=130,y=40)
n_entry = ttk.Entry(master=frame1)
n_entry.place(x=130,y=80)

p_label = ttk.Label(master=frame1, text="Probability of Success (p):")
p_label.place(x=130,y=120)
p_entry = ttk.Entry(master=frame1)
p_entry.place(x=130,y=160)

x_label = ttk.Label(master=frame1, text="Value for Cumulative Distribution (x):")
x_label.place(x=130,y=200)
x_entry = ttk.Entry(master=frame1)
x_entry.place(x=130,y=240)

calculate_button = ttk.Button(master=frame1, text="Calculate", command=calculate_cumulative_prob)
calculate_button.place(x=130,y=280)

result_label = ttk.Label(master=frame1, text="")
result_label.place(x=130,y=320)

me_label = ttk.Label(master=frame1, text="by nekou dfrm")
me_label.place(x=10,y=360)

root.mainloop()
#my git: nekou-cpe