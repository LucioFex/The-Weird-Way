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
c_bg_press = "#1a1920"  # Color de botones comúnes siendo presionados
c_bg_press_si = "#221f2a"  # Color de niveles desbloqueados siendo presionados
c_bg_win = "#d7b64c"  # Color de niveles superados
c_bg_press_win = "#cbab47"  # Color de niveles ganados siendo presionados

# Direcciones
all_p = ("f1ll", "f2ll", "f3ll", "f4ll")  # Cantidad de direcciones: 4
xy_p = ("x", "y")  # Cantidad de direcciones: 2
dos_p = ("ac", "bc", "bd", "ad")  # Cantidad de direcciones: 4
tres_p = ("abd", "acd", "abc", "bcd")  # Cantidad de direcciones: 4

# Extras
maximo = 1  # Mayor nivel alcanzado en el regístro del juego

# -- -- -- Root
root = Tk()
root.title(titulo)
root.resizable(False, False)
root.geometry("{}x{}+{}+{}".format(ancho, alto, 200, 45))
root.iconbitmap("LucioPalIco.ico")
root.config(bg=c_fondo)

# -- -- -- Imagenes
# A = Izquierda | B = Derecha | C = Arriba | D = Abajo
logo_im = PhotoImage(file="Imagenes/Logo.png")
menu_im = PhotoImage(file="Imagenes/Inicio5.png")  # Fondo Menu
selec_im = PhotoImage(file="Imagenes/Selector.png") # Fondo Selector
fondo_im = PhotoImage(file="Imagenes/Fondo12.png")  # Escenario del juego
player_im = PhotoImage(file="Imagenes/Red_Skull2.png")
candado_im = PhotoImage(file="Imagenes/Candado2.png")
# -- -- Botones In-Game
home_im = PhotoImage(file="Imagenes/Retorno_Menu.png")  # Regreso al menu
walk0_im = PhotoImage(file="Imagenes/Moverse0.png")  # Caminar desactivado
walk1_im = PhotoImage(file="Imagenes/Moverse1.png")  # Caminar sin | punto |
walk2_im = PhotoImage(file="Imagenes/Moverse2.png")  # Caminar con | punto |
# -- -- Puentes giratorios
puente_x_im = PhotoImage(file="Imagenes/PuenteX.png")  # X
puente_y_im = PhotoImage(file="Imagenes/PuenteY.png")  # Y
puente_f1ll_im = PhotoImage(file="Imagenes/PuenteF1LL.png")  # XY
puente_f2ll_im = PhotoImage(file="Imagenes/PuenteF2LL.png")  # XY
puente_f3ll_im = PhotoImage(file="Imagenes/PuenteF3LL.png")  # XY
puente_f4ll_im = PhotoImage(file="Imagenes/PuenteF4LL.png")  # XY

puente_ac_im = PhotoImage(file="Imagenes/PuenteAC.png")  # AC
puente_ad_im = PhotoImage(file="Imagenes/PuenteAD.png")  # AD
puente_bc_im = PhotoImage(file="Imagenes/PuenteBC.png")  # BC
puente_bd_im = PhotoImage(file="Imagenes/PuenteBD.png")  # BD

puente_abc_im = PhotoImage(file="Imagenes/PuenteABC.png")  # ABC
puente_abd_im = PhotoImage(file="Imagenes/PuenteABD.png")  # ABD
puente_acd_im = PhotoImage(file="Imagenes/PuenteACD.png")  # ACD
puente_bcd_im = PhotoImage(file="Imagenes/PuenteBCD.png")  # BCD
# -- -- Puentes no giratorios
puente_x2_im = PhotoImage(file="Imagenes/PuenteX2.png")  # X
puente_y2_im = PhotoImage(file="Imagenes/PuenteY2.png")  # Y
puente_f1ll2_im = PhotoImage(file="Imagenes/PuenteF1LL2.png")  # XY

puente_ac2_im = PhotoImage(file="Imagenes/PuenteAC2.png")  # AC
puente_ad2_im = PhotoImage(file="Imagenes/PuenteAD2.png")  # AD
puente_bc2_im = PhotoImage(file="Imagenes/PuenteBC2.png")  # BC
puente_bd2_im = PhotoImage(file="Imagenes/PuenteBD2.png")  # BD

