#Contiene los metodos que inian la ventana principal y la invocacion de la GUI

import tkinter as tk
from interfaz import COLORES, crear_calculadora_gui

ventana_principal = tk.Tk()
ventana_principal.title("Calculadora")
ventana_principal.configure(background=COLORES["GRIS_FONDO"])
ventana_principal.geometry("380x390")
#Metodo para agregar un icono a la ventana. Recibe como argumento un path con la ubicacion relativa del archivo
ventana_principal.iconbitmap('./img/calculadora.ico')

#Configuraciones para estirar la ventana
ventana_principal.columnconfigure(0, weight=1)
ventana_principal.rowconfigure(1, weight=1)  
ventana_principal.rowconfigure(2, weight=1)

#Llamamos a la función que crea la interfaz, le pasamos como argumento la variable que almacena la instancia de la ventana principal
crear_calculadora_gui(ventana_principal)
    
ventana_principal.mainloop()