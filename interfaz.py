# Contiene funciones relacionadas con la interfaz de usuario
import tkinter as tk
from operaciones import reciclar_historial, borrar_historial, borrar_todo_historial, calcular_expresion

# Diccionario de colores
COLORES = {
   "NEGRO": "#212121",
    "GRIS_OSCURO": "#5C5C5C",
    "GRIS": "#B0B0B0",
    "NARANJA_CLARO": "#FFA500",
    "NARANJA_OSCURO": "#EE7600",
    "ROJO": "#ff4353",
    "CELESTE": "#688EEB",
    "VERDE": '#7CCD7C'
}

# Lista de tuplas botones: (text, bg, row, column)
botones_config = [
    ("Log", COLORES["CELESTE"], 0, 0),
    ("7", COLORES["NEGRO"], 1, 0),
    ("8", COLORES["NEGRO"], 1, 1),
    ("9", COLORES["NEGRO"], 1, 2),
    ("4", COLORES["NEGRO"], 2, 0),
    ("5", COLORES["NEGRO"], 2, 1),
    ("6", COLORES["NEGRO"], 2, 2),
    ("*", COLORES["NEGRO"], 2, 3),
    ("/", COLORES["NEGRO"], 2, 4),
    ("1", COLORES["NEGRO"], 3, 0),
    ("2", COLORES["NEGRO"], 3, 1),
    ("3", COLORES["NEGRO"], 3, 2),
    ("+", COLORES["NEGRO"], 3, 3),
    ("-", COLORES["NEGRO"], 3, 4),
    ("0", COLORES["NEGRO"], 4, 0),
    (".", COLORES["NEGRO"], 4, 1),
    ("√", COLORES["NEGRO"], 4, 2),
    ("^2", COLORES["NEGRO"], 4, 3),
    ("=", COLORES["GRIS"], 4, 4),
    ("CE", COLORES["NARANJA_OSCURO"], 1, 3),
    ("C", COLORES["NARANJA_OSCURO"], 1, 4),
]


# Lista para controlar el historial de operaciones
historial = []
# Variable global para almacenar la ventana top level que maneja el historial de operaciones  
tl = None
#Variable global bandera para determinar si la ventana historial se encuentra abierta
isHistorialOpen = False

# Esta función se utiliza para controlar las acciones de los botones en la calculadora. Recibe tres argumentos: valor es el valor del botón presionado, visor es el Entry donde se muestra la expresión y el resultado, y ventana_principal es la ventana principal de la calculadora.
def handler_btn(valor, visor, ventana_principal):
    if valor == "=":
        expresion = visor.get()
        visor.delete(0, "end")
        resultado = calcular_expresion(expresion)
        visor.insert(0, resultado)
        # Si lo que retorna calc_expresion es un error retornamos None y salimos de la funcion
        if (resultado == 'Math Error' or resultado == 'Sintax Error' or resultado == 'Error'):
            return None
        # Si es un resultado valido lo metememos en el la lista
        historial.append(expresion + " = " + str(resultado))
        print(historial)
    elif valor == "Log":
        global isHistorialOpen
        global tl
        if not isHistorialOpen:
            tl = crear_top_level(ventana_principal, visor)
            isHistorialOpen = True
        else:
            cerrar_top_level(tl)
            isHistorialOpen = False
    elif valor == "CE":
        visor.delete(len(visor.get()) - 1, "end")
    elif valor == "C":
        visor.delete(0, "end")
    else:
        visor.insert("end", valor)
        
def cerrar_top_level(window):
    window.destroy()