puente_abc2_im = PhotoImage(file="Imagenes/PuenteABC2.png")  # ABC
puente_abd2_im = PhotoImage(file="Imagenes/PuenteABD2.png")  # ABD
puente_acd2_im = PhotoImage(file="Imagenes/PuenteACD2.png")  # ACD
puente_bcd2_im = PhotoImage(file="Imagenes/PuenteBCD2.png")  # BCD

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
        self.imagen = graficos.create_image(ancho/2, alto/2, image=menu_im)
        self.logo2 = graficos.create_image(ancho/2, alto/2 - alto/4,
                                           image=logo_im)
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

    def abrir_selector(self, desbloqueados=7):  # Predeterminado: 1
        global maximo
        if desbloqueados >= maximo:  # Guardado del nivel aumentado
            maximo = desbloqueados

        self.volver = Button(graficos, text="Volver al menu principal",
                             width=19, font=("Comic Sans MS", 15),
                             bg=c_bg_se, fg=c_fg,
                             activebackground=c_bg_press,
                             activeforeground=c_fg, cursor="hand2",
                             command=lambda: self.cerrar_selec("0"))

        # Loop para generar los botones de los niveles:
        for nivel in ("self.nivel_1", "self.nivel_2", "self.nivel_3",
                      "self.nivel_4", "self.nivel_5", "self.nivel_6",
                      "self.nivel_7", "self.nivel_8", "self.nivel_9"):
            # Botones generandose
            exec("""{0} = Button(graficos, text='       Nivel {1} ',
                 width=276,font=('Comic Sans MS', 20),
                 bg=c_bg_se, fg=c_fg,
                 activebackground=c_bg_press,
                 activeforeground=c_fg, cursor='hand2')""".
                 format(nivel, nivel[-1]))
            # Botones seleccionables dependiendo de los niveles desbloqueados
            if int(nivel[-1]) <= maximo:
                exec("""{0}.config(command=lambda: self.cerrar_selec('{0}'),
                    activebackground=c_bg_press_si, bg=c_bg_si,
                    width=17, height=2, text="Nivel {1}")"""
                     .format(nivel, nivel[-1]))
            # Botones bloqueados por niveles injugables
            else:
                exec("{}.config(image=candado_im, compound='right')"
                     .format(nivel))

        # Solución con IFs (solo para corto plazo)
        if maximo >= 1:
            self.nivel_1.config(command=lambda: self.cerrar_selec("1"))
        if maximo >= 2:
            self.nivel_2.config(command=lambda: self.cerrar_selec("2"))
        if maximo >= 3:
            self.nivel_3.config(command=lambda: self.cerrar_selec("3"))
        if maximo >= 4:
            self.nivel_4.config(command=lambda: self.cerrar_selec("4"))
        if maximo >= 5:
            self.nivel_5.config(command=lambda: self.cerrar_selec("5"))
        if maximo >= 6:
            self.nivel_6.config(command=lambda: self.cerrar_selec("6"))
        if maximo >= 7:
            self.nivel_7.config(command=lambda: self.cerrar_selec("7"))
        if maximo >= 8:
            self.nivel_8.config(command=lambda: self.cerrar_selec("8"))
        if maximo >= 9:
            self.nivel_9.config(command=lambda: self.cerrar_selec("9"))
        # ---------------------------------------------------------------------
        # Fondo
        graficos.create_image(ancho/2, alto/2, image=selec_im)
        # Fila 0
        graficos.create_window(ancho/8, 30, window=self.volver)
        # Fila 1
        graficos.create_window((ancho/5.5), (alto/4.5), window=self.nivel_1)
        graficos.create_window((ancho/1.955), (alto/4.5), window=self.nivel_2)
        graficos.create_window((ancho/1.20), (alto/4.5), window=self.nivel_3)
        # Fila 2
        graficos.create_window((ancho/5.5), (alto/2), window=self.nivel_4)
        graficos.create_window((ancho/1.955), (alto/2), window=self.nivel_5)
        graficos.create_window((ancho/1.20), (alto/2), window=self.nivel_6)
        # Fila 3
        graficos.create_window((ancho/5.5), (alto/1.27), window=self.nivel_7)
        graficos.create_window((ancho/1.955), (alto/1.27), window=self.nivel_8)
        graficos.create_window((ancho/1.20), (alto/1.27), window=self.nivel_9)

    def cerrar_selec(self, nivel):  # 0 = Menu | >= 1 y <=9 = X Nivel
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


