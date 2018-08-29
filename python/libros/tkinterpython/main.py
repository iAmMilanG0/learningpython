# -*- coding: utf-8 -*-

# trabajando con python v2

from Tkinter import * # importamos la libreria Tkinter

marco = Tk() # creamos el marco principal con la 'Clase Tk()' que contendra todos los elementos 

# añadiendo un fondo negro...
#marco.config(bg="black") # le da el color al fondo

# una forma de controlar la ventana seria el siguiente ejemplo...

marco.geometry("300x300") # cambia el tamaño de la ventana

# podemos declarar mas objetos pertenecientes a la clase Tkinter():

'''
Toplevel => crea una nueva ventana
Frame    => coloca los paneles para ordenar los elementos
Canvas   => para dibujar y graficar funciones y otros elementos
Button   => para colocar un boton
Label    => coloca una etiqueta de texto
Message  => coloca un mensaje
Entry    => coloca una entrada de texto de una linea
Text     => coloca una entrada de texto de varias lineas
Listbox  => coloca una lista con elementos clickeables
Menu     => Coloca un menú que puede contener cascadas y elementos clickeables
'''



marco.mainloop() # aqui usammo el metodo mainloop de la clase Tk() para asi mostrar la ventana permanente...