def crear_top_level(ventana_principal, visor):
    # Crea una nueva ventana secundaria (Toplevel) dentro de la ventana principal.
    ventana_historial = tk.Toplevel(ventana_principal)

    # Asigna un ícono (iconbitmap) a la ventana secundaria desde el archivo "./img/history.ico".
    ventana_historial.iconbitmap("./img/history.ico")

    # Configura el fondo de la ventana secundaria .
    ventana_historial.configure(bg=COLORES["NEGRO"])

    # Configura la expansión de las filas y columnas en la ventana secundaria.
    ventana_historial.columnconfigure(0, weight=1)
    ventana_historial.rowconfigure(0, weight=1)
    ventana_historial.rowconfigure(1, weight=1)
    ventana_historial.rowconfigure(2, weight=1)

    # Crea una etiqueta para mostrar el título "Historial de Operaciones".
    etiqueta = tk.Label(
        ventana_historial,
        text="Historial de Operaciones",
        font=("Arial", 14, "bold"),
        bg=COLORES["NEGRO"],
        fg=COLORES["VERDE"],
        height=2,
    )
    etiqueta.grid(row=0, column=0, columnspan=3, pady=(5), sticky="nsew")

    # Crea una Listbox para mostrar las operaciones en el historial.
    lista = tk.Listbox(
        ventana_historial,
        bg=COLORES["GRIS_OSCURO"],
        relief="flat",
        font=("Arial", 14),
        selectbackground=COLORES["NARANJA_CLARO"],
        fg="white",
        selectforeground="black",
    )
    lista.grid(row=1, column=0, columnspan=3, sticky="nsew")

    # Llena la lista con elementos del historial almacenados en la variable 'historial'.
    for item in historial:
        lista.insert(tk.END, item)

    # Calcula el ancho máximo para los botones en función del texto "Borrar Todos".
    ancho_maximo = len("Borrar Todos")

    # Crea el botón "Borrar Todos" que llama a la función borrar_todo_historial.
    boton_borrar_todos = tk.Button(
        ventana_historial,
        text="Borrar Todos",
        command=lambda lista=lista: borrar_todo_historial(lista, historial),
        bg=COLORES["ROJO"],
        width=ancho_maximo,
        fg="white",
        font=("Arial", 8, "bold"),
        height=2,
    )
    boton_borrar_todos.grid(row=2, column=0, pady=0, sticky="nsew")

    # Crea el botón "Borrar" que llama a la función borrar_historial.
    boton_borrar = tk.Button(
        ventana_historial,
        text="Borrar",
        command=lambda lista=lista: borrar_historial(lista, historial),
        bg=COLORES["NARANJA_CLARO"],
        width=ancho_maximo,
        fg="white",
        font=("Arial", 8, "bold"),
        height=2,
    )
    boton_borrar.grid(row=2, column=1, pady=0, sticky="nsew")

    # Crea el botón "Reciclar" que llama a la función reciclar_historial.
    boton_reciclar = tk.Button(
        ventana_historial,
        text="Reciclar",
        command=lambda: reciclar_historial(lista, visor),
        bg=COLORES["CELESTE"],
        width=ancho_maximo,
        fg="white",
        font=("Arial", 8, "bold"),
        height=2,
    )
    boton_reciclar.grid(row=2, column=2, pady=0, sticky="nsew")
    
    return ventana_historial

def create_button(marco, text, visor, ventana_principal):
    return tk.Button(
        marco,
        width=7,
        font=("Arial", 8, "bold"),
        height=2,
        text=text,
        command=lambda v=text: handler_btn(v, visor, ventana_principal),
    )  # Expand both vertically and horizontally

def crear_calculadora_gui(ventana_principal):
    # Etiqueta que muestra el título "CASIO" en la parte superior de la calculadora.
    etiqueta = tk.Label(
        ventana_principal,
        text="CASIO",
        font=("Arial", 11, "bold", "italic"),
        bg=COLORES["GRIS_OSCURO"],
        fg=COLORES["GRIS"],
    )
    etiqueta.grid(row=0, column=0, sticky="nw", pady=(10, 5), padx=5)

    # Entry que simula el visor donde se mostrarán las expresiones y resultados.
    visor = tk.Entry(
        ventana_principal,
        font=("Arial", 25, "bold"),
        width=21,
        bg=COLORES["VERDE"],
        justify="right",
        relief="sunken",
        bd=3,
        highlightbackground="#212121",
    )
    visor.grid(row=1, column=0, columnspan=1, pady=(5, 0),
               padx=7, sticky="nsew")  # Expand horizontally

    # Marco que contiene los botones de la calculadora.
    marco_botones = tk.Frame(ventana_principal, bg=COLORES["GRIS_OSCURO"])
    marco_botones.grid(row=2, column=0, columnspan=1, padx=7,
                       pady=(15, 10), sticky="nsew")  # Expand vertically

    # Itera a través de la configuración de los botones (botones_config).
    for text, bg, row, column in botones_config:
        if bg == COLORES["NARANJA_OSCURO"] or bg == COLORES["GRIS"]:
            fg = "black"
        else:
            fg = "white"

        # Crea y coloca un botón en el marco de botones.
        btn = create_button(marco_botones, text, visor, ventana_principal)
        btn.config(bg=bg,fg=fg )
        btn.grid(row=row, column=column, padx=7, pady=7, sticky="nsew")

    # Configuración para la expansión de columnas y filas en el marco de botones. (Junto con la propiedad nsew hace que los elementos se estiren junto a la ventana)
    for i in range(5):
        marco_botones.columnconfigure(i, weight=1)
    for i in range(5):
        marco_botones.rowconfigure(i, weight=1)
