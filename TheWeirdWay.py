from tkinter import Canvas, Frame, Tk, PhotoImage, Button

# -- -- -- Titulo
titulo = "The Weird Way"
print("=" * len(titulo) + "\n" + titulo + "\n" + "=" * len(titulo), "\n")

# -- -- -- Variables e imagenes previas
# Tamaños
ancho = 1071
alto = 708

# Colores
c_fondo = "#1c1b20"  # Fondo del root
c_pantalla = "#26242b"  # Fondo del canvas "Graficos"
c_fg = "#e7e7e7"  # Todas las letras base
c_fg_win = "#615637"  # Letras de los niveles ganados
c_bg_se = "#1a1820"  # Color de cuadros de inicio
c_bg_no = "#1e1c24"  # Color de niveles bloqueados
c_bg_si = "#272430"  # Color de niveles desbloqueados
c_bg_press = "#1c1b20"  # Color de botones comúnes siendo presionados
c_bg_press_si = "#221f2a"  # Color de niveles desbloqueados siendo presionados
c_bg_win = "#d7b64c"  # Color de niveles superados
c_bg_press_win = "#cbab47"  # Color de niveles ganados siendo presionados

# Direcciones
all_p = ("xy")  # Cantidad de direcciones: 1
xy_p = ("x", "y")  # Cantidad de direcciones: 2
dos_p = ("ac", "bc", "bd", "ad")  # Cantidad de direcciones: 4
tres_p = ("abd", "acd", "abc", "bcd")  # Cantidad de direcciones: 4

# -- -- -- Root
root = Tk()
root.title(titulo)
root.resizable(False, False)
root.geometry("{}x{}+{}+{}".format(ancho, alto, 200, 45))
root.iconbitmap("LucioPalIco.ico")
root.config(bg=c_fondo)

# -- -- -- Imagenes
# A = Izquierda | B = Derecha | C = Arriba | D = Abajo
logo_img = PhotoImage(file="Imagenes/Logo.png")
menu_img = PhotoImage(file="Imagenes/Inicio3.png")
fondo_img = PhotoImage(file="Imagenes/Fondo6.png")
player_img = PhotoImage(file="Imagenes/Red_Skull2.png")
candado_img = PhotoImage(file="Imagenes/Candado2.png")

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

    def __init__(self):   # __init__ para cancelar la selecciones de puentes
        graficos.unbind("<Button-1>")

    def crear_menu(self):

        self.num = alto  # Reseteo del numerador de la animación de cerrado.
        self.imagen = graficos.create_image(ancho/2, alto/2, image=menu_img)

        self.logo2 = graficos.create_image(ancho/2, alto/2 - alto/4,
                                           image=logo_img)
        self.ani_menu = graficos.create_rectangle(-1, 0, ancho, 0,
                                                  fill=c_fondo,
                                                  outline="purple")

        self.nueva = Button(graficos, text="Nueva Partida", fg=c_fg,
                            cursor="hand2", font=("Century Gothic", 20),
                            bg=c_bg_no, width=30, activeforeground=c_fg,
                            activebackground=c_bg_se,
                            command=lambda: self.cerrar_menu("nueva"))

        self.continuar = Button(graficos, text="Continuar Partida", fg=c_fg,
                                cursor="hand2", font=("Century Gothic", 20),
                                bg=c_bg_no, width=27, activeforeground=c_fg,
                                activebackground=c_bg_se,
                                command=lambda: self.cerrar_menu("continuar"))

        self.salir = Button(graficos, text="Salir", fg=c_fg, cursor="hand2",
                            font=("Century Gothic", 20), bg=c_bg_no,
                            width=24, activeforeground=c_fg,
                            activebackground=c_bg_se,
                            command=lambda: self.cerrar_menu("salir"))

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
        self.num -= 50
        graficos.coords(self.ani_menu, -1, alto, ancho, self.num)

        if selected == "nueva":
            graficos.move(self.nueva2,     + 65, 0)
            graficos.move(self.continuar2, - 65, 0)
            graficos.move(self.salir2,     - 65, 0)
        elif selected == "continuar":
            graficos.move(self.nueva2,     - 65, 0)
            graficos.move(self.continuar2, + 65, 0)
            graficos.move(self.salir2,     - 65, 0)
        elif selected == "salir":
            graficos.move(self.nueva2,     - 65, 0)
            graficos.move(self.continuar2, - 65, 0)
            graficos.move(self.salir2,     + 65, 0)

        if self.num > -50:  # Bucle generado para repetír el método (Animación)
            root.after(60, lambda: self.cerrar_menu(selected))

        else:  # Acciones tras animación. Eliminación de todo.
            graficos.delete("all")
            if selected != "salir":
                return Seleccion().abrir_selector()
            else:
                root.destroy()


