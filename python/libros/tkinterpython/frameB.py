# -*- coding: utf-8 -*-


from Tkinter import *


marco1 = Tk()
marco2 = Toplevel(marco1)

marco1.config(bg="")
marco1.geometry("300x300")

def mostrar_ventana(ventana): ventana.deiconify()
def ocultar_ventana(ventana): ventana.withdraw()
def ejecutar(f): marco1.after(200, f)

# creamos el boton creamos un evento para mostrar una nueva ventana...
btn_mostrar = Button(marco1, text="Mostrar Ventana", command=lambda:
	ejecutar(mostrar_ventana(marco2)))
# cargarmos el boton...
btn_mostrar.grid(row=1, column=1)

btn_ocultar = Button(marco1, text="Ocultar Ventana", command=lambda:
	ejecutar(ocultar_ventana(marco2)))
btn_ocultar.grid(row=1, column=2)

marco2.withdraw()

marco1.mainloop()

