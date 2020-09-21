from tkinter import Canvas, Frame, Tk, PhotoImage, Button
import time

# -- -- -- Titulo

titulo = "The Weird Way"
print("=" * len(titulo) + "\n" + titulo + "\n" + "=" * len(titulo), "\n")

# -- -- -- Variables e imagenes previas

# Tamaños
tamaño = 25
columnas = 40
filas = 27
ancho = tamaño * columnas
alto = tamaño * filas

# Colores
c_fondo = "#1c1b20"
c_pantalla = "#26242b"
c_fg = "#8b64ed"
c_fg_win = "#615637"
c_bg_fg = "#222027"
c_bg_fg_win = "#d7b64c"
c_bg_press = "#1c1b20"
c_bg_press_win = "#ffd00d"

# -- -- -- Root

root = Tk()
root.title(titulo)
root.resizable(False, False)
root.geometry("{}x{}+{}+{}".format(ancho, alto, 245, 55))
root.iconbitmap("LucioPalIco.ico")
root.config(bg=c_fondo)

# -- -- -- Imagenes

logo_img = PhotoImage(file="Imagenes/Logo.png")
puente_x = PhotoImage(file="Imagenes/PuenteX.png")
puente_y = PhotoImage(file="Imagenes/PuenteY.png")
puente_xy = PhotoImage(file="Imagenes/PuenteXY.png")

# -- -- -- Frame

pantalla = Frame(root, width=ancho, height=alto, bg=c_pantalla)
pantalla.pack()

# -- -- -- Canvas

graficos = Canvas(pantalla, width=ancho, height=alto, bg=c_pantalla,
                  borderwidth=0, highlightthickness=0)
graficos.pack()

# -- -- -- Botones Menu


class Menu:  # Menu principal

    def crear_menu(self):
        graficos.delete("all")

        self.num = alto  # Reseteo del numerador de la animación de cerrado.
        self.ani_menu = graficos.create_rectangle(-1, 0, ancho, 0,
                                                  fill=c_fondo,
                                                  outline="purple")

        self.nueva = Button(graficos, text="Nueva Partida", fg=c_fg,
                            cursor="hand2", font=("Century Gothic", 20),
                            bg=c_bg_fg, width=30, activeforeground=c_fg,
                            activebackground=c_bg_press,
                            command=lambda: self.cerrar_menu("nueva"))

        self.continuar = Button(graficos, text="Continuar Partida", fg=c_fg,
                                cursor="hand2", font=("Century Gothic", 20),
                                bg=c_bg_fg, width=27, activeforeground=c_fg,
                                activebackground=c_bg_press,
                                command=lambda: self.cerrar_menu("continuar"))

        self.salir = Button(graficos, text="Salir", fg=c_fg, cursor="hand2",
                            font=("Century Gothic", 20), bg=c_bg_fg, width=24,
                            activeforeground=c_fg, activebackground=c_bg_press,
                            command=lambda: self.cerrar_menu("salir"))

        self.logo2 = graficos.create_image(ancho/2, alto/2 - alto/4,
                                           image=logo_img)
        self.nueva2 = graficos.create_window(ancho/2, alto/2 + alto/50,
                                             window=self.nueva)
        self.continuar2 = graficos.create_window(ancho/2, alto/2 + alto/5,
                                                 window=self.continuar)
        self.salir2 = graficos.create_window(ancho/2, alto/2 + alto/2.70,
                                             window=self.salir)

    def cerrar_menu(self, selected):  # 1ro: Animación, luego cerrado.
        self.nueva.config(command=lambda: None)
        self.continuar.config(command=lambda: None)
        self.salir.config(command=lambda: None)

        self.num -= 75
        graficos.coords(self.ani_menu, -1, alto, ancho, self.num)

        if selected == "nueva":
            graficos.move(self.nueva2,     - 90, 0)
        elif selected == "continuar":
            graficos.move(self.continuar2, + 90, 0)
        elif selected == "salir":
            graficos.move(self.salir2,     - 90, 0)

        if self.num > -75:  # Bucle generado para repetír el método (Animación)
            root.after(125, lambda: self.cerrar_menu(selected))

        else:  # Acciones tras animación. Eliminación de todo.
            time.sleep(0.90)  # Tiempo para que cargue
            graficos.delete("all")
            return Seleccion().abrir_selector()


