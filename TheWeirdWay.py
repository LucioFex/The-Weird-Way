from tkinter import Canvas, Frame, Tk, PhotoImage, Button

# -- -- -- Titulo

titulo = "The Weird Way"
print("=" * len(titulo) + "\n" + titulo + "\n" + "=" * len(titulo), "\n")

# -- -- -- Variables e imagenes previas

# Tamaños

ancho = 1071
alto = 708

# Colores
c_fondo = "#1c1b20"
c_pantalla = "#26242b"
c_fg = "#8b64ed"
c_fg_win = "#615637"
c_bg_fg_no = "#222027"
c_bg_fg_si = "#272430"
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
fondo_img = PhotoImage(file="Imagenes/Fondo3.png")
player_img = PhotoImage(file="Imagenes/Red_Skull2.png")

puente_x_img = PhotoImage(file="Imagenes/PuenteX.png")  # X
puente_y_img = PhotoImage(file="Imagenes/PuenteY.png")  # Y
puente_xy_img = PhotoImage(file="Imagenes/PuenteXY.png")  # XY

puente_ac_img = PhotoImage(file="Imagenes/PuenteAC.png")  # AC
puente_ad_img = PhotoImage(file="Imagenes/PuenteAD.png")  # AD
puente_bc_img = PhotoImage(file="Imagenes/PuenteBC.png")  # BC
puente_bd_img = PhotoImage(file="Imagenes/PuenteBD.png")  # BD

