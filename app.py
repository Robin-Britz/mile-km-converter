import tkinter

from pandas.core.groupby.base import transform_kernel_allowlist

window = tkinter.Tk()
window.title("Convert Miles > Km")
window.config(padx=60, pady=20)

def convertion():
    miles = float(user_input.get())
    km = round(miles * 1.61, 2)
    result.config(text=f"{km}")

# input
user_input = tkinter.Entry()
user_input.config(width=5)
user_input.grid(column=1, row=0)

# input label
label_miles = tkinter.Label()
label_miles.config(text="Miles")
label_miles.grid(column=2, row=0)

# 'is equal to' label
label_equal = tkinter.Label()
label_equal.config(text="is equal to")
label_equal.grid(column=0, row=1)

# result
result = tkinter.Label()
result.config(text="0")
result.grid(column=1, row=1)

# result label
label_result = tkinter.Label()
label_result.config(text="Km")
label_result.grid(column=2, row=1)

# calculate button
button = tkinter.Button()
button.config(text="Calculate", command=convertion)
button.grid(column=1, row=2)

tkinter.mainloop()