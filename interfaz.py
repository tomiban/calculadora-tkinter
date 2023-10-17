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
BOTONES = [
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
    ("=", COLORES["NEGRO"], 4, 4),
    ("CE", COLORES["NARANJA_OSCURO"], 1, 3),
    ("C", COLORES["NARANJA_OSCURO"], 1, 4),
]

# VARIABLES GLOBALES
historial = []  # Almacena el historial de operaciones

ventana_principal = None  # Almacena la ventana principal que nos llegará del main en la funcion crear_calculadora_gui

top_level = None  # Almacena la ventana top level que maneja el historial de operaciones, al momento de ser iniciada

isHistorialOpen = False  # Bandera para determinar si la ventana historial se encuentra abierta

# Esta función se utiliza para controlar las acciones de los botones en la calculadora. Recibe tres argumentos: valor es el valor del botón presionado, visor es el Entry donde se muestra la expresión y el resultado, y ventana_principal es la ventana principal de la calculadora.
def manejador_evento_boton(valor, visor):
    if valor == "=":
        # Obtener la expresión actual en el visor
        expresion = visor.get()
        
        # Borra el contenido del visor
        visor.delete(0, "end")
        
        # Calcular el resultado de la expresión
        resultado = calcular_expresion(expresion)
        
        visor.insert(0, resultado)
        
        # Si lo que retorna calcular_expresion es un error, retornamos None y salimos de la función sin agregar la operacion al historial
        if (resultado == 'Math Error' or resultado == 'Syntax Error' or resultado == 'Invalid Expression'):
            return None
        else:
        # Si es un resultado válido, lo añadimos al historial
            historial.append(expresion + " = " + str(resultado))
            print(historial)
            
    elif valor == "Log":
        # Accedemos a las variables globales para poder modificarlas dentro del contexto de la funcionz
        global isHistorialOpen
        global top_level

        if not isHistorialOpen:
            # Si la ventana de historial no está abierta, la creamos y establecemos la bandera en True
            top_level = crear_top_level(visor)
            isHistorialOpen = True
        else:
            # Si la ventana de historial ya está abierta, la cerramos y establecemos la bandera en False
            cerrar_top_level(top_level)
            isHistorialOpen = False
    
    elif valor == "CE":
        # Elimina el último carácter en el visor
        visor.delete(len(visor.get()) - 1, "end")
    
    elif valor == "C":
        # Borra completamente el contenido del visor
        visor.delete(0, "end")
    
    else:
        # Si no se cumple ninguna de las condiciones anteriores, asumimos que se ha presionado un botón numérico, operador o punto decimal, y agregamos ese valor al visor en la posición actual (al final de la entrada).
        visor.insert("end", valor)

# Función que destruye la ventana secundaria
def cerrar_top_level(window):
    window.destroy()

# Función que crea y retorna la ventana secundaria del historial de operaciones
def crear_top_level(visor):
    # Crea una nueva ventana secundaria (Toplevel) dentro de la ventana principal.
    ventana_historial = tk.Toplevel(ventana_principal)

    # Asigna un ícono a la ventana secundaria.
    ventana_historial.iconbitmap("./img/history.ico")

    # Configura el fondo de la ventana secundaria.
    ventana_historial.configure(bg=COLORES["NEGRO"])

    # Configura la expansión de las filas y columnas en la ventana secundaria.
    ventana_historial.columnconfigure(0, weight=1)
    ventana_historial.columnconfigure(1, weight=1)
    ventana_historial.columnconfigure(2, weight=1)
    ventana_historial.rowconfigure(0, weight=1)
    ventana_historial.rowconfigure(1, weight=1)
    ventana_historial.rowconfigure(2, weight=1)

    # Crea una etiqueta para mostrar el título "Historial de Operaciones".
    etiqueta = tk.Label(
        ventana_historial,
        text="Historial de Operaciones",
        font=("Arial", 14, "bold"),
        bg=COLORES["NEGRO"],
        fg=COLORES["CELESTE"],
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

    # Calcula el ancho máximo para los botones en función del texto de mayor longitud.
    ancho_maximo = len("Borrar Todos")

    # Crea el botón "Borrar Todos" que llama a la función borrar_todo_historial.
    boton_borrar_todos = tk.Button(
        ventana_historial,
        text="Borrar Todos",
        command=lambda lista=lista, his=historial: borrar_todo_historial(
            lista, his),
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
        command=lambda lista=lista, his=historial: borrar_historial(
            lista, his),
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
        command=lambda lista=lista, visor=visor: reciclar_historial(
            lista, visor),
        bg=COLORES["VERDE"],
        width=ancho_maximo,
        fg="white",
        font=("Arial", 8, "bold"),
        height=2,
    )
    boton_reciclar.grid(row=2, column=2, pady=0, sticky="nsew")

    return ventana_historial

# Función que crea los botones dinámicamente
def crear_boton(marco, text, visor):
    return tk.Button(
        marco,
        width=7,
        font=("Arial", 8, "bold"),
        height=2,
        text=text,
        command=lambda text=text, visor=visor: manejador_evento_boton(
            text, visor),
    )

# Función que crea la interfaz gráfica de la calculadora.
def crear_calculadora_gui(vp):
    global ventana_principal
    ventana_principal = vp
    # Etiqueta que muestra el título "CASIO" en la parte superior de la calculadora.
    etiqueta = tk.Label(
        vp,
        text="CASIO",
        font=("Arial", 11, "bold", "italic"),
        bg=COLORES["GRIS_OSCURO"],
        fg=COLORES["GRIS"],
    )
    etiqueta.grid(row=0, column=0, sticky="nw", pady=(10, 5), padx=5)

    # Entry que simula el visor donde se mostrarán las expresiones y resultados.
    visor = tk.Entry(
        vp,
        font=("Arial", 25, "bold"),
        width=21,
        bg=COLORES["VERDE"],
        justify="right",
        relief="sunken",
        bd=3,
        highlightbackground="#212121",
    )
    visor.grid(row=1, column=0, columnspan=1, pady=(5, 0),
               padx=7, sticky="nsew")

    # Marco que contiene los botones de la calculadora.
    marco_botones = tk.Frame(vp, bg=COLORES["GRIS_OSCURO"])
    marco_botones.grid(row=2, column=0, columnspan=1, padx=7,
                       pady=(15, 10), sticky="nsew")

    # Itera a través de la configuración de los botones (BOTONES).
    for text, bg, row, column in BOTONES:
        # Disponemos el color de la fuente según el color de fondo de cada botón.
        if bg == COLORES["NARANJA_OSCURO"] or bg == COLORES["GRIS"]:
            fg = "black"
        else:
            fg = "white"

        # Crea y coloca un botón en el marco de botones.
        btn = crear_boton(marco_botones, text, visor)
        btn.config(bg=bg, fg=fg)
        btn.grid(row=row, column=column, padx=7, pady=7, sticky="nsew")

    # Configuración para la expansión de columnas y filas en el marco de botones. (Junto con la propiedad nsew hace que los botones se estiren junto a la ventana marco_botones, que también se ve afectada en la configuración del main)
    for i in range(5):
        marco_botones.columnconfigure(i, weight=1)
    for i in range(5):
        marco_botones.rowconfigure(i, weight=1)