puente_abc_img = PhotoImage(file="Imagenes/PuenteABC.png")  # ABC
puente_abd_img = PhotoImage(file="Imagenes/PuenteABD.png")  # ABD
puente_acd_img = PhotoImage(file="Imagenes/PuenteACD.png")  # ACD
puente_bcd_img = PhotoImage(file="Imagenes/PuenteBCD.png")  # BCD

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

        self.num = alto  # Reseteo del numerador de la animación de cerrado.
        self.ani_menu = graficos.create_rectangle(-1, 0, ancho, 0,
                                                  fill=c_fondo,
                                                  outline="purple")

        self.nueva = Button(graficos, text="Nueva Partida", fg=c_fg,
                            cursor="hand2", font=("Century Gothic", 20),
                            bg=c_bg_fg_no, width=30, activeforeground=c_fg,
                            activebackground=c_bg_press,
                            command=lambda: self.cerrar_menu("nueva"))

        self.continuar = Button(graficos, text="Continuar Partida", fg=c_fg,
                                cursor="hand2", font=("Century Gothic", 20),
                                bg=c_bg_fg_no, width=27, activeforeground=c_fg,
                                activebackground=c_bg_press,
                                command=lambda: self.cerrar_menu("continuar"))

        self.salir = Button(graficos, text="Salir", fg=c_fg, cursor="hand2",
                            font=("Century Gothic", 20), bg=c_bg_fg_no,
                            width=24, activeforeground=c_fg,
                            activebackground=c_bg_press,
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
        # Animaciones:
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
            graficos.delete("all")
            if selected != "salir":
                return Seleccion().abrir_selector()
            else:
                root.destroy()


class Seleccion:  # Seleccionador de Niveles.

    def abrir_selector(self):

        self.volver = Button(graficos, text="Volver al menu principal",
                             width=19, font=("Comic Sans MS", 15),
                             bg=c_bg_fg_no, fg=c_fg,
                             activebackground=c_bg_press,
                             activeforeground=c_fg, cursor="hand2",
                             command=lambda: self.cerrar_selector("0"))
        self.nivel_1 = Button(graficos, text="Nivel 1", width=17, height=2,
                              font=("Comic Sans MS", 20), bg=c_bg_fg_si,
                              fg=c_fg, activebackground=c_bg_press,
                              activeforeground=c_fg, cursor="hand2",
                              command=lambda: self.cerrar_selector("1"))
        self.nivel_2 = Button(graficos, text="Nivel 2", width=17, height=2,
                              font=("Comic Sans MS", 20), bg=c_bg_fg_no,
                              fg=c_fg, activebackground=c_bg_press,
                              activeforeground=c_fg, cursor="hand2",
                              command=lambda: self.cerrar_selector("2"))
        self.nivel_3 = Button(graficos, text="Nivel 3", width=17, height=2,
                              font=("Comic Sans MS", 20), bg=c_bg_fg_no,
                              fg=c_fg, activebackground=c_bg_press,
                              activeforeground=c_fg, cursor="hand2",
                              command=lambda: self.cerrar_selector("3"))
        self.nivel_4 = Button(graficos, text="Nivel 4", width=17, height=2,
                              font=("Comic Sans MS", 20), bg=c_bg_fg_no,
                              fg=c_fg, activebackground=c_bg_press,
                              activeforeground=c_fg, cursor="hand2",
                              command=lambda: self.cerrar_selector("4"))
        self.nivel_5 = Button(graficos, text="Nivel 5", width=17, height=2,
                              font=("Comic Sans MS", 20), bg=c_bg_fg_no,
                              fg=c_fg, activebackground=c_bg_press,
                              activeforeground=c_fg, cursor="hand2",
                              command=lambda: self.cerrar_selector("5"))
        self.nivel_6 = Button(graficos, text="Nivel 6", width=17, height=2,
                              font=("Comic Sans MS", 20), bg=c_bg_fg_no,
                              fg=c_fg, activebackground=c_bg_press,
                              activeforeground=c_fg, cursor="hand2",
                              command=lambda: self.cerrar_selector("6"))
        self.nivel_7 = Button(graficos, text="Nivel 7", width=17, height=2,
                              font=("Comic Sans MS", 20), bg=c_bg_fg_no,
                              fg=c_fg, activebackground=c_bg_press,
                              activeforeground=c_fg, cursor="hand2",
                              command=lambda: self.cerrar_selector("7"))
        self.nivel_8 = Button(graficos, text="Nivel 8", width=17, height=2,
                              font=("Comic Sans MS", 20), bg=c_bg_fg_no,
                              fg=c_fg, activebackground=c_bg_press,
                              activeforeground=c_fg, cursor="hand2",
                              command=lambda: self.cerrar_selector("8"))
        self.nivel_9 = Button(graficos, text="Nivel 9", width=17, height=2,
                              font=("Comic Sans MS", 20), bg=c_bg_fg_no,
                              fg=c_fg, activebackground=c_bg_press,
                              activeforeground=c_fg, cursor="hand2",
                              command=lambda: self.cerrar_selector("9"))
        # ---------------------------------------------------------------------
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

    def cerrar_selector(self, nivel):  # 0 = Menu | >= 1 y <=9 = X nivel
        graficos.delete("all")
        del self.volver, self.nivel_1, self.nivel_2, self.nivel_3,
        self.nivel_4, self.nivel_5, self.nivel_6,
        self.nivel_7, self.nivel_8, self.nivel_9

        if nivel == "0":  # If por si se quiere volver al menu principal.
            return Menu().crear_menu()
        else:  # Else para activar la clase Partída con método para el nivel.
            for lvl in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
                if nivel == lvl:
                    exec('Partida().nivel_{0}("init")'.format(lvl))
                    break


class Partida:  # Ancho base = 76 * | Alto base = 71 *

    def __init__(self):
        self.fondo = graficos.create_image(ancho/2, alto/2, image=fondo_img)
        self.player = graficos.create_image(45, 71*6,
                                            image=player_img)

    def nivel_1(self, act):  # "init" = Crear | "game" = Acción del juego
        if act == "init":
            self.puente1 = [graficos.create_image(153, 140*2,
                                                  image=puente_acd_img), "acd"]
            self.puente2 = [graficos.create_image(153, 140*3,
                                                  image=puente_y_img), "y"]
            self.puente3 = [graficos.create_image(153*2, 140*2,
                                                  image=puente_xy_img), "xy"]
            self.puente4 = [graficos.create_image(153*2, 140*3,
                                                  image=puente_bc_img), "bc"]
            self.puente5 = [graficos.create_image(153*3, 140*3,
                                                  image=puente_y_img), "y"]
            self.puente6 = [graficos.create_image(153*4, 140*2,
                                                  image=puente_bc_img), "bc"]
            self.puente5 = [graficos.create_image(153*4, 140*6,
                                                  image=puente_ac_img), "ac"]
            self.puente5 = [graficos.create_image(153*5, 140*3,
                                                  image=puente_y_img), "y"]
            self.puente5 = [graficos.create_image(153*6, 140*3,
                                                  image=puente_ac_img), "ac"]
            self.puente5 = [graficos.create_image(153*6, 140*2,
                                                  image=puente_x_img), "x"]
            self.puente5 = [graficos.create_image(153*6, 140,
                                                  image=puente_ad_img), "ad"]

        graficos.lift(self.player)


jojer = Menu()
jojer.crear_menu()

# -- -- -- Mainloop
if __name__ == "__main__":
    root.mainloop()
