import random
import tkinter as tk
from tkinter import ttk

# main window
window = tk.Tk()
window.title("Love Calculator")
window.geometry("720x600")

# variable
result = tk.StringVar()

# calculate


def calculate():
    resultLabel.config(text="")

    randomNumber = random.randint(0, 100)
    decimal = random.randint(0, 9)

    i = 0

    while (i != 100):
        result.set(str(i) + "%")
        window.update_idletasks()
        window.after(12)
        i = i + 1

    while (i != 0):
        result.set(str(i) + "%")
        window.update_idletasks()
        window.after(12)
        i = i - 1

    while (i != 100):
        result.set(str(i) + "%")
        window.update_idletasks()
        window.after(12)

        if (i == randomNumber):
            break

        i = i + 1

    result.set(str(i))

    if (decimal != 0):
        current_result = result.get()
        new_result = current_result + "." + str(decimal) + "%"
        result.set(new_result)
    else:
        current_result = result.get()
        new_result = current_result + "%"
        result.set(new_result)


# love calculator label
titleLabel = tk.Label(window, text="Welcome to the Love Calculator")
titleLabel.pack()

# person label
p1Label = tk.Label(window, text="Person 1")
p1Label.pack(pady=(25, 0))

p1entry = tk.Entry(window)
p1entry.pack()

# plus sign
plusLabel = tk.Label(window, text="+")
plusLabel.pack(pady=(25, 0))

# person 2 label
p2Label = tk.Label(window, text="Person 2")
p2Label.pack(pady=(25, 0))

p2entry = tk.Entry(window)
p2entry.pack()

# calculate button
calcButton = tk.Button(window, text="Calculate", command=calculate)
calcButton.pack(pady=(35, 0))

# output label
outputLabel = tk.Label(window, text="Result:")
outputLabel.pack(pady=(35, 0))

# result label
resultLabel = tk.Label(window, textvariable=result)
resultLabel.pack()

# loop
window.mainloop()
