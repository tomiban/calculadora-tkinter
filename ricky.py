import tkinter as tk
from tkinter import Entry
#Ventana Principal
ventana_principal = tk.Tk()
ventana_principal.title("Calculadora")
ventana_principal.geometry("340x275")

def handler_btn(visor, valor):
    if valor == "=":
        Calculo= visor.get()
        Resultado= eval(Calculo)
        visor.delete(0,tk.END)
        visor.insert(tk.END,Resultado)
    elif valor == "C":
        visor.delete(0,tk.END)
            
    else:
        visor.insert(tk.END, valor)
    
#Funcion
def Crear_Calculadora_GUI(ventana_principal):
    #Campo de texto
    Visor = tk.Entry(ventana_principal,width=20,font=("arial",23))
    Visor.grid(row=0,columnspan=4,pady=(5))
    
    MarcoBotones = tk.Frame(ventana_principal).grid(row=1,column=0,pady=(40,0))


    column=0
    row=1

    #Se crea la lista de botones que van aparecer en la ventana principal
    ListaBotonex=[
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "0", "C", "=", "/"
    ]

    #Se corre la lista a travez de un bucle 
    for btn in ListaBotonex:
        tk.Button(MarcoBotones,text=btn, height=2, width=7, bg="black",fg="white", command=lambda v=btn: handler_btn(Visor, v)).grid(row=row,column=column,padx=7,pady=7)
        column=column+1
        if column==4:
            row=row+1
            column=0



Crear_Calculadora_GUI(ventana_principal)












#Main
ventana_principal.mainloop()