class Partida:  # Ancho base = 154.5 (77 X) | Alto base = 140 (140 Y)

    def __init__(self):
        self.fondo = graficos.create_image(ancho/2, alto/2, image=fondo_im)
        self.player = graficos.create_image(-100, -100,
                                            image=player_im)
        self.home = Button(graficos, font=("Century Gothic", 15),
                           bd=0, highlightthickness=0, image=home_im,
                           activebackground='#23272d',
                           cursor="hand2", command=self.regresar)

        self.walk = Button(graficos, font=("Century Gothic", 15),
                           bd=0, highlightthickness=0, image=walk0_im,
                           activebackground='#23272d', cursor="hand2")

        graficos.create_window(35, 35, window=self.home)  # Botón de regreso
        graficos.create_window(1035, 35, window=self.walk)  # Botón de caminar
        graficos.bind("<Button-1>", self.giro)  # Giro de los caminos

    def giro(self, cursor):
        # Condicionales a corto plazo, tratar de depurarlo con bucles o algo.

        if (cursor.x >= 17.5 and cursor.x < 52.5 and  # HOME (Regreso al menu)
                cursor.y >= 17.5 and cursor.y < 52.5):
            return self.regresar()
        # ---------------------- Cuadros ----------------------
        if (cursor.x >= 77 and cursor.x < 77 * 3 and  # Cuadro 11
                cursor.y >= 69 and cursor.y < 69 * 3):
            try:
                return self.cambio(self.puente11)
            except AttributeError:
                print("No hay cuadro 11")

        elif (cursor.x >= 77 and cursor.x < 77 * 3 and  # Cuadro 21
              cursor.y >= 69 * 3 and cursor.y < 69 * 5):
            try:
                return self.cambio(self.puente21)
            except AttributeError:
                print("No hay cuadro 21")

        elif (cursor.x >= 77 and cursor.x < 77 * 3 and  # Cuadro 31
              cursor.y >= 69 * 5 and cursor.y < 69 * 7):
            try:
                return self.cambio(self.puente31)
            except AttributeError:
                print("No hay cuadro 31")

        elif (cursor.x >= 77 and cursor.x < 77 * 3 and  # Cuadro 41
              cursor.y >= 69 * 7 and cursor.y < (69 * 9) + 11):
            try:
                return self.cambio(self.puente41)
            except AttributeError:
                print("No hay cuadro 41")

        elif (cursor.x >= 77 * 3 and cursor.x < 77 * 5 and  # Cuadro 12
              cursor.y >= 69 and cursor.y < 69 * 3):
            try:
                return self.cambio(self.puente12)
            except AttributeError:
                print("No hay cuadro 12")

        elif (cursor.x >= 77 * 3 and cursor.x < 77 * 5 and  # Cuadro 22
              cursor.y >= 69 * 3 and cursor.y < 69 * 5):
            try:
                return self.cambio(self.puente22)
            except AttributeError:
                print("No hay cuadro 22")

        elif (cursor.x >= 77 * 3 and cursor.x < 77 * 5 and  # Cuadro 32
              cursor.y >= 69 * 5 and cursor.y < 69 * 7):
            try:
                return self.cambio(self.puente32)
            except AttributeError:
                print("No hay cuadro 32")

        elif (cursor.x >= 77 * 3 and cursor.x < 77 * 5 and  # Cuadro 42
              cursor.y >= 69 * 7 and cursor.y < (69 * 9) + 11):
            try:
                return self.cambio(self.puente42)
            except AttributeError:
                print("No hay cuadro 42")

        elif (cursor.x >= 77 * 5 and cursor.x < 77 * 7 and  # Cuadro 13
              cursor.y >= 69 and cursor.y < 69 * 3):
            try:
                return self.cambio(self.puente13)
            except AttributeError:
                print("No hay cuadro 13")

        elif (cursor.x >= 77 * 5 and cursor.x < 77 * 7 and  # Cuadro 23
              cursor.y >= 69 * 3 and cursor.y < 69 * 5):
            try:
                return self.cambio(self.puente23)
            except AttributeError:
                print("No hay cuadro 23")

        elif (cursor.x >= 77 * 5 and cursor.x < 77 * 7 and  # Cuadro 33
              cursor.y >= 69 * 5 and cursor.y < 69 * 7):
            try:
                return self.cambio(self.puente33)
            except AttributeError:
                print("No hay cuadro 33")

        elif (cursor.x >= 77 * 5 and cursor.x < 77 * 7 and  # Cuadro 43
              cursor.y >= 69 * 7 and cursor.y < (69 * 9) + 11):
            try:
                return self.cambio(self.puente43)
            except AttributeError:
                print("No hay cuadro 43")

        elif (cursor.x >= 77 * 7 and cursor.x < 77 * 9 and  # Cuadro 14
              cursor.y >= 69 and cursor.y < 69 * 3):
            try:
                return self.cambio(self.puente14)
            except AttributeError:
                print("No hay cuadro 14")

        elif (cursor.x >= 77 * 7 and cursor.x < 77 * 9 and  # Cuadro 24
              cursor.y >= 69 * 3 and cursor.y < 69 * 5):
            try:
                return self.cambio(self.puente24)
            except AttributeError:
                print("No hay cuadro 24")

        elif (cursor.x >= 77 * 7 and cursor.x < 77 * 9 and  # Cuadro 34
              cursor.y >= 69 * 5 and cursor.y < 69 * 7):
            try:
                return self.cambio(self.puente34)
            except AttributeError:
                print("No hay cuadro 34")

        elif (cursor.x >= 77 * 7 and cursor.x < 77 * 9 and  # Cuadro 44
              cursor.y >= 69 * 7 and cursor.y < (69 * 9) + 11):
            try:
                return self.cambio(self.puente44)
            except AttributeError:
                print("No hay cuadro 44")

        elif (cursor.x >= 77 * 9 and cursor.x < 77 * 11 and  # Cuadro 15
              cursor.y >= 69 and cursor.y < 69 * 3):
            try:
                return self.cambio(self.puente15)
            except AttributeError:
                print("No hay cuadro 15")

        elif (cursor.x >= 77 * 9 and cursor.x < 77 * 11 and  # Cuadro 25
              cursor.y >= 69 * 3 and cursor.y < 69 * 5):
            try:
                return self.cambio(self.puente25)
            except AttributeError:
                print("No hay cuadro 25")

        elif (cursor.x >= 77 * 9 and cursor.x < 77 * 11 and  # Cuadro 35
              cursor.y >= 69 * 5 and cursor.y < 69 * 7):
            try:
                return self.cambio(self.puente35)
            except AttributeError:
                print("No hay cuadro 35")

        elif (cursor.x >= 77 * 9 and cursor.x < 77 * 11 and  # Cuadro 45
              cursor.y >= 69 * 7 and cursor.y < (69 * 9) + 11):
            try:
                return self.cambio(self.puente45)
            except AttributeError:
                print("No hay cuadro 45")

        elif (cursor.x >= 77 * 11 and cursor.x < 77 * 13 and  # Cuadro 16
              cursor.y >= 69 and cursor.y < 69 * 3):
            try:
                return self.cambio(self.puente16)
            except AttributeError:
                print("No hay cuadro 16")

        elif (cursor.x >= 77 * 11 and cursor.x < 77 * 13 and  # Cuadro 26
              cursor.y >= 69 * 3 and cursor.y < 69 * 5):
            try:
                return self.cambio(self.puente26)
            except AttributeError:
                print("No hay cuadro 26")

        elif (cursor.x >= 77 * 11 and cursor.x < 77 * 13 and  # Cuadro 36
              cursor.y >= 69 * 5 and cursor.y < 69 * 7):
            try:
                return self.cambio(self.puente36)
            except AttributeError:
                print("No hay cuadro 36")

        elif (cursor.x >= 77 * 11 and cursor.x < 77 * 13 and  # Cuadro 46
              cursor.y >= 69 * 7 and cursor.y < (69 * 9) + 11):
            try:
                return self.cambio(self.puente46)
            except AttributeError:
                print("No hay cuadro 46")

    def cambio(self, dire):  # p = Posición de los puentes

        if dire[1] in all_p:
            if dire[1] == "f1ll":
                dire[1] = "f2ll"
                graficos.itemconfig(dire[0], image=puente_f2ll_im)
            elif dire[1] == "f2ll":
                dire[1] = "f3ll"
                graficos.itemconfig(dire[0], image=puente_f3ll_im)
            elif dire[1] == "f3ll":
                dire[1] = "f4ll"
                graficos.itemconfig(dire[0], image=puente_f4ll_im)
            elif dire[1] == "f4ll":
                dire[1] = "f1ll"
                graficos.itemconfig(dire[0], image=puente_f1ll_im)

        if dire[1] in xy_p:  # X | Y
            if dire[1] == "x":
                dire[1] = "y"
                graficos.itemconfig(dire[0], image=puente_y_im)
            elif dire[1] == "y":
                dire[1] = "x"
                graficos.itemconfig(dire[0], image=puente_x_im)

        elif dire[1] in dos_p:  # AC | BC | BD | AD
            if dire[1] == "ac":
                dire[1] = "bc"
                graficos.itemconfig(dire[0], image=puente_bc_im)
            elif dire[1] == "bc":
                dire[1] = "bd"
                graficos.itemconfig(dire[0], image=puente_bd_im)
            elif dire[1] == "bd":
                dire[1] = "ad"
                graficos.itemconfig(dire[0], image=puente_ad_im)
            elif dire[1] == "ad":
                dire[1] = "ac"
                graficos.itemconfig(dire[0], image=puente_ac_im)

        elif dire[1] in tres_p:  # ABD | ACD | ABC | BCD
            if dire[1] == "abd":
                dire[1] = "acd"
                graficos.itemconfig(dire[0], image=puente_acd_im)
            elif dire[1] == "acd":
                dire[1] = "abc"
                graficos.itemconfig(dire[0], image=puente_abc_im)
            elif dire[1] == "abc":
                dire[1] = "bcd"
                graficos.itemconfig(dire[0], image=puente_bcd_im)
            elif dire[1] == "bcd":
                dire[1] = "abd"
                graficos.itemconfig(dire[0], image=puente_abd_im)
        # -- -- -- Niveles Ganados
        # -- Nivel 1 Ganado:
        if (self.piso == 1 and self.puente31[1] == "x"
            and self.puente22[1] == "bd" and self.puente32[1] == "ac"
            and self.puente23[1] == "x" and self.puente24[1] == "ad"
            and self.puente34[1] == "bc" and self.puente35[1] == "x"
            and self.puente36[1] == "ac" and self.puente26[1] == "y"
                and self.puente16[1] == "bd"):
            self.paso = [0, 1, 4, 1, 1, 3, 1, 1, 4, 4, 1, 1, 1]
            self.walk.config(image=walk1_im,
                             command=lambda: self.mov_animacion(1, self.paso))
        # -- Nivel 2 Ganado:
        elif (self.piso == 2 and self.puente11[1] == "bd"
              and self.puente21[1] == "ac" and self.puente22[1] == "y"
              and self.puente32[1] == "bc" and self.puente33[1] == "f1ll"
              and self.puente25[1] == "x" and self.puente25[1] == "x"
              and self.puente24[1] == "bd" and self.puente26[1] == "ad"
              and self.puente36[1] == "bc" and (self.puente12[1] == "abd"
              or self.puente12[1] == "acd") and (self.puente34[1] == "abc"
              or self.puente34[1] == "acd")):

            self.paso = [0, 4, 1, 3, 3, 1, 1, 4, 1, 1, 3, 1, 1, 1]
            self.walk.config(image=walk2_im,
                             command=lambda:
                             self.mov_animacion(2, self.paso))

        elif (self.piso == 2 and self.puente11[1] == "bd"
              and self.puente21[1] == "ac" and self.puente24[1] == "bc"
              and self.puente25[1] == "x" and self.puente26[1] == "ad"
              and self.puente36[1] == "bc" and (self.puente12[1] == "abd"
              or self.puente12[1] == "abc")):

            self.paso = [0, 4, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1]
            self.walk.config(image=walk1_im,
                             command=lambda:
                             self.mov_animacion(2, self.paso))

        # -- Nivel 3 Ganado:
        elif (self.piso == 3 and self.puente31[1] == "x"  # (Punto)
              and self.puente32[1] == "ad" and self.puente43[1] == "x"
              and self.puente44[1] == "x" and self.puente45[1] == "ac"
              and self.puente35[1] == "ad" and self.puente33[1] == "bc"
              and self.puente23[1] == "y" and self.puente13[1] == "bd"
              and self.puente14[1] == "x" and self.puente15[1] == "x"
              and self.puente16[1] == "ad" and self.puente26[1] == "bc"
              and (self.puente42[1] == "abc" or self.puente42[1] == "bcd")):

            self.paso = [0, 1, 3, 1, 1, 1, 4, 2, 2, 4, 4, 1, 1, 1, 3, 1, 1, 1]
            self.walk.config(image=walk2_im,
                             command=lambda:
                             self.mov_animacion(3, self.paso))

        elif (self.piso == 3 and self.puente31[1] == "x"
              and self.puente32[1] == "ad" and self.puente43[1] == "x"
              and self.puente44[1] == "x" and self.puente45[1] == "ac"
              and self.puente35[1] == "bd" and self.puente26[1] == "bd"
              and (self.puente42[1] == "abc" or self.puente42[1] == "bcd")):

            self.paso = [0, 1, 3, 1, 1, 1, 4, 1, 4, 1, 1, 1]
            self.walk.config(image=walk1_im,
                             command=lambda:
                             self.mov_animacion(3, self.paso))

        # -- Nivel 4 Ganado:
        elif (self.piso == 4 and self.puente31[1] == "ac"
              and self.puente22[1] == "x" and self.puente23[1] == "ac"
              and self.puente13[1] == "bd" and self.puente15[1] == "x"
              and self.puente16[1] == "ad" and self.puente26[1] == "y"):

            self.paso = [0, 4, 1, 1, 4, 1, 1, 1, 3, 3, 1, 1, 1]
            self.walk.config(image=walk2_im,
                             command=lambda:
                             self.mov_animacion(4, self.paso))  # PUNTO

        elif (self.piso == 4 and self.puente31[1] == "ad"
                and self.puente42[1] == "x" and self.puente43[1] == "x"
                and self.puente44[1] == "ac" and self.puente35[1] == "x"):

            self.paso = [0, 3, 1, 1, 1, 4, 1, 1, 1, 1]
            self.walk.config(image=walk1_im,
                             command=lambda:
                             self.mov_animacion(4, self.paso))
        # -- Nivel 5 Ganado:
        elif (self.piso == 5 and self.puente11[1] == "ad"
              and self.puente32[1] == "x" and self.puente33[1] == "ac"
              and self.puente23[1] == "ad" and self.puente22[1] == "bc"
              and self.puente14[1] == "x" and self.puente16[1] == "ad"
              and (self.puente31[1] == "abc" or self.puente31[1] == "bcd")
              and (self.puente13[1] == "abd" or self.puente13[1] == "abc")):

            self.paso = [0, 3, 3, 1, 1, 4, 2, 4, 1, 1, 1, 1, 3, 1, 1, 1]
            self.walk.config(image=walk2_im,
                             command=lambda:
                             self.mov_animacion(5, self.paso))  # PUNTO

        elif (self.piso == 5 and self.puente11[1] == "ad"
              and self.puente32[1] == "x" and self.puente33[1] == "ac"
              and self.puente23[1] == "bd" and self.puente24[1] == "x"
              and self.puente25[1] == "x" and (self.puente31[1] == "abc"
              or self.puente31[1] == "bcd")):

            self.paso = [0, 3, 3, 1, 1, 4, 1, 1, 1, 1, 1, 1]
            self.walk.config(image=walk1_im,
                             command=lambda:
                             self.mov_animacion(5, self.paso))

        # -- Nivel 6 Ganado:
        elif (self.piso == 6 and self.puente21[1] == "ad"
              and self.puente41[1] == "bc" and self.puente42[1] == "x"
              and self.puente43[1] == "x" and (self.puente45[1] == "abc"
              or self.puente45[1] == "abd") and (self.puente36[1] == "bcd"
              or self.puente36[1] == "abd")):

            self.paso = [0, 3, 3, 1, 1, 1, 1, 1, 4, 1, 1, 1]
            self.walk.config(image=walk1_im,
                             command=lambda:
                             self.mov_animacion(6, self.paso))

        elif (self.piso == 6 and self.puente11[1] == "bd"  # (Punto)
              and self.puente21[1] == "ac" and self.puente22[1] == "bc"
              and self.puente34[1] == "bc" and self.puente35[1] == "x"
              and (self.puente36[1] == "abc" or self.puente36[1] == "abd")):

            self.paso = [0, 4, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1]
            self.walk.config(image=walk2_im,
                             command=lambda:
                             self.mov_animacion(6, self.paso))

        # -- Nivel 7 Ganado:
        elif (self.piso == 7 and self.puente21[1] == "bd"  # (Punto)
              and self.puente31[1] == "y" and self.puente41[1] == "ac"
              and self.puente23[1] == "ad" and self.puente33[1] == "bc"
              and self.puente14[1] == "bd" and self.puente24[1] == "y"
              and self.puente15[1] == "ad" and self.puente25[1] == "bc"):
            self.paso = [0, 4, 4, 1, 1, 3, 1, 4, 4, 1, 3, 1, 1, 1, 1]
            self.walk.config(image=walk2_im,
                             command=lambda:
                             self.mov_animacion(7, self.paso))

        elif (self.piso == 7 and self.puente21[1] == "bd"
              and self.puente31[1] == "y" and self.puente41[1] == "ac"
              and self.puente42[1] == "bc" and self.puente23[1] == "ad"
              and self.puente33[1] == "ac" and self.puente43[1] == "x"
              and self.puente44[1] == "x" and self.puente25[1] == "bd"
              and self.puente35[1] == "y"):
            self.paso = [0, 4, 4, 1, 1, 3, 2, 3, 1, 1, 1, 4, 4, 1, 1, 1, 1]
            self.walk.config(image=walk1_im,
                             command=lambda:
                             self.mov_animacion(7, self.paso))

        else:  # Desabilitación del botón de PLAY (walk)
            self.walk.config(image=walk0_im, command=lambda: None)

    def mov_personaje(self, direccion, iter=0):  # iter = Iteraciones
        # 1 = DER | 2 = IZQ | 3 = ABA | 4 = ARR | 0 = Primer DER #
        if iter == 13:
            return None
        else:
            graficos.move(self.player, 9, 0) if direccion == 0 else None
            graficos.move(self.player, 11.9, 0) if direccion == 1 else None
            graficos.move(self.player, -11.9, 0) if direccion == 2 else None
            graficos.move(self.player, 0, 10.7) if direccion == 3 else None
            graficos.move(self.player, 0, -10.7) if direccion == 4 else None

            graficos.update()
            graficos.after(25, lambda: self.mov_personaje(direccion, iter+1))

    def mov_animacion(self, nivel, paso, camino=1):  # Animación del char
        graficos.unbind("<Button-1>")
        self.walk.config(command=lambda: None)
        self.home.config(command=lambda: None)
        try:  # Forma de chequear si la lista esta vacía o no:
            self.mov_personaje(paso[0])
        except IndexError:  # Si esta vacía, se termino la animación:
            return self.regresar(nivel + 1)

        paso.pop(0)
        graficos.after(415, lambda: self.mov_animacion(nivel, paso, camino))

    def nivel_1(self):  # --- --- --- --- 11 Puentes

        self.piso = 1
        graficos.coords(self.player, 154.5*0.25, 140*3)

        self.puente21 = [graficos.create_image(154.5, 140*2,
                                               image=puente_bd_im), "bd"]
        self.puente31 = [graficos.create_image(154.5, 140*3,
                                               image=puente_y_im), "y"]
        self.puente22 = [graficos.create_image(154.5*2, 140*2,
                                               image=puente_bc_im), "bc"]
        self.puente32 = [graficos.create_image(154.5*2, 140*3,
                                               image=puente_bc_im), "bc"]
        self.puente23 = [graficos.create_image(154.5*3, 140*2,
                                               image=puente_y_im), "y"]
        self.puente24 = [graficos.create_image(154.5*4, 140*2,
                                               image=puente_bc_im), "bc"]
        self.puente34 = [graficos.create_image(154.5*4, 140*3,
                                               image=puente_ac_im), "ac"]
        self.puente35 = [graficos.create_image(154.5*5, 140*3,
                                               image=puente_y_im), "y"]
        self.puente36 = [graficos.create_image(154.5*6, 140*3,
                                               image=puente_ac_im), "ac"]
        self.puente26 = [graficos.create_image(154.5*6, 140*2,
                                               image=puente_x_im), "x"]
        self.puente16 = [(graficos.create_image(154.5*6, 140,
                                                image=puente_ad_im)), "ad"]
        graficos.lift(self.player)

    def nivel_2(self):  # --- --- --- --- 15 Puentes

        self.piso = 2
        graficos.coords(self.player, 154.5*0.25, 140*2)

        self.puente11 = [graficos.create_image(154.5, 140,
                                               image=puente_ad_im), "ad"]
        self.puente21 = [graficos.create_image(154.5, 140*2,
                                               image=puente_ad_im), "ad"]
        self.puente41 = [graficos.create_image(154.5, 140*4,
                                               image=puente_abd_im), "abd"]
        self.puente12 = [graficos.create_image(154.5*2, 140,
                                               image=puente_abc_im), "abc"]
        self.puente13 = [graficos.create_image(154.5*3, 140,
                                               image=puente_x2_im), "x2"]
        self.puente14 = [graficos.create_image(154.5*4, 140,
                                               image=puente_ad2_im), "ad2"]
        self.puente22 = [graficos.create_image(154.5*2, 140*2,
                                               image=puente_y_im), "y"]
        self.puente32 = [graficos.create_image(154.5*2, 140*3,
                                               image=puente_ac_im), "ac"]
        self.puente23 = [graficos.create_image(154.5*3, 140*2,
                                               image=puente_x_im), "x"]
        self.puente33 = [graficos.create_image(154.5*3, 140*3,
                                               image=puente_f1ll_im), "f1ll"]
        self.puente24 = [graficos.create_image(154.5*4, 140*2,
                                               image=puente_ac_im), "ac"]
        self.puente34 = [graficos.create_image(154.5*4, 140*3,
                                               image=puente_abc_im), "abc"]
        self.puente25 = [graficos.create_image(154.5*5, 140*2,
                                               image=puente_x_im), "x"]
        self.puente26 = [graficos.create_image(154.5*6, 140*2,
                                               image=puente_bc_im), "bc"]
        self.puente36 = [graficos.create_image(154.5*6, 140*3,
                                               image=puente_ac_im), "ac"]
        graficos.lift(self.player)

    def nivel_3(self):  # --- --- --- --- 18 Puentes

        self.piso = 3
        graficos.coords(self.player, 154.5*0.25, 140*3)

        self.puente21 = [graficos.create_image(154.5, 140*2,
                                               image=puente_abd_im), "abd"]
        self.puente31 = [graficos.create_image(154.5, 140*3,
                                               image=puente_x_im), "x"]
        self.puente32 = [graficos.create_image(154.5*2, 140*3,
                                               image=puente_bc_im), "bc"]
        self.puente42 = [graficos.create_image(154.5*2, 140*4,
                                               image=puente_abd_im), "abd"]
        self.puente13 = [graficos.create_image(154.5*3, 140,
                                               image=puente_bd_im), "bd"]
        self.puente23 = [graficos.create_image(154.5*3, 140*2,
                                               image=puente_x_im), "x"]
        self.puente33 = [graficos.create_image(154.5*3, 140*3,
                                               image=puente_ad_im), "ad"]
        self.puente43 = [graficos.create_image(154.5*3, 140*4,
                                               image=puente_y_im), "y"]
        self.puente14 = [graficos.create_image(154.5*4, 140,
                                               image=puente_x_im), "x"]
        self.puente24 = [graficos.create_image(154.5*4, 140*2,
                                               image=puente_ac_im), "ac"]
        self.puente34 = [graficos.create_image(154.5*4, 140*3,
                                               image=puente_f1ll2_im), "f1ll2"]
        self.puente44 = [graficos.create_image(154.5*4, 140*4,
                                               image=puente_y_im), "y"]
        self.puente15 = [graficos.create_image(154.5*5, 140,
                                               image=puente_y_im), "y"]
        self.puente35 = [graficos.create_image(154.5*5, 140*3,
                                               image=puente_bc_im), "bc"]
        self.puente45 = [graficos.create_image(154.5*5, 140*4,
                                               image=puente_bc_im), "bc"]
        self.puente16 = [graficos.create_image(154.5*6, 140,
                                               image=puente_bc_im), "bc"]
        self.puente26 = [graficos.create_image(154.5*6, 140*2,
                                               image=puente_ac_im), "ac"]
        self.puente36 = [graficos.create_image(154.5*6, 140*3,
                                               image=puente_ac2_im), "ac2"]
        graficos.lift(self.player)

    def nivel_4(self):  # --- --- --- --- 17 Puentes

        self.piso = 4
        graficos.coords(self.player, 154.5*0.25, 140*3)

        self.puente21 = [graficos.create_image(154.5, 140*2,
                                               image=puente_bd2_im), "bd2"]
        self.puente31 = [graficos.create_image(154.5, 140*3,
                                               image=puente_bc_im), "bc"]
        self.puente41 = [graficos.create_image(154.5, 140*4,
                                               image=puente_bc2_im), "bc2"]
        self.puente22 = [graficos.create_image(154.5*2, 140*2,
                                               image=puente_y_im), "y"]
        self.puente32 = [graficos.create_image(154.5*2, 140*3,
                                               image=puente_ac_im), "ac"]
        self.puente42 = [graficos.create_image(154.5*2, 140*4,
                                               image=puente_y_im), "y"]
        self.puente13 = [graficos.create_image(154.5*3, 140,
                                               image=puente_ac_im), "ac"]
        self.puente23 = [graficos.create_image(154.5*3, 140*2,
                                               image=puente_ad_im), "ad"]
        self.puente43 = [graficos.create_image(154.5*3, 140*4,
                                               image=puente_y_im), "y"]
        self.puente14 = [graficos.create_image(154.5*4, 140,
                                               image=puente_x2_im), "x2"]
        self.puente34 = [graficos.create_image(154.5*4, 140*3,
                                               image=puente_bd2_im), "bd2"]
        self.puente44 = [graficos.create_image(154.5*4, 140*4,
                                               image=puente_bc_im), "bc"]
        self.puente15 = [graficos.create_image(154.5*5, 140,
                                               image=puente_x_im), "x"]
        self.puente35 = [graficos.create_image(154.5*5, 140*3,
                                               image=puente_y_im), "y"]
        self.puente16 = [graficos.create_image(154.5*6, 140,
                                               image=puente_ac_im), "ac"]
        self.puente26 = [graficos.create_image(154.5*6, 140*2,
                                               image=puente_x_im), "x"]
        self.puente36 = [graficos.create_image(154.5*6, 140*3,
                                               image=puente_abc2_im), "abc2"]
        graficos.lift(self.player)

    def nivel_5(self):  # --- --- --- --- 17 Puentes

        self.piso = 5
        graficos.coords(self.player, 154.5*0.25, 140)

        self.puente11 = [graficos.create_image(154.5, 140,
                                               image=puente_ac_im), "ac"]
        self.puente21 = [graficos.create_image(154.5, 140*2,
                                               image=puente_y2_im), "y2"]
        self.puente31 = [graficos.create_image(154.5, 140*3,
                                               image=puente_acd_im), "acd"]
        self.puente41 = [graficos.create_image(154.5, 140*4,
                                               image=puente_bc2_im), "bc2"]
        self.puente12 = [graficos.create_image(154.5*2, 140,
                                               image=puente_bd2_im), "bd2"]
        self.puente22 = [graficos.create_image(154.5*2, 140*2,
                                               image=puente_bd_im), "bd"]
        self.puente32 = [graficos.create_image(154.5*2, 140*3,
                                               image=puente_x_im), "x"]
        self.puente42 = [graficos.create_image(154.5*2, 140*4,
                                               image=puente_y_im), "y"]
        self.puente13 = [graficos.create_image(154.5*3, 140,
                                               image=puente_bcd_im), "bcd"]
        self.puente23 = [graficos.create_image(154.5*3, 140*2,
                                               image=puente_bd_im), "bd"]
        self.puente33 = [graficos.create_image(154.5*3, 140*3,
                                               image=puente_bc_im), "bc"]
        self.puente14 = [graficos.create_image(154.5*4, 140,
                                               image=puente_y_im), "y"]
        self.puente24 = [graficos.create_image(154.5*4, 140*2,
                                               image=puente_y_im), "y"]
        self.puente15 = [graficos.create_image(154.5*5, 140,
                                               image=puente_x2_im), "x2"]
        self.puente25 = [graficos.create_image(154.5*5, 140*2,
                                               image=puente_y_im), "y"]
        self.puente16 = [graficos.create_image(154.5*6, 140,
                                               image=puente_ac_im), "ac"]
        self.puente26 = [graficos.create_image(154.5*6, 140*2,
                                               image=puente_abc2_im), "abc2"]
        graficos.lift(self.player)

    def nivel_6(self):  # --- --- --- --- 18 Puentes

        self.piso = 6
        graficos.coords(self.player, 154.5*0.25, 140*2)

        self.puente11 = [graficos.create_image(154.5, 140,
                                               image=puente_ac_im), "ac"]
        self.puente21 = [graficos.create_image(154.5, 140*2,
                                               image=puente_bc_im), "bc"]
        self.puente31 = [graficos.create_image(154.5, 140*3,
                                               image=puente_y2_im), "y2"]
        self.puente41 = [graficos.create_image(154.5, 140*4,
                                               image=puente_ac_im), "ac"]
        self.puente12 = [graficos.create_image(154.5*2, 140,
                                               image=puente_abd2_im), "abd2"]
        self.puente22 = [graficos.create_image(154.5*2, 140*2,
                                               image=puente_ac_im), "ac"]
        self.puente32 = [graficos.create_image(154.5*2, 140*3,
                                               image=puente_ad_im), "ad"]
        self.puente42 = [graficos.create_image(154.5*2, 140*4,
                                               image=puente_y_im), "y"]
        self.puente13 = [graficos.create_image(154.5*3, 140,
                                               image=puente_x_im), "x"]
        self.puente23 = [graficos.create_image(154.5*3, 140*2,
                                               image=puente_f1ll_im), "f1ll"]
        self.puente43 = [graficos.create_image(154.5*3, 140*4,
                                               image=puente_y_im), "y"]
        self.puente24 = [graficos.create_image(154.5*4, 140*2,
                                               image=puente_ad2_im), "ad2"]
        self.puente34 = [graficos.create_image(154.5*4, 140*3,
                                               image=puente_ac_im), "ac"]
        self.puente44 = [graficos.create_image(154.5*4, 140*4,
                                               image=puente_x2_im), "x2"]
        self.puente35 = [graficos.create_image(154.5*5, 140*3,
                                               image=puente_y_im), "y"]
        self.puente45 = [graficos.create_image(154.5*5, 140*4,
                                               image=puente_acd_im), "acd"]
        self.puente36 = [graficos.create_image(154.5*6, 140*3,
                                               image=puente_abc_im), "abc"]
        self.puente46 = [graficos.create_image(154.5*6, 140*4,
                                               image=puente_ac2_im), "ac2"]
        graficos.lift(self.player)

    def nivel_7(self):  # --- --- --- --- 19 Puentes

        self.piso = 7
        graficos.coords(self.player, 154.5*0.25, 140*4)

        self.puente21 = [graficos.create_image(154.5, 140*2,
                                               image=puente_ad_im), "ad"]
        self.puente31 = [graficos.create_image(154.5, 140*3,
                                               image=puente_x_im), "x"]
        self.puente41 = [graficos.create_image(154.5, 140*4,
                                               image=puente_bc_im), "bc"]
        self.puente22 = [graficos.create_image(154.5*2, 140*2,
                                               image=puente_x2_im), "x2"]
        self.puente32 = [graficos.create_image(154.5*2, 140*3,
                                               image=puente_bd2_im), "bd2"]
        self.puente42 = [graficos.create_image(154.5*2, 140*4,
                                               image=puente_ad_im), "ad"]
        self.puente13 = [graficos.create_image(154.5*3, 140,
                                               image=puente_ac_im), "ac"]
        self.puente23 = [graficos.create_image(154.5*3, 140*2,
                                               image=puente_ad_im), "ad"]
        self.puente33 = [graficos.create_image(154.5*3, 140*3,
                                               image=puente_ac_im), "ac"]
        self.puente43 = [graficos.create_image(154.5*3, 140*4,
                                               image=puente_x_im), "x"]
        self.puente14 = [graficos.create_image(154.5*4, 140,
                                               image=puente_bc_im), "bc"]
        self.puente24 = [graficos.create_image(154.5*4, 140*2,
                                               image=puente_x_im), "x"]
        self.puente34 = [graficos.create_image(154.5*4, 140*3,
                                               image=puente_ac2_im), "ac2"]
        self.puente44 = [graficos.create_image(154.5*4, 140*4,
                                               image=puente_y_im), "y"]
        self.puente15 = [graficos.create_image(154.5*5, 140,
                                               image=puente_ac_im), "ac"]
        self.puente25 = [graficos.create_image(154.5*5, 140*2,
                                               image=puente_ac_im), "ac"]
        self.puente35 = [graficos.create_image(154.5*5, 140*3,
                                               image=puente_x_im), "x"]
        self.puente45 = [graficos.create_image(154.5*5, 140*4,
                                               image=puente_ac2_im), "ac2"]
        self.puente26 = [graficos.create_image(154.5*6, 140*2,
                                               image=puente_x2_im), "x2"]
        graficos.lift(self.player)

    def regresar(self, desbloqueado=1):  # Retorno al menu principal
        graficos.unbind("<Button-1>")
        graficos.delete("all")
        return Seleccion().abrir_selector(desbloqueado)


videojuego = Menu()
videojuego.crear_menu()

# -- -- -- Mainloop
if __name__ == "__main__":
    root.mainloop()