class Seleccion:  # Seleccionador de Niveles.

    def __init__(self):  # __init__ para cancelar la selecciones de puentes
        graficos.unbind("<Button-1>")

    def abrir_selector(self):
        self.volver = Button(graficos, text="Volver al menu principal",
                             width=19, font=("Comic Sans MS", 15),
                             bg=c_bg_se, fg=c_fg,
                             activebackground=c_bg_press,
                             activeforeground=c_fg, cursor="hand2",
                             command=lambda: self.cerrar_selector("0"))

        # Loop para generar los botones de los niveles:
        for nivel in ["self.nivel_1", "self.nivel_2", "self.nivel_3",
                      "self.nivel_4", "self.nivel_5", "self.nivel_6",
                      "self.nivel_7", "self.nivel_8", "self.nivel_9"]:

            exec("""{0} = Button(graficos, text='       Nivel {1} ',
                 width=276,font=('Comic Sans MS', 20),
                 bg=c_bg_se, fg=c_fg,
                 activebackground=c_bg_press,
                 activeforeground=c_fg, cursor='hand2')""".
                 format(nivel, nivel[-1]))

            if nivel != "self.nivel_1":
                exec("{}.config(image=candado_img, compound='right')"
                     .format(nivel))

        self.nivel_1.config(bg=c_bg_si, width=17, height=2, text="Nivel 1",
                            activebackground=c_bg_press_si,
                            command=lambda: self.cerrar_selector("1"))
        self.nivel_2.config(command=lambda: self.cerrar_selector("2"))
        self.nivel_3.config(command=lambda: self.cerrar_selector("3"))
        self.nivel_4.config(command=lambda: self.cerrar_selector("4"))
        self.nivel_5.config(command=lambda: self.cerrar_selector("5"))
        self.nivel_6.config(command=lambda: self.cerrar_selector("6"))
        self.nivel_7.config(command=lambda: self.cerrar_selector("7"))
        self.nivel_8.config(command=lambda: self.cerrar_selector("8"))
        self.nivel_9.config(command=lambda: self.cerrar_selector("9"))

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

        # Candados:
        # graficos.create_image(ancho/1.955, alto/4.5)

    def cerrar_selector(self, nivel):  # 0 = Menu | >= 1 y <=9 = X Nivel
        graficos.delete("all")
        del self.volver, self.nivel_1, self.nivel_2, self.nivel_3,
        self.nivel_4, self.nivel_5, self.nivel_6,
        self.nivel_7, self.nivel_8, self.nivel_9

        if nivel == "0":  # If por si se quiere volver al menu principal.
            return Menu().crear_menu()
        else:  # Else para activar la clase Partída con método para el nivel.
            for lvl in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
                if nivel == lvl:
                    exec('Partida().nivel_{0}()'.format(lvl))
                    break


