# 1 EJERCICIO TEMA 14 TKINTER
# Escribe el código necesario para crear una ventana utilizando tkinter
# Debe mostrar un texto de presentación o una advertencia

import tkinter as tk

root = tk.Tk()

text = tk.Text(root)
text.pack()

label = tk.Label(text, text = "Hola,me llamo Sigrid.")
label.pack(side = "left")

entry = tk.Entry(text)
entry.pack(side = "right")

frame2 = tk.Frame(root)
frame2.pack()

label2 = tk.Label(frame2, text = "Soy de Málaga.")
label2.pack(side = "left")

entry2 = tk.Entry(frame2)
entry2.pack(side = "right")


root.mainloop()