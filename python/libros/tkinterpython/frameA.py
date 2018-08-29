# -*- coding: utf-8 -*- 


from Tkinter import * 

ventana1 = Tk()

ventana1.config(bg="black")

ventana1.geometry("300x300")

'''
pero como mostrar de nuevo?
si con un evento de un boton

crea un objeto de tipo boton de la clase Boton y le pasamos sus respectivos parametros
'''

#boton1 = Button(ventana1, text="Abrir otra ventana") # crea el primer boton 

'''
pero el boton no tiene ningun evento, 
ademas cargo con el metodo '.pack()', lo podemos cargar con '.grid()'
'''

#boton1.pack() # carga el boton

'''
otra manera de crearlo y cargarlo...
'''

#boton1 = Button(ventana1, text="Abrir otra ventana").pack()

'''
en una sola linea o como este:
'''

boton1 = Button(ventana1, text="Abrir ventana") # crea el boton
boton1.grid(row=1, column=1) # el boton es cargado

'''
ahora vamos a mostrar la otra ventana
creamos una funcion para mostrara
'''

def mostrar_ventana(ventana):
	ventana.deiconify() # el metodo deiconify muestra la ventana que habia sido oculta por '.withdraw()' 
 
'''
ademas una funcion para ocultar la ventana seria asi:
'''

def ocultar_ventana(ventana):
	ventana.withdraw()

'''
con estas dos funciones podemos mostrar y ocultar ventanas

=> todo mas completo en el archivo = 'frameB.py'
'''

ventana2 = Toplevel() # crea una ventana de hija (se puede evitar el inicializar con la variable)

'''
la ventana hija se puede ocultar de la siguiente manera
'''

ventana2.withdraw() # oculta la ventana 2

ventana1.mainloop()
