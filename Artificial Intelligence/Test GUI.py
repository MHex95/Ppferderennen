import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Label oben")
label1.grid(row=0, column=0, columnspan=2)

button1 = tk.Button(root, text="Ich bin links oben")
button1.grid(row=1, column=0)

button2 = tk.Button(root, text="Ich bin rechts oben")
button2.grid(row=1, column=1)

button3 = tk.Button(root, text="Ich bin links unten")
button3.grid(row=2, column=0)

button4 = tk.Button(root, text="Ich bin rechts unten")
button4.grid(row=2, column=1)

label2 = tk.Label(root, text="label unten")
label2.grid(row=3, column=0, columnspan=2)

root.mainloop()