class Partida:  # Ancho base = 154 | Alto base = 140

    def __init__(self):
        self.fondo = graficos.create_image(ancho/2, alto/2, image=fondo_img)
        self.player = graficos.create_image(154*0.25, 71*6,
                                            image=player_img)

    def giro(self, cursor):
        print("X = {}".format(cursor.x))
        print("Y = {}".format(cursor.y))

        if (cursor.x >= 70 and cursor.x <= 77 * 3 and
           cursor.y >= 70 * 3 and cursor.y <= 70 * 5):
            try:
                return self.cambio(self.puente21)
            except AttributeError:
                print("No hay cuadro 21")  # Hacer Loop para generar el click

    def cambio(self, dire):  # p = Posición
        if dire[1] in all_p:
            return dire

        elif dire[1] in xy_p:
            if dire[1] == "x":
                dire[1] = "y"
                graficos.itemconfig(dire[0], image=puente_y_img)
            elif dire[1] == "y":
                dire[1] = "x"
                graficos.itemconfig(dire[0], image=puente_x_img)
            return dire

        elif dire[1] in dos_p:
            if dire[1] == "ac":
                dire[1] = "bc"
                graficos.itemconfig(dire[0], image=puente_bc_img)
            elif dire[1] == "bc":
                dire[1] = "bd"
                graficos.itemconfig(dire[0], image=puente_bd_img)
            elif dire[1] == "bd":
                dire[1] = "ad"
                graficos.itemconfig(dire[0], image=puente_ad_img)
            elif dire[1] == "ad":
                dire[1] = "ac"
                graficos.itemconfig(dire[0], image=puente_ac_img)
            return dire

        elif dire[1] in tres_p:
            if dire[1] == "abd":
                dire[1] = "acd"
                graficos.itemconfig(dire[0], image=puente_acd_img)
            elif dire[1] == "acd":
                dire[1] = "abc"
                graficos.itemconfig(dire[0], image=puente_abc_img)
            elif dire[1] == "abc":
                dire[1] = "bcd"
                graficos.itemconfig(dire[0], image=puente_bcd_img)
            elif dire[1] == "bcd":
                dire[1] = "abd"
                graficos.itemconfig(dire[0], image=puente_abd_img)
            return dire

    def nivel_1(self):
        # for e in range(1, 4 + 1):
        #     for i in range(1, 6 + 1):
        #         graficos.create_image(154*int("{}".format(i)),
        #                               140*int("{}".format(e)),
        #                               image=puente_xy_img)

        self.puente21 = [graficos.create_image(154, 140*2,
                                               image=puente_acd_img),
                         "acd", "self.puente21"]
        self.puente32 = [graficos.create_image(154, 140*3,
                                               image=puente_y_img),
                         "y", "32"]
        self.puente22 = [graficos.create_image(154*2, 140*2,
                                               image=puente_bc_img),
                         "bc", "22"]
        self.puente32 = [graficos.create_image(154*2, 140*3,
                                               image=puente_bc_img),
                         "bc", "32"]
        self.puente23 = [graficos.create_image(154*3, 140*2,
                                               image=puente_y_img),
                         "y", "23"]
        self.puente24 = [graficos.create_image(154*4, 140*2,
                                               image=puente_bc_img),
                         "bc", "24"]
        self.puente23 = [graficos.create_image(154*4, 140*3,
                                               image=puente_ac_img),
                         "ac", "23"]
        self.puente35 = [graficos.create_image(154*5, 140*3,
                                               image=puente_y_img),
                         "y", "35"]
        self.puente36 = [graficos.create_image(154*6, 140*3,
                                               image=puente_ac_img),
                         "ac", "36"]
        self.puente26 = [graficos.create_image(154*6, 140*2,
                                               image=puente_x_img),
                         "x", "26"]
        self.puente16 = [(graficos.create_image(154*6, 140,
                                                image=puente_ad_img)),
                         "ad", "16"]

        graficos.lift(self.player)
        graficos.bind("<Button-1>", self.giro)  # Giro de los caminos


jojer = Menu()
jojer.crear_menu()

# -- -- -- Mainloop
if __name__ == "__main__":
    root.mainloop()
