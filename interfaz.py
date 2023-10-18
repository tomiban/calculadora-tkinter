# Contiene funciones relacionadas con la interfaz de usuario

import tkinter as tk
from operaciones import reciclar_historial, borrar_historial, borrar_todo_historial, calcular_expresion

# Constante que almacena un diccionario de colores
COLORES = {
    "NEGRO": "#212121",
    "GRIS_FONDO": "#5C5C5C",
    "GRIS": "#B0B0B0",
    "GRIS_OSCURO": "#4B4A46",
    "NARANJA": "#FFA500",
    "NARANJA_OSCURO": "#EE7600",
    "ROJO": "#ff4353",
    "CELESTE": "#688EEB",
    "VERDE": '#7CCD7C'
}

# Constante que almacena una lista de tuplas con info de los botones (text, bg, row, column)
BOTONES = [
    ("Log", COLORES["CELESTE"], 0, 0),
    ("ON", COLORES["GRIS_OSCURO"], 0, 3),
    ("OFF", COLORES["ROJO"], 0, 4),
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
# Almacena el historial de operaciones
historial = []  

# Almacena la ventana principal que nos llegará del main en la funcion crear_calculadora_gui
ventana_principal = None

# Almacena la ventana top level que maneja el historial de operaciones, al momento de ser iniciada
top_level = None

# Bandera para determinar si la ventana historial se encuentra abierta
isHistorialOpen = False

#Funcion que se encarga de borrar el mensaje de bienvenida al encender la calculadora
def borrar_mensaje_bienvenida(visor):
    visor.delete(0, "end")  

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
        bg=COLORES["GRIS_FONDO"],
        relief="flat",
        font=("Arial", 14),
        selectbackground=COLORES["NARANJA"],
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
        bg=COLORES["NARANJA"],
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

# Funcion que se encarga de controlar las acciones de los botones en la calculadora. Recibe dos argumentos: valor es el texto del botón presionado, visor es el Entry.
def manejador_evento_boton(valor, visor):
    # Accedemos a las variables globales para poder modificarlas dentro del contexto de la funcionz
    global isHistorialOpen
    global top_level

    if valor == "=":
        # Obtenemos la expresión actual en el visor
        expresion = visor.get()

        # Borramos el contenido del visor
        visor.delete(0, "end")

        # Calcula el resultado de la expresión
        resultado = calcular_expresion(expresion)

        # Mostramos el valor de resultado
        visor.insert(0, resultado)

        # Si lo que retorna calcular_expresion es un error, retornamos None y salimos de la función sin agregar la operacion al historial
        if (resultado == 'Math Error' or resultado == 'Syntax Error' or resultado == 'Invalid Expression'):
            return None
        else:
        # Si es un resultado válido, lo añadimos al historial
            historial.append(expresion + " = " + str(resultado))
            
    elif valor == "Log":
        if not isHistorialOpen:
            # Si la ventana de historial no está abierta, la creamos y establecemos la bandera en True
            isHistorialOpen = True
            
            #Guardamos la ventana en la variable global para poder destruirla al volver a presionar el boton de log
            top_level = crear_top_level(visor)
        else:
            # Si la ventana de historial ya está abierta, la cerramos y establecemos la bandera en False
            isHistorialOpen = False
            cerrar_top_level(top_level)
            
    elif valor == "CE":
        # Elimina el último carácter en el visor
        visor.delete(len(visor.get()) - 1, "end")

    elif valor == "C":
        # Borra todo el contenido del visor
        visor.delete(0, "end")

    elif valor == "ON":
        visor.configure(state="normal")  # Habilita el visor
        # Muestra el mensaje de bienvenida
        visor.insert("end", "CASIO             ")
        # Llama a borrar_mensaje_bienvenida después de 1 seg
        ventana_principal.after(
            1000, lambda v=visor: borrar_mensaje_bienvenida(v))

    elif valor == "OFF":
        visor.delete(0, "end")
        visor.configure(state="disabled")  # Deshabilita el visor

    else:
        # Si no se cumple ninguna de las condiciones anteriores, asumimos que se presionó un botón numérico, operador o punto decimal, y agregamos ese valor al visor en la posición actual (al final de la entrada).
        visor.insert("end", valor)

# Función que crea los botones dinámicamente sobre los argumentos que le llegan de la iteracion de BOTONES
def crear_boton(marco, text, visor, bg):
    if text == 'ON' or text == 'OFF':
        print("Entré a ON/OFF")
        width = 2
        height = 1
    else:
        width = 7
        height = 2

    if bg == COLORES["NARANJA_OSCURO"] or bg == COLORES["GRIS"]:
        fg = "black"
    else:
        fg = "white"

    btn = tk.Button(
        marco,
        width=width,
        font=("Arial", 8, "bold"),
        height=height,
        text=text,
        bg=bg,
        fg=fg,
        command=lambda text=text, visor=visor: manejador_evento_boton(
            text, visor),
    )
    return btn

# Función que crea la interfaz gráfica de la calculadora.
def crear_calculadora_gui(vp):
    global ventana_principal

    # Almacenamos la referencia de la ventana principal en una variable global para evitar pasarla como argumento
    ventana_principal = vp

    # Etiqueta que muestra el título "CASIO" en la parte superior de la calculadora.
    etiqueta = tk.Label(
        vp,
        text="CASIO",
        font=("Arial", 11, "bold", "italic"),
        bg=COLORES["GRIS_FONDO"],
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
    
    #Deshabilitamos por defecto el visor para obligar al usuario a encenderlo con la tecla ON
    visor.configure(state='disabled')

    # Marco que contiene los botones de la calculadora.
    marco_botones = tk.Frame(vp, bg=COLORES["GRIS_FONDO"])
    marco_botones.grid(row=2, column=0, columnspan=1, padx=7,
                       pady=(15, 10), sticky="nsew")

    # Iteramos a través de la configuración de la tupla botones.
    for text, bg, row, column in BOTONES:
        # Crea y coloca un botón en el marco de botones. A  los botones que no son ON y OFF le asignamos la propiedad sticky nswew para que ocupen todo el espacio disponible. A ON le damos sticky e para que se pegue del lado derecho y se acerque a OFF.
        btn = crear_boton(marco_botones, text, visor, bg)
        if text != 'ON' and text != 'OFF':
            btn.grid(row=row, column=column, padx=7, pady=7, sticky="nsew")
        elif text == 'ON':
            btn.grid(row=row, column=column,  sticky='e', ipadx=1, ipady=1)
        else:
            btn.grid(row=row, column=column, ipadx=1, ipady=1)

    # Configuración para la expansión de columnas y filas en el marco de botones. (Junto con la propiedad sticky hace que los botones se estiren junto a la ventana marco_botones, que también se ve afectada en la configuración del main)
    for i in range(5):
        marco_botones.columnconfigure(i, weight=1)
    for i in range(5):
        marco_botones.rowconfigure(i, weight=1)