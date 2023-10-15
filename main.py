#Contiene los metodos que inian la ventana principal y la invocacion de la GUI

import tkinter as tk
from interfaz import COLORES, crear_calculadora_gui

ventana_principal = tk.Tk()
ventana_principal.title("Calculadora")
ventana_principal.configure(background=COLORES["GRIS_OSCURO"])
ventana_principal.geometry("380x390")
ventana_principal.iconbitmap('./img/calculadora.ico')

#Configuraciones para estirar la ventana
ventana_principal.columnconfigure(0, weight=1)
ventana_principal.rowconfigure(1, weight=1)  
ventana_principal.rowconfigure(2, weight=1)

#Llamamos a la función que crea la interfaz
crear_calculadora_gui(ventana_principal)

ventana_principal.mainloop()