class Seleccion:  # Seleccionador de Niveles.

    def __init__(self):
        self.volver = Button(graficos, text="Volver al menu principal",
                             width=19, font=("Comic Sans MS", 15), bg=c_bg_fg,
                             fg=c_fg, activebackground=c_bg_press,
                             activeforeground=c_fg,
                             command=lambda: Menu().crear_menu())
        self.nivel_1 = Button(graficos, text="Nivel 1", width=17, height=2,
                              font=("Comic Sans MS", 20), bg=c_bg_fg, fg=c_fg,
                              activebackground=c_bg_press,
                              activeforeground=c_fg)
        self.nivel_2 = Button(graficos, text="Nivel 2", width=17, height=2,
                              font=("Comic Sans MS", 20), bg=c_bg_fg, fg=c_fg,
                              activebackground=c_bg_press,
                              activeforeground=c_fg)
        self.nivel_3 = Button(graficos, text="Nivel 3", width=17, height=2,
                              font=("Comic Sans MS", 20), bg=c_bg_fg, fg=c_fg,
                              activebackground=c_bg_press,
                              activeforeground=c_fg)
        self.nivel_4 = Button(graficos, text="Nivel 4", width=17, height=2,
                              font=("Comic Sans MS", 20), bg=c_bg_fg, fg=c_fg,
                              activebackground=c_bg_press,
                              activeforeground=c_fg)
        self.nivel_5 = Button(graficos, text="Nivel 5", width=17, height=2,
                              font=("Comic Sans MS", 20), bg=c_bg_fg, fg=c_fg,
                              activebackground=c_bg_press,
                              activeforeground=c_fg)
        self.nivel_6 = Button(graficos, text="Nivel 6", width=17, height=2,
                              font=("Comic Sans MS", 20), bg=c_bg_fg, fg=c_fg,
                              activebackground=c_bg_press,
                              activeforeground=c_fg)
        self.nivel_7 = Button(graficos, text="Nivel 7", width=17, height=2,
                              font=("Comic Sans MS", 20), bg=c_bg_fg, fg=c_fg,
                              activebackground=c_bg_press,
                              activeforeground=c_fg)
        self.nivel_8 = Button(graficos, text="Nivel 8", width=17, height=2,
                              font=("Comic Sans MS", 20), bg=c_bg_fg, fg=c_fg,
                              activebackground=c_bg_press,
                              activeforeground=c_fg)
        self.nivel_9 = Button(graficos, text="Nivel 9", width=17, height=2,
                              font=("Comic Sans MS", 20), bg=c_bg_fg, fg=c_fg,
                              activebackground=c_bg_press,
                              activeforeground=c_fg)

    def abrir_selector(self):
        # Fila 0
        graficos.create_window(ancho/8, 30, window=self.volver)
        # Fila 1
        graficos.create_window(ancho/5.5, alto/4.5, window=self.nivel_1)
        graficos.create_window(ancho/1.955, alto/4.5, window=self.nivel_2)
        graficos.create_window(ancho/1.20, alto/4.5, window=self.nivel_3)
        # Fila 2
        graficos.create_window(ancho/5.5, alto/2, window=self.nivel_4)
        graficos.create_window(ancho/1.955, alto/2, window=self.nivel_5)
        graficos.create_window(ancho/1.20, alto/2, window=self.nivel_6)
        # Fila 3
        graficos.create_window(ancho/5.5, alto/1.27, window=self.nivel_7)
        graficos.create_window(ancho/1.955, alto/1.27, window=self.nivel_8)
        graficos.create_window(ancho/1.20, alto/1.27, window=self.nivel_9)


jojer = Menu()
jojer.crear_menu()

# -- -- -- Mainloop
if __name__ == "__main__":
    root.mainloop()
