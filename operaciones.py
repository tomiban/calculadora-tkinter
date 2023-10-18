#Contiene funciones relacionadas con las operaciones matemáticas y la gestion del historial de operaciones.

import tkinter as tk
from math import sqrt 
from tkinter import messagebox

#Funcion que lanza un mensaje de confirmacion
def msg_confirmacion():
    messagebox.showinfo("Operación completada", "¡Historial borrado con éxito!")
    return None

#Funcion que lanza un mensaje de alerta y return true/false de acuerdo a lo presionado
def msg_askyesno():
    msg = messagebox.askyesno(
        title="Confirmar borrado", message="¿Deseas borrar todo el historial?")
    return msg

# Esta función se llama cuando se presiona el botón "Borrar Todos" en la ventana de historial. Elimina todos los elementos en el ListBox y borra todos los elementos en la lista historial.
def borrar_todo_historial(lista, historial):
    # Muestra un mensaje de confirmacion. Si se presiona NO, imprime en consola operacion cancelada sino borra y muestra un mensaje de confirmacion
    if len(historial) > 0:
        msg = msg_askyesno()
        if not msg:
            print("Operación cancelada")
        else:
            lista.delete(0, tk.END)
            #El metodo clear borra todos los elementos que tiene almacenados la lista
            historial.clear()
            msg_confirmacion()

# Esta función se llama cuando se presiona el botón "Borrar". Borra el elemento seleccionado en el ListBox y lo elimina de la lista historial.
def borrar_historial(lista, historial):
    # El metodo curselection devuelve una tupla con los indices que ubican a la selecciones en la listbox. Como es una listbox simple solo tiene un primer valor con el indice y el resto rstá vacio (indice,)
    indices = lista.curselection()
    if indices:
        # Elimina visualmente el elemento seleccionado en la ListBox.
        lista.delete(indices)
        # Elimina el elemento de la lista historial, le pasamos como referencia el primer elemento de la tupla que contiene el indice donde se ubicaba el elemento borrado.
        historial.pop(indices[0])

# Esta función se llama cuando se presiona el botón "Reciclar". Obtiene el elemento seleccionado en la ListBox, extrae la primera parte de la cadena y la coloca en el campo de entrada visor
def reciclar_historial(lista,  visor):
    indices = lista.curselection()  # Devuelve una tupla (indice,)
    
    #Si indices no es None entonces
    if indices:
        # Accedemos al primer valor de la tupla donde esta la posicion del elemento
        index = indices[0]
        # A partir del indice podemos capturar el valor del elemento seleccionado
        elemento = lista.get(index)
        # Cortamos la operacion en el primer espacio del string (2+2| = 4)
        resultado = elemento.split(' ')
        
        visor.delete(0, "end")
        
        # Mostramos en el visor la primer parte
        visor.insert(0, resultado[0])
    else:
        messagebox.showerror("Error","Falló la operación")

#Funcion que calcula potencia cuadrada
def calcular_potencia(base, exponente):
    return base ** exponente

#Funcion que calcula raiz cuadrada
def calcular_raiz(n):
    return sqrt(n)

# La función se encarga de evaluar una expresión matemática dada como cadena de texto en el arg expresion y devuelve el resultado de la evaluación.
def calcular_expresion(expresion):
    # Definimos operadores y números válidos para la expresión.
    operadores_validos = ("+", "-", "*", "/", "√", "^", "(", ")")
    nros_validos = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".")

    try:
        # Verifica si la expresión contiene caracteres invalidos.
        for char in expresion:
            if char not in nros_validos and char not in operadores_validos:
                return "Invalid Expression" 

        # Si la expresión contiene "^2", calcula la potencia cuadrada.
        if "^2" in expresion:
            base = expresion.replace("^2", "")  # Elimina "^2" de la cadena de caracteres, para dejar solo el string del nro.
            base = float(base)  # Convierte la base a un flotante.
            # Enviamos la base para calcular la potencia cuadrada.
            resultado = calcular_potencia(base, 2)
            return resultado

        # Si la expresión contiene "√", calcula la raíz cuadrada.
        if "√" in expresion:
            base = expresion.replace("√", "")  # Elimina "√" de la expresión.
            base = float(base)  # Convierte la base a un flotante.
            resultado = calcular_raiz(base)  # Calcula la raíz cuadrada.
            return resultado

        # Si no se encuentran operadores especiales, evalúa la expresión.
        else:
            resultado = eval(expresion)  # Evalúa la expresión matemática.
            return resultado

    except ZeroDivisionError:
        # Devuelve un mensaje de error si hay división por cero.
        return "Math Error"
    except SyntaxError:
        # Devuelve un mensaje de error si hay un error de sintaxis.
        return "Syntax Error"
