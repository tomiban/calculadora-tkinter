#Contiene funciones relacionadas con las operaciones matemáticas y la evaluación de expresiones.

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
    msg = msg_askyesno()
    if not msg:
        print("Operación cancelada")
    else:
        lista.delete(0, tk.END)
        historial.clear()
        msg_confirmacion()

# Esta función se llama cuando se presiona el botón "Borrar". Borra el elemento seleccionado en el ListBox y lo elimina de la lista historial.
def borrar_historial(lista, historial):
    # Obtenemos los indices en una tupla que ubican a la seleccion en la listbox (indice, )
    indices = lista.curselection()
    if indices:
        # Elimina visualmente el elemento seleccionado en la lista.
        lista.delete(indices)
        # Elimina el elemento de la lista historial.
        historial.pop(indices[0])

# Esta función se llama cuando se presiona el botón "Reciclar". Obtiene el elemento seleccionado en la ListBox, extrae la primera parte de la cadena y la coloca en el campo de entrada visor
def reciclar_historial(lista,  visor):
    indices = lista.curselection()  # Devuelve una tupla (indice,)

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
        print("Falló la operación")

#Funcion que calcula potencia cuadrada
def calcular_potencia(base, exponente):
    return base ** exponente

#Funcion que calcula raiz cuadrada
def calcular_raiz(n):
    return sqrt(n)

# La función se encarga de evaluar una expresión matemática dada como cadena de texto en el arg expresion y devuelve el resultado de la evaluación.
def calcular_expresion(expresion):
    # Operadores y números válidos en la expresión.
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
            base = int(base)  # Convierte la base a un entero.
            # Enviamos la base para calcular la potencia cuadrada.
            resultado = calcular_potencia(base, 2)
            return resultado

        # Si la expresión contiene "√", calcula la raíz cuadrada.
        if "√" in expresion:
            base = expresion.replace("√", "")  # Elimina "√" de la expresión.
            base = int(base)  # Convierte la base a un entero.
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
