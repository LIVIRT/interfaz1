import tkinter
from tkinter import ttk
import json

with open('errores.json','r')as file:
    data=json.load(file)

def obtenervalores():
    codigo=entrada.get()
    for error in data['Errores']:
        if error['codigo'] == codigo:
            descripcion.config(text=error['desc'])
            break
        else:
            descripcion.config(text="decripcion no encontrada.")

ventana=tkinter.Tk()
ventana.title("codigo de error")

titulo=ttk.Label(ventana, text="ingrese codigo",font="Calibri 24 bold")
titulo.pack(padx=10, pady=10)

entrada=ttk.Entry(ventana)
entrada.pack(padx=10, pady=10)

btn_buscar=ttk.Button(ventana,text="buscar codigo",command=obtenervalores)
btn_buscar.pack(padx=10,pady=10)


descripcion=ttk.Label(ventana,text="")
descripcion.pack(padx=10,pady=10)
ventana.mainloop()