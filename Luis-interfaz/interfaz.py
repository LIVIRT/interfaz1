import tkinter
from tkinter import ttk
import json

ventana=tkinter.Tk()
ventana.title("codigo de error")

titulo=ttk.Label(ventana, text="ingrese codigo",font="Calibri 24 bold")
titulo.pack(padx=10, pady=10)

entrada=ttk.Entry(ventana)
entrada.pack(padx=10, pady=10)

btn_buscar=ttk.Button(ventana,text="buscar codigo")
btn_buscar.pack(padx=10,pady=10)



ventana.mainloop()