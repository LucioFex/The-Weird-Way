from tkinter import Canvas, Frame, Tk, PhotoImage, Button
from pygame import mixer
import TheWeirdBBDD

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
c_fg_no = "#aaa7a4"  # Todas las letras base
c_bg_se = "#1a1820"  # Color de cuadros de inicio
c_bg_no = "#1e1c24"  # Color de niveles bloqueados
c_bg_no2 = "#282121"  # Color de niveles bloqueados
c_bg_si = "#272430"  # Color de niveles desbloqueados
c_bg_press = "#1a1920"  # Color de botones comúnes siendo presionados
c_bg_press_si = "#221f2a"  # Color de niveles desbloqueados siendo presionados

# Direcciones
all_p = ("f1ll", "f2ll", "f3ll", "f4ll")  # Cantidad de direcciones: 4
xy_p = ("x", "y")  # Cantidad de direcciones: 2
dos_p = ("ac", "bc", "bd", "ad")  # Cantidad de direcciones: 4
tres_p = ("abd", "acd", "abc", "bcd")  # Cantidad de direcciones: 4

# Extras
maximo = 1  # Mayor nivel alcanzado en el regístro del juego
all_s = ["10", "20", "30", "40", "50", "60", "70", "80", "90"]  # Stars | Lvl
arranque = True  # Musica de inicio
piernas = {"dross", "randolph", "freud", "milei", "menem"}
ruedas = {"dolar", "seba", "franco"}
caminar_boton_se = True

# -- -- -- Root
root = Tk()
root.title(titulo)
root.resizable(False, False)
root.geometry(f"{ancho}x{alto}+{200}+{45}")
root.iconbitmap("LucioPalIco.ico")
root.config(bg=c_fondo)

# -- -- -- Guardado de la partida / BBDD
memoria = TheWeirdBBDD.Memoria()

# -- -- -- Imgs
# A = Izquierda | B = Derecha | C = Arriba | D = Abajo
logo_im = PhotoImage(file="Imgs/Logo.png")  # Logo del juego en el menu
menu_im = PhotoImage(file="Imgs/Inicio5.png")  # Fondo Menu
selec_im = PhotoImage(file="Imgs/Selector.png")  # Fondo Selector
fondo_im = PhotoImage(file="Imgs/Fondo_a.png")  # Escenario del juego
candado_im = PhotoImage(file="Imgs/Candado2.png")  # Niveles bloqueados
cuadro_im = PhotoImage(file="Imgs/Menu_play.png")  # Fondo de la Pausa
red_orb1_im = PhotoImage(file="Imgs/RedOrb1.png")  # Orbes Rojos / Puntos
red_orb2_im = PhotoImage(file="Imgs/RedOrb2.png")  # Orbes Rojos / Puntos
red_orb3_im = PhotoImage(file="Imgs/RedOrb3.png")  # Orbes Rojos / Puntos
elec_im = PhotoImage(file="Imgs/Chars/Marco.png")  # Marco de selección de char
star0_im = PhotoImage(file="Imgs/star0.png")  # Estrella inactiva
star1_im = PhotoImage(file="Imgs/star1.png")  # Estrella activa
puntos_im = PhotoImage(file="Imgs/Puntos.png")  # Estrella activa
lava_imgs = [None, None, None]  # Material para la animación de lava
for frame in range(3):
    lava_imgs[frame] = PhotoImage(file=f"Imgs/Fondo_b{frame + 1}.png")
# -- -- Botones In-Game
home_im = PhotoImage(file="Imgs/Retorno_Menu.png")  # Regreso al menu
restart_im = PhotoImage(file="Imgs/restart.png")  # Reinicio de nivel
walk0_im = PhotoImage(file="Imgs/Moverse0.png")  # Caminar desactivado
walk1_im = PhotoImage(file="Imgs/Moverse1.png")  # Caminar sin punto
walk2_im = PhotoImage(file="Imgs/Moverse2.png")  # Caminar con punto
# -- -- Trampas
trampa_im = [None, None, None, None]
for img in range(4):  # Trampas de fondo
    trampa_im[img] = PhotoImage(file=f"Imgs/Trap_{img + 1}.png")
# -- -- Puentes giratorios
puente_x_im = PhotoImage(file="Imgs/PuenteX.png")  # X
puente_y_im = PhotoImage(file="Imgs/PuenteY.png")  # Y
puente_f1ll_im = PhotoImage(file="Imgs/PuenteF1LL.png")  # XY
puente_f2ll_im = PhotoImage(file="Imgs/PuenteF2LL.png")  # XY
puente_f3ll_im = PhotoImage(file="Imgs/PuenteF3LL.png")  # XY
puente_f4ll_im = PhotoImage(file="Imgs/PuenteF4LL.png")  # XY

puente_ac_im = PhotoImage(file="Imgs/PuenteAC.png")  # AC
puente_ad_im = PhotoImage(file="Imgs/PuenteAD.png")  # AD
puente_bc_im = PhotoImage(file="Imgs/PuenteBC.png")  # BC
puente_bd_im = PhotoImage(file="Imgs/PuenteBD.png")  # BD

puente_abc_im = PhotoImage(file="Imgs/PuenteABC.png")  # ABC
puente_abd_im = PhotoImage(file="Imgs/PuenteABD.png")  # ABD
puente_acd_im = PhotoImage(file="Imgs/PuenteACD.png")  # ACD
puente_bcd_im = PhotoImage(file="Imgs/PuenteBCD.png")  # BCD
# -- -- Puentes no giratorios
puente_x2_im = PhotoImage(file="Imgs/PuenteX2.png")  # X
puente_y2_im = PhotoImage(file="Imgs/PuenteY2.png")  # Y
puente_f1ll2_im = PhotoImage(file="Imgs/PuenteF1LL2.png")  # XY

puente_ac2_im = PhotoImage(file="Imgs/PuenteAC2.png")  # AC
puente_ad2_im = PhotoImage(file="Imgs/PuenteAD2.png")  # AD
puente_bc2_im = PhotoImage(file="Imgs/PuenteBC2.png")  # BC
puente_bd2_im = PhotoImage(file="Imgs/PuenteBD2.png")  # BD

puente_abc2_im = PhotoImage(file="Imgs/PuenteABC2.png")  # ABC
puente_abd2_im = PhotoImage(file="Imgs/PuenteABD2.png")  # ABD
puente_acd2_im = PhotoImage(file="Imgs/PuenteACD2.png")  # ACD
puente_bcd2_im = PhotoImage(file="Imgs/PuenteBCD2.png")  # BCD

# -- -- -- Frame
pantalla = Frame(root, width=ancho, height=alto, bg=c_pantalla)
pantalla.pack()

# -- -- -- Canvas
graficos = Canvas(pantalla, width=ancho, height=alto, bg=c_pantalla,
                  borderwidth=0, highlightthickness=0)
graficos.pack()

# -- -- -- Musica y sonido
mixer.init(channels=1)
mixer.music.load("Audio/Musica/Menu.mp3")
select1_se = mixer.Sound("Audio/Sonido/select1.wav")
select2_se = mixer.Sound("Audio/Sonido/select2.wav")
select3_se = mixer.Sound("Audio/Sonido/select3.mp3")
red_orb_se = mixer.Sound("Audio/Sonido/red_orb.wav")
giro_se = mixer.Sound('Audio/Sonido/giro_puente.wav')
restart_se = mixer.Sound('Audio/Sonido/restart.mp3')
imposible_se = mixer.Sound('Audio/Sonido/imposible.wav')
run_se = mixer.Sound('Audio/Sonido/run.wav')
caminar1_se = mixer.Sound('Audio/Sonido/walking_1.wav')
caminar2_se = mixer.Sound('Audio/Sonido/walking_2.wav')

giro_se.set_volume(0.5)
run_se.set_volume(0.8)
caminar1_se.set_volume(0.5)
caminar2_se.set_volume(1)


# -- -- -- Botones Menu
class Menu:  # Menu principal
    def crear_menu(self):
        global arranque
        per = memoria.cargar()[2]
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
                            command=lambda: self.advertencia_reinicio())

        self.continuar = Button(graficos, text="Continuar Partida", fg=c_fg_no,
                                cursor="arrow", font=("Century Gothic", 20),
                                bg=c_bg_no2, width=27, state="disabled")

        if memoria.cargar() != [1, all_s, 'dross']:
            self.continuar.config(cursor="hand2", activeforeground=c_fg,
                                  activebackground=c_bg_se, fg=c_fg,
                                  bg=c_bg_no, state="normal", command=lambda:
                                  self.cerrar_menu("continuar", per))

        self.salir = Button(graficos, text="Salir", fg=c_fg, cursor="hand2",
                            font=("Century Gothic", 20), bg=c_bg_no,
                            width=24, activeforeground=c_fg,
                            activebackground=c_bg_se,
                            command=lambda: self.cerrar_menu("salir", per))

        self.nueva2 = graficos.create_window(ancho/2, alto/2 + alto/50,
                                             window=self.nueva)
        self.continuar2 = graficos.create_window(ancho/2, alto/2 + alto/5,
                                                 window=self.continuar)
        self.salir2 = graficos.create_window(ancho/2, alto/2 + alto/2.70,
                                             window=self.salir)

        # Musica
        if arranque:
            mixer.music.play(loops=-1)
            arranque = False
        # Sonido
        select3_se.set_volume(0.3)

    def cerrar_menu(self, selected, per):  # 1ro: Animación, luego cerrado.
        for boton in (self.nueva, self.continuar, self.salir):
            boton.config(command=lambda: None)

        # Sonido
        select3_se.play() if self.num == alto else None

        # Animaciones
        self.num -= 50
        graficos.coords(self.ani_menu, -1, alto, ancho, self.num)

        if selected == "nueva":
            try:
                graficos.move(self.bg_texto,   -65, 0)
                graficos.move(self.texto,      -65, 0)
            except AttributeError:
                pass
            finally:
                graficos.move(self.nueva2,     + 65, 0)
                graficos.move(self.continuar2, - 65, 0)
                graficos.move(self.salir2,     - 65, 0)
        elif selected == "continuar":
            graficos.move(self.nueva2,         - 65, 0)
            graficos.move(self.continuar2,     + 65, 0)
            graficos.move(self.salir2,         - 65, 0)
        elif selected == "salir":
            mixer.music.fadeout(1000)
            select3_se.fadeout(1000)
            graficos.move(self.nueva2,         - 65, 0)
            graficos.move(self.continuar2,     - 65, 0)
            graficos.move(self.salir2,         + 65, 0)

        if self.num > -50:  # Bucle generado para repetír el método (Animación)
            root.after(60, lambda: self.cerrar_menu(selected, per))

        elif self.num <= -50:  # Acciones tras animación. Eliminación de todo.
            graficos.delete("all")

            if selected == "nueva":
                memoria.vaciar()
                return Seleccion().abrir_selector(per)

            elif selected == "continuar":
                return Seleccion().abrir_selector(per, memoria.cargar()[0])
            return root.destroy()  # Si se quiere salir

    def advertencia_reinicio(self):
        if memoria.cargar() == [1, memoria.cargar()[1], 'dross']:
            return self.cerrar_menu("nueva", "dross")

        mixer.Sound.play(select1_se)
        aviso = ("    Se ha encontrado\n" +
                 "una partida guardada.\n" +
                 "¿Quieres reemplazarla\n" +
                 "    de todos modos?")
        self.bg_texto = graficos.create_rectangle(25, 300, 275, 450,
                                                  fill="#102f44")
        self.texto = graficos.create_text(150, 370, text=aviso,
                                          fill="#e5e5e5",
                                          font=("Century Gothic", 16))
        self.nueva.config(command=lambda: self.cerrar_menu("nueva", "dross"))


class Seleccion:  # Seleccionador de Niveles.
    def abrir_selector(self, per, desbloqueados=1, punto="00"):
        # Nivel predeterminado: 1
        # global maximo
        if desbloqueados >= memoria.cargar()[0]:  # Guardado del nivel jugado
            memoria.añadir_n(desbloqueados)
        maximo = memoria.cargar()[0]

        self.volver = Button(graficos, text="Volver al menu principal",
                             width=19, font=("Verdana", 15),
                             bg=c_bg_se, fg=c_fg,
                             activebackground=c_bg_press,
                             activeforeground=c_fg, cursor="hand2",
                             command=lambda: self.cerrar_selec("0", per))

        self.char = PhotoImage(file="Imgs/Chars/{}/Char.png".format(per))
        self.char_sec = Button(graficos, text="Personajes ",
                               font=("Verdana", 15), bg=c_bg_se, fg=c_fg,
                               cursor="hand2", activeforeground=c_fg,
                               image=self.char, compound="right",
                               activebackground=c_bg_press,
                               command=self.personajes)

        # Loop para generar los botones de los niveles:
        for nivel in ("self.nivel_1", "self.nivel_2", "self.nivel_3",
                      "self.nivel_4", "self.nivel_5", "self.nivel_6",
                      "self.nivel_7", "self.nivel_8", "self.nivel_9"):
            # Botones generandose
            exec("""{0} = Button(graficos, text='       Nivel {1} ',
                    width=276,font=('Verdana', 20),
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
            elif int(nivel[-1]) > maximo:
                exec(f"{nivel}.config(image=candado_im, compound='right')")

        # Solución con IFs (solo para corto plazo)
        if maximo >= 1:
            self.nivel_1.config(command=lambda: self.cerrar_selec("1", per))
        if maximo >= 2:
            self.nivel_2.config(command=lambda: self.cerrar_selec("2", per))
        if maximo >= 3:
            self.nivel_3.config(command=lambda: self.cerrar_selec("3", per))
        if maximo >= 4:
            self.nivel_4.config(command=lambda: self.cerrar_selec("4", per))
        if maximo >= 5:
            self.nivel_5.config(command=lambda: self.cerrar_selec("5", per))
        if maximo >= 6:
            self.nivel_6.config(command=lambda: self.cerrar_selec("6", per))
        if maximo >= 7:
            self.nivel_7.config(command=lambda: self.cerrar_selec("7", per))
        if maximo >= 8:
            self.nivel_8.config(command=lambda: self.cerrar_selec("8", per))
        if maximo >= 9:
            self.nivel_9.config(command=lambda: self.cerrar_selec("9", per))
        # ---------------------------------------------------------------------
        # Fondo
        graficos.create_image(ancho/2, alto/2, image=selec_im)
        # Fila 0 / Botones de configuración
        graficos.create_window(ancho/5.75, 35, window=self.volver)
        graficos.create_window(ancho/1.205, 35, window=self.char_sec)

        lvl = 0  # Generación de filas de niveles
        for fila in (alto/4.5, alto/2, alto/1.27):
            for colum in (ancho/5.5, ancho/1.955, ancho/1.20):
                lvl += 1
                exec(f"""graficos.create_window(colum, fila,
                                                window=self.nivel_{lvl})""")
        del lvl

        # Generación de Sprites del personaje seleccionado:
        return self.puntaje(punto)

    def puntaje(self, obtenido):
        repe = 1  # Repetición
        lista_s = memoria.cargar()[1]  # Lista de niveles editable

        for star_x in (115, 200, 285):  # Generación de estrellas huecas
            for star_y in (245, 455, 655):
                for col in (0, 350, 695):
                    exec("""self.est_{} = graficos.create_image(
                            star_x + col, star_y, image=star0_im)"""
                         .format(repe))
                    repe += 1
        del repe

        for p in range(1, 9 + 1):  # Incremento de estrellas por avance en lvl
            if (int(obtenido[0]) == p and
               int(obtenido[1]) > int(lista_s[p-1][1])):

                # Reemplazo por mayores puntos (++) si son (>) a los anteriores
                lista_s[p - 1] = (lista_s[p-1][0:-1] +
                                  obtenido[1])
                break

        for p in lista_s:  # Estrellas obtenidas por nivel
            lista = []
            lista.append(0) if p[1] == "1" else None
            lista.extend([0, 9]) if p[1] == "2" else None
            lista.extend([0, 9, 18]) if p[1] == "3" else None

            for punto in lista:
                exec("graficos.itemconfig(self.est_{},image=star1_im)".
                     format(int(p[0]) + punto))

        self.total_p = 0  # Todos los puntos obtenidos
        for i in lista_s:
            self.total_p += int(i[1])
        print(self.total_p)
        memoria.añadir_e(lista_s)

        return lista_s  # Todas las estrellas

    def personajes(self):
        mixer.Sound.play(select1_se)
        graficos.delete("all")
        graficos.bind("<Button-1>", self.cambio_chars)
        self.chara = memoria.cargar()[2]

        for face in ("dross", "randolph", "dolar", "freud",
                     "milei", "seba", "franco", "menem"):
            exec("self.{0}_img = PhotoImage(file='Imgs/Chars/Caras/{0}.png')"
                 .format(face))

        self.selec_menu = Button(graficos, text="Selector de niveles",
                                 width=15, font=("Verdana", 15),
                                 bg=c_bg_se, fg=c_fg,
                                 activebackground=c_bg_press,
                                 activeforeground=c_fg, cursor="hand2",
                                 command=self.salir_chars)

        for default in (("dross", 206, 253), ("randolph", 371, 253),
                        ("dolar", 535, 253), ("freud", 696, 252),
                        ("milei", 856, 252), ("seba", 369, 449),
                        ("franco", 531, 447), ("menem", 696, 447)):
            # print(f"DEFAULT = {default} | PER = {per}")
            if default[0] == self.chara:
                #  back = Imagen de fondo
                self.back_im = PhotoImage(file="Imgs/Chars/Inter_{}.png".
                                          format(default[0]))
                self.backg = graficos.create_image(ancho/2, alto/2,
                                                   image=self.back_im)
                self.marco = graficos.create_image(default[1], default[2],
                                                   image=elec_im)
                break

        # -- -- Colocación de Imgs
        graficos.create_window(ancho/8.5, 50, window=self.selec_menu)

        # -- -- Personajes desbloqueados
        star_min = 0
        for i in ((208, 249, self.dross_img),
                  (371, 251, self.randolph_img),
                  (538, 252, self.dolar_img),
                  (694, 252, self.freud_img),
                  (856, 252, self.milei_img),
                  (371, 447, self.seba_img),
                  (531, 447, self.franco_img),
                  (696, 447, self.menem_img)):

            if self.total_p >= star_min:
                graficos.create_image(i[0], i[1], image=i[2])
                star_min += 3
        del star_min

        self.presen = PhotoImage(file="Imgs/Chars/{}/Presentacion.png".
                                 format(self.chara))  # Presentación
        graficos.create_image(125, 575, image=self.presen)

        #  Anotación del total de estrellas
        graficos.create_image(950, 58, image=puntos_im)
        graficos.create_text(1000, 56, text=self.total_p, fill="#f4f4f4",
                             font=("Century Gothic", 30))

    def cambio_chars(self, cursor):  # Selección de personajes
        # 0=Dross|1=Randolph|2=Dolar|3=Freud|4=Milei|5=Seba|6=Franco|7=Menem #

        # -- -- Posición del click al elegír un personaje
        for click in (("dross", 133, 161, 281, 339, 206, 253, 0),
                      ("randolph", 299, 162, 443, 339, 371, 253, 3),
                      ("dolar", 464, 163, 612, 339, 535, 253, 6),
                      ("freud", 622, 163, 767, 342, 696, 252, 9),
                      ("milei", 784, 161, 927, 339, 856, 252, 12),
                      ("seba", 299, 356, 444, 535, 369, 449, 15),
                      ("franco", 458, 357, 605, 535, 531, 447, 18),
                      ("menem", 623, 361, 767, 534, 696, 447, 21)):

            if (cursor.x >= click[1] and cursor.x <= click[3] and
                    cursor.y >= click[2] and cursor.y <= click[4]):

                if self.total_p >= click[7]:
                    self.chara = click[0]
                    self.cuadro_advertencia(click[7], True)

                    self.back_im = PhotoImage(file="Imgs/Chars/Inter_{}.png".
                                              format(click[0]))

                    graficos.coords(self.marco, click[5], click[6])
                    self.backg = graficos.create_image(ancho/2, alto/2,
                                                       image=self.back_im)
                    graficos.lower(self.backg)
                    break

                elif self.total_p < click[7]:
                    self.cuadro_advertencia(click[7], False)
                    break

        # Presentación
        self.presen = PhotoImage(file="Imgs/Chars/{}/Presentacion.png".
                                 format(self.chara))
        graficos.create_image(125, 575, image=self.presen)

        return memoria.añadir_p(self.chara)

    def cuadro_advertencia(self, estrellas, limpiar):
        aviso = (f"   Se requieren \n{estrellas} estrellas para\n" +
                 " este personaje")
        try:
            graficos.delete(self.bg_texto)
            graficos.delete(self.texto)
        except AttributeError:
            pass
        finally:
            if limpiar:
                mixer.Sound.play(select1_se)
            elif limpiar is not True:
                mixer.Sound.play(imposible_se)
                self.bg_texto = graficos.create_rectangle(832, 450, 1069, 555,
                                                          fill="#350b0b")
                self.texto = graficos.create_text(950, 500, text=aviso,
                                                  fill="#e5e5e5",
                                                  font=("Century Gothic", 19))

    def salir_chars(self):
        mixer.Sound.play(select1_se)
        graficos.delete("all")
        graficos.unbind("<Button-1>")
        return self.abrir_selector(self.chara, maximo)

    def cerrar_selec(self, nivel, per):  # 0 = Menu | >= 1 y <=9 = X Nivel
        graficos.delete("all")
        del self.volver, self.nivel_1, self.nivel_2, self.nivel_3,
        self.nivel_4, self.nivel_5, self.nivel_6, self.nivel_7,
        self.nivel_8, self.nivel_9

        if nivel == "0":  # If por si se quiere volver al menu principal
            mixer.Sound.play(select1_se)
            return Menu().crear_menu()
        elif nivel != "0":  # Elif para buscar un nivel
            mixer.Sound.play(select2_se)
            for lvl in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
                if nivel == lvl:
                    exec('Partida(per).nivel_{0}()'.format(lvl))
                    break


class Partida:  # Ancho base = 154.5 (77 X) | Alto base = 140 (140 Y)
    def __init__(self, per):
        self.char = per
        self.lava = graficos.create_image(ancho/2, alto/2, image=lava_imgs[0])
        self.fondo = graficos.create_image(ancho/2, alto/2, image=fondo_im)
        self.tiempo = 0  # String para el tiempo del nivel

        self.reinicio = Button(graficos, font=("Century Gothic", 15),
                               bd=0, highlightthickness=0, image=restart_im,
                               activebackground='#1d2023',
                               cursor="hand2", command=self.reiniciar)

        self.home = Button(graficos, font=("Century Gothic", 15),
                           bd=0, highlightthickness=0, image=home_im,
                           activebackground='#23272d',
                           cursor="hand2", command=self.pausa)

        self.walk = Button(graficos, font=("Century Gothic", 15),
                           bd=0, highlightthickness=0, image=walk0_im,
                           activebackground='#23272d', cursor="hand2")

        self.limite = graficos.create_text(ancho/2, 15, fill="white",
                                           text=f"Bonus: {self.tiempo}",
                                           font=("Century Gothic", 18))

        graficos.create_window(35, 35, window=self.home)
        graficos.create_window(1035, 35, window=self.walk)
        graficos.create_window(70, 20, window=self.reinicio)
        graficos.bind("<Button-1>", self.giro)  # Giro de los caminos

        self.interrupcion = False  # Pausa de las animaciones

        for img in ("aba", "izq", "der", "arr"):  # Sprites de 4 dires
            for sprite in range(1, 3 + 1):  # 3 sprites al caminar
                exec("""self.char{1}_{2} = PhotoImage(
                        file='Imgs/Chars/{0}/Char{1}_{2}.png')""".
                     format(self.char, sprite, img))
        self.player = graficos.create_image(-100, -100,
                                            image=self.char1_der)

        self.trap = [None, None, None, None, None, None, None, None]
        return self.lava_mov()

    def lava_mov(self, intensidad=0):
        if self.interrupcion is False:
            if intensidad == 0:
                graficos.itemconfig(self.lava, image=lava_imgs[0])
            elif intensidad == 1:
                graficos.itemconfig(self.lava, image=lava_imgs[1])
            elif intensidad == 2:
                graficos.itemconfig(self.lava, image=lava_imgs[2])
            elif intensidad == 3:
                graficos.itemconfig(self.lava, image=lava_imgs[1])
                intensidad = -1

            graficos.after(1500, lambda: self.lava_mov(intensidad + 1))

    def tiempo_bonus(self):
        if self.interrupcion is False and self.tiempo > 0:
            self.tiempo -= 1
            graficos.itemconfig(self.limite, text=f"Bonus: {self.tiempo}")

            return graficos.after(1005, self.tiempo_bonus)

    def reiniciar(self):  # Reinicio del estado del nivel
        mixer.Sound.play(restart_se)
        graficos.delete("all")
        exec("Partida(self.char).nivel_{}()".format(self.piso))

    def pausa(self):  # Ret = Return / Retorno
        mixer.Sound.play(select1_se)
        self.interrupcion = True
        graficos.unbind("<Button-1>")
        self.home.config(command=lambda: None)
        self.walk.config(command=lambda: None)
        self.reinicio.config(command=lambda: None)

        for boton in ("reanudar", "sele", "exit"):  # Generación de botones
            exec("""self.{} = Button(graficos, bg="#22144f", bd=2, fg=c_fg,
                                     font=("Lucida Sans", 21),
                                     width=16, relief="raised",
                                     activebackground="#1a0d46",
                                     activeforeground=c_fg,
                                     highlightthickness=0)""".format(boton))

        self.reanudar.config(text="Reanudar", command=self.despausa)
        self.sele.config(text="Seleccionar nivel",
                         command=lambda: self.regresar(destino="selec"))
        self.exit.config(text="Volver al menu",
                         command=lambda: self.regresar(destino="menu"))

        self.cuadro = graficos.create_image(ancho/2, alto/2, image=cuadro_im)
        self.retorno = graficos.create_window(ancho/2, alto/3,
                                              window=self.reanudar)
        self.selector = graficos.create_window(ancho/2, alto/2,
                                               window=self.sele)
        self.salida = graficos.create_window(ancho/2, alto/1.5,
                                             window=self.exit)

    def giro(self, cursor):
        # Condicionales a corto plazo, tratar de depurarlo con bucles o algo.

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
        mixer.Sound.play(giro_se)
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

        return self.nivel_ganado()

    def nivel_ganado(self):  # -- -- -- Niveles Ganados
        # -- Nivel 1 Ganado:
        if (self.piso == 1 and self.puente31[1] == "x"
            and self.puente22[1] == "bd" and self.puente32[1] == "ac"
            and self.puente23[1] == "x" and self.puente24[1] == "ad"
            and self.puente34[1] == "bc" and self.puente35[1] == "x"
            and self.puente36[1] == "ac" and self.puente26[1] == "y"
                and self.puente16[1] == "bd"):
            self.paso = [0, 1, 4, 1, 1, 3, 1, 1, 4, 4, 1, 1, 1]
            return self.walk.config(image=walk1_im,
                                    command=lambda:
                                    self.mov_animacion(1, self.paso, "11"))
        elif (self.piso == 1 and self.puente31[1] == "x"  # PUNTO
              and self.puente32[1] == "ad" and self.puente42[1] == "bc"
              and self.puente43[1] == "x" and self.puente44[1] == "ac"
              and self.puente34[1] == "bd" and self.puente35[1] == "x"
              and self.puente36[1] == "ac" and self.puente26[1] == "y"
              and self.puente16[1] == "bd"):
            self.paso = [0, 1, 3, 1, 1, 4, 1, 1, 4, 4, 1, 1, 1]
            return self.walk.config(image=walk2_im,
                                    command=lambda:
                                    self.mov_animacion(1, self.paso, "12"))
            self.estrellas_1 += 2
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
            return self.walk.config(image=walk2_im, command=lambda:  # PUNTO
                                    self.mov_animacion(2, self.paso, "22"))

        elif (self.piso == 2 and self.puente11[1] == "bd"
              and self.puente21[1] == "ac" and self.puente24[1] == "bc"
              and self.puente25[1] == "x" and self.puente26[1] == "ad"
              and self.puente36[1] == "bc" and (self.puente12[1] == "abd"
              or self.puente12[1] == "abc")):

            self.paso = [0, 4, 1, 1, 1, 3, 1, 1, 3, 1, 1, 1]
            return self.walk.config(image=walk1_im, command=lambda:
                                    self.mov_animacion(2, self.paso, "21"))

        # -- Nivel 3 Ganado:
        elif (self.piso == 3 and self.puente31[1] == "x"
              and self.puente32[1] == "ad" and self.puente43[1] == "x"
              and self.puente44[1] == "x" and self.puente45[1] == "ac"
              and self.puente35[1] == "ad" and self.puente33[1] == "bc"
              and self.puente23[1] == "y" and self.puente13[1] == "bd"
              and self.puente14[1] == "x" and self.puente15[1] == "x"
              and self.puente16[1] == "ad" and self.puente26[1] == "bc"
              and (self.puente42[1] == "abc" or self.puente42[1] == "bcd")):

            self.paso = [0, 1, 3, 1, 1, 1, 4, 2, 2, 4, 4, 1, 1, 1, 3, 1, 1, 1]
            return self.walk.config(image=walk2_im, command=lambda:  # PUNTO
                                    self.mov_animacion(3, self.paso, "32"))

        elif (self.piso == 3 and self.puente31[1] == "x"
              and self.puente32[1] == "ad" and self.puente43[1] == "x"
              and self.puente44[1] == "x" and self.puente45[1] == "ac"
              and self.puente35[1] == "bd" and self.puente26[1] == "bd"
              and (self.puente42[1] == "abc" or self.puente42[1] == "bcd")):

            self.paso = [0, 1, 3, 1, 1, 1, 4, 1, 4, 1, 1, 1]
            return self.walk.config(image=walk1_im, command=lambda:
                                    self.mov_animacion(3, self.paso, "31"))

        # -- Nivel 4 Ganado:
        elif (self.piso == 4 and self.puente31[1] == "ac"
              and self.puente22[1] == "x" and self.puente23[1] == "ac"
              and self.puente13[1] == "bd" and self.puente15[1] == "x"
              and self.puente16[1] == "ad" and self.puente26[1] == "y"):

            self.paso = [0, 4, 1, 1, 4, 1, 1, 1, 3, 3, 1, 1, 1]
            return self.walk.config(image=walk2_im, command=lambda:  # PUNTO
                                    self.mov_animacion(4, self.paso, "42"))

        elif (self.piso == 4 and self.puente31[1] == "ad"
                and self.puente42[1] == "x" and self.puente43[1] == "x"
                and self.puente44[1] == "ac" and self.puente35[1] == "x"):

            self.paso = [0, 3, 1, 1, 1, 4, 1, 1, 1, 1]
            return self.walk.config(image=walk1_im, command=lambda:
                                    self.mov_animacion(4, self.paso, "41"))
        # -- Nivel 5 Ganado:
        elif (self.piso == 5 and self.puente11[1] == "ad"
              and self.puente32[1] == "x" and self.puente33[1] == "ac"
              and self.puente23[1] == "ad" and self.puente22[1] == "bc"
              and self.puente14[1] == "x" and self.puente16[1] == "ad"
              and (self.puente31[1] == "abc" or self.puente31[1] == "bcd")
              and (self.puente13[1] == "abd" or self.puente13[1] == "abc")):

            self.paso = [0, 3, 3, 1, 1, 4, 2, 4, 1, 1, 1, 1, 3, 1, 1, 1]
            return self.walk.config(image=walk2_im, command=lambda:  # PUNTO
                                    self.mov_animacion(5, self.paso, "52"))

        elif (self.piso == 5 and self.puente11[1] == "ad"
              and self.puente32[1] == "x" and self.puente33[1] == "ac"
              and self.puente23[1] == "bd" and self.puente24[1] == "x"
              and self.puente25[1] == "x" and (self.puente31[1] == "abc"
              or self.puente31[1] == "bcd")):

            self.paso = [0, 3, 3, 1, 1, 4, 1, 1, 1, 1, 1, 1]
            return self.walk.config(image=walk1_im, command=lambda:
                                    self.mov_animacion(5, self.paso, "51"))

        # -- Nivel 6 Ganado:
        elif (self.piso == 6 and self.puente21[1] == "ad"
              and self.puente41[1] == "bc" and self.puente42[1] == "x"
              and self.puente43[1] == "x" and (self.puente45[1] == "abc"
              or self.puente45[1] == "abd") and (self.puente36[1] == "bcd"
              or self.puente36[1] == "abd")):

            self.paso = [0, 3, 3, 1, 1, 1, 1, 1, 4, 1, 1, 1]
            return self.walk.config(image=walk1_im, command=lambda:
                                    self.mov_animacion(6, self.paso, "61"))

        elif (self.piso == 6 and self.puente11[1] == "bd"
              and self.puente21[1] == "ac" and self.puente22[1] == "bc"
              and self.puente34[1] == "bc" and self.puente35[1] == "x"
              and (self.puente36[1] == "abc" or self.puente36[1] == "abd")):

            self.paso = [0, 4, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1]
            return self.walk.config(image=walk2_im, command=lambda:  # PUNTO
                                    self.mov_animacion(6, self.paso, "62"))

        # -- Nivel 7 Ganado:
        elif (self.piso == 7 and self.puente21[1] == "bd"
              and self.puente31[1] == "y" and self.puente41[1] == "ac"
              and self.puente23[1] == "ad" and self.puente33[1] == "bc"
              and self.puente14[1] == "bd" and self.puente24[1] == "y"
              and self.puente15[1] == "ad" and self.puente25[1] == "bc"):
            self.paso = [0, 4, 4, 1, 1, 3, 1, 4, 4, 1, 3, 1, 1, 1, 1]
            return self.walk.config(image=walk2_im, command=lambda:  # PUNTO
                                    self.mov_animacion(7, self.paso, "72"))

        elif (self.piso == 7 and self.puente21[1] == "bd"
              and self.puente31[1] == "y" and self.puente41[1] == "ac"
              and self.puente42[1] == "bc" and self.puente23[1] == "ad"
              and self.puente33[1] == "ac" and self.puente43[1] == "x"
              and self.puente44[1] == "x" and self.puente25[1] == "bd"
              and self.puente35[1] == "y"):
            self.paso = [0, 4, 4, 1, 1, 3, 2, 3, 1, 1, 1, 4, 4, 1, 1, 1, 1]
            return self.walk.config(image=walk1_im, command=lambda:
                                    self.mov_animacion(7, self.paso, "71"))
        # -- Nivel 8 Ganado:
        elif (self.piso == 8 and self.puente11[1] == "ad"  # (Punto)
              and self.puente21[1] == "bc" and self.puente22[1] == "ad"
              and self.puente32[1] == "y" and self.puente42[1] == "bc"
              and self.puente43[1] == "x" and self.puente34[1] == "bd"
              and self.puente35[1] == "ad" and self.puente45[1] == "bc"
              and self.puente46[1] == "ac"):

            self.paso = [0, 3, 1, 3, 3, 1, 1, 4, 1, 3, 1, 4, 1, 1, 1]
            return self.walk.config(image=walk2_im, command=lambda:
                                    self.mov_animacion(8, self.paso, "82"))

        elif (self.piso == 8 and self.puente11[1] == "ad"
              and self.puente21[1] == "bc" and self.puente22[1] == "ac"
              and (self.puente13[1] == "abd" or self.puente13[1] == "acd")
              and self.puente24[1] == "x" and self.puente25[1] == "ad"
              and self.puente35[1] == "bc"):

            self.paso = [0, 3, 1, 4, 1, 3, 1, 1, 3, 1, 1, 1]
            return self.walk.config(image=walk1_im, command=lambda:
                                    self.mov_animacion(8, self.paso, "81"))
        # -- Nivel 9 Ganado / FINAL:
        elif (self.piso == 9 and self.puente31[1] == "ac"  # Op 1 / Si Punto
              and self.puente21[1] == "y" and self.puente12[1] == "ad"
              and self.puente22[1] == "bc" and self.puente23[1] == "ac"
              and self.puente14[1] == "x" and self.puente15[1] == "ad"
              and (self.puente25[1] == "acd" or self.puente25[1] == "bcd")
              and self.puente34[1] == "bd" and self.puente44[1] == "bc"
              and self.puente45[1] == "x" and self.puente36[1] == "y"
              and self.puente16[1] == "bd"):

            self.paso = [0, 4, 4, 1, 3, 1, 4, 1, 1, 3, 3,
                         2, 3, 1, 1, 4, 4, 4, 1, 1, 1, 1]
            return self.walk.config(image=walk2_im, command=lambda:
                                    self.mov_animacion(9, self.paso, "92"))

        elif (self.piso == 9 and self.puente31[1] == "ad"  # Op 2
              and self.puente41[1] == "bc" and self.puente42[1] == "x"
              and self.puente34[1] == "ad" and self.puente44[1] == "bc"
              and self.puente45[1] == "x" and self.puente36[1] == "y"
              and self.puente36[1] == "y" and self.puente16[1] == "bd"):

            self.paso = [0, 3, 1, 1, 4, 1, 3, 1, 1, 4, 4, 4, 1, 1, 1]
            return self.walk.config(image=walk1_im, command=lambda:
                                    self.mov_animacion(9, self.paso, "91"))

        elif (self.piso == 9 and self.puente31[1] == "ac"  # Op 3
              and self.puente21[1] == "y" and self.puente12[1] == "ad"
              and self.puente22[1] == "bc" and self.puente23[1] == "ad"
              and self.puente34[1] == "ad" and self.puente44[1] == "bc"
              and self.puente45[1] == "x" and self.puente36[1] == "y"
              and self.puente16[1] == "bd"):

            self.paso = [0, 4, 4, 1, 3, 1, 3, 1, 3, 1, 1, 4, 4, 4, 1, 1, 1]
            return self.walk.config(image=walk1_im, command=lambda:
                                    self.mov_animacion(9, self.paso, "91"))

        elif (self.piso == 9 and self.puente31[1] == "ad"  # Op 4
              and self.puente41[1] == "bc" and self.puente42[1] == "x"
              and self.puente22[1] == "bd" and self.puente23[1] == "ac"
              and self.puente14[1] == "x" and self.puente15[1] == "ad"
              and (self.puente25[1] == "acd" or self.puente25[1] == "bcd")
              and self.puente34[1] == "bd" and self.puente44[1] == "bc"
              and self.puente45[1] == "x" and self.puente36[1] == "y"
              and self.puente16[1] == "bd"):

            self.paso = [0, 3, 1, 1, 4, 2, 4, 1, 4, 1, 1, 3,
                         3, 2, 3, 1, 1, 4, 4, 4, 1, 1, 1, 1]
            return self.walk.config(image=walk2_im, command=lambda:
                                    self.mov_animacion(9, self.paso, "92"))

        # Desabilitación del botón de PLAY (walk)
        return self.walk.config(image=walk0_im, command=lambda: None)

    def mov_personaje(self, direccion, iter=0):  # iter = Iteraciones
        # 1 = DER | 2 = IZQ | 3 = ABA | 4 = ARR | 0 = Primer DER #
        global jojo
        if iter == 13:
            return None

        if mixer.Channel(1).get_busy() == 0 and self.char in piernas:
            mixer.Channel(1).play(caminar1_se)  # Sonido de pasos de pies

        elif mixer.Channel(1).get_busy() == 0 and self.char in ruedas:
            mixer.Channel(1).play(caminar2_se)  # Sonido de ruedas girando

        if direccion == 0:  # Dirección = Derecha Inicial
            if iter >= 0 and iter < 3:
                graficos.itemconfig(self.player, image=self.char1_der)
            elif iter >= 3 and iter < 6:
                graficos.itemconfig(self.player, image=self.char2_der)
            elif iter >= 6 and iter < 9:
                graficos.itemconfig(self.player, image=self.char1_der)
            elif iter >= 9 and iter < 13:
                graficos.itemconfig(self.player, image=self.char3_der)
            graficos.move(self.player, 9, 0)
            if iter == 0:
                self.len_x += 1

        elif direccion == 1:  # Dirección = Derecha
            if iter >= 0 and iter < 3:
                graficos.itemconfig(self.player, image=self.char1_der)
            elif iter >= 3 and iter < 6:
                graficos.itemconfig(self.player, image=self.char2_der)
            elif iter >= 6 and iter < 9:
                graficos.itemconfig(self.player, image=self.char1_der)
            elif iter >= 9 and iter < 13:
                graficos.itemconfig(self.player, image=self.char3_der)
            graficos.move(self.player, 11.9, 0)
            if iter == 0:
                self.len_x += 1

        elif direccion == 2:  # Dirección = Izquierda
            if iter >= 0 and iter < 3:
                graficos.itemconfig(self.player, image=self.char1_izq)
            elif iter >= 3 and iter < 6:
                graficos.itemconfig(self.player, image=self.char2_izq)
            elif iter >= 6 and iter < 9:
                graficos.itemconfig(self.player, image=self.char1_izq)
            elif iter >= 9 and iter < 13:
                graficos.itemconfig(self.player, image=self.char3_izq)
            graficos.move(self.player, -11.9, 0)
            if iter == 0:
                self.len_x -= 1

        elif direccion == 3:  # Dirección = Abajo
            if iter >= 0 and iter < 3:
                graficos.itemconfig(self.player, image=self.char1_aba)
            elif iter >= 3 and iter < 6:
                graficos.itemconfig(self.player, image=self.char2_aba)
            elif iter >= 6 and iter < 9:
                graficos.itemconfig(self.player, image=self.char1_aba)
            elif iter >= 9 and iter < 13:
                graficos.itemconfig(self.player, image=self.char3_aba)
            graficos.move(self.player, 0, 10.7)
            if iter == 0:
                self.len_y += 1

        elif direccion == 4:  # Dirección = Arriba
            if iter >= 0 and iter < 3:
                graficos.itemconfig(self.player, image=self.char1_arr)
            elif iter >= 3 and iter < 6:
                graficos.itemconfig(self.player, image=self.char2_arr)
            elif iter >= 6 and iter < 9:
                graficos.itemconfig(self.player, image=self.char1_arr)
            elif iter >= 9 and iter < 13:
                graficos.itemconfig(self.player, image=self.char3_arr)
            graficos.move(self.player, 0, -10.7)
            if iter == 0:
                self.len_y -= 1

        # -- -- -- Obtención del punto / orbe:
        if self.len_x == self.orbe_x and self.len_y == self.orbe_y:
            red_orb_se.play() if iter == 4 else None
            if iter >= 8 and iter < 10:
                graficos.lift(self.orbe)
                graficos.itemconfig(self.orbe, image=red_orb2_im)
            elif iter >= 10 and iter < 12:
                graficos.itemconfig(self.orbe, image=red_orb3_im)
            elif iter >= 12:
                graficos.delete(self.orbe)

        graficos.update()
        graficos.after(27, lambda: self.mov_personaje(direccion, iter+1))

    def mov_animacion(self, nivel, paso, camino):  # Animación del char
        global caminar_boton_se
        if caminar_boton_se:
            mixer.Sound.play(run_se)
            caminar_boton_se = False

        graficos.unbind("<Button-1>")
        self.walk.config(command=lambda: None)
        self.home.config(command=lambda: None)
        self.reinicio.config(command=lambda: None)
        try:  # Forma de chequear si la lista esta vacía o no:
            self.mov_personaje(paso[0])
        except IndexError:  # Si esta vacía, se terminó la animación:
            caminar_boton_se = True
            if self.tiempo > 0:
                return self.regresar(desbloqueado=nivel + 1,
                                     puntos=str(int(camino) + 1))
            return self.regresar(desbloqueado=nivel + 1, puntos=camino)

        paso.pop(0)
        graficos.after(415, lambda: self.mov_animacion(nivel, paso, camino))

    def trampas(self, spin=0):  # Justificación de la meta
        if spin > 3:  # Motívo del bucle / límite de Sprites
            spin = 0
        for sprite in range(4):  # Ilusión / Animación
            if spin == sprite:
                for trampa in range(len(self.trap)):  # 8 Trampas
                    graficos.itemconfig(self.trap[trampa],
                                        image=trampa_im[sprite])
                break  # Seguir chequeando el asunto de las trampas

        if self.interrupcion is False:
            return graficos.after(55, lambda: self.trampas(spin + 1))

    def orbe_mov(self, mov=0):
        if mov <= 5:
            graficos.move(self.orbe, 0, -1)
        elif mov > 5:
            graficos.move(self.orbe, 0, 1)

        if mov >= 10:
            mov = 0

        if self.interrupcion is False:
            return graficos.after(200, lambda: self.orbe_mov(mov + 1))

    def nivel_1(self):  # --- --- --- --- 11 Puentes

        self.len_x = 0
        self.len_y = 3
        self.orbe_x = 3
        self.orbe_y = 4

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
        self.puente42 = [(graficos.create_image(154.5*2, 140*4,
                                                image=puente_ad_im)), "ad"]
        self.puente43 = [(graficos.create_image(154.5*3, 140*4,
                                                image=puente_x_im)), "x"]
        self.puente44 = [(graficos.create_image(154.5*4, 140*4,
                                                image=puente_bd_im)), "bd"]

        self.orbe = graficos.create_image(154.5*3, 140*4, image=red_orb1_im)
        graficos.lift(self.player)

        for p in range(4):  # Punto de partida
            if p != 2:  # Punto sin trampa
                self.trap[p+4] = graficos.create_image(40, 139*(p+1),
                                                       image=trampa_im[0])
        for i in range(4):  # Punto de llegada
            if i != 0:  # Punto sin trampa
                self.trap[i] = graficos.create_image(1035, 139*(i+1),
                                                     image=trampa_im[0])

        self.tiempo = 11  # String para el tiempo del nivel
        return self.trampas(), self.orbe_mov(), self.tiempo_bonus()

    def nivel_2(self):  # --- --- --- --- 15 Puentes

        self.len_x = 0
        self.len_y = 2
        self.orbe_x = 4
        self.orbe_y = 3

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
        self.puente13b = [graficos.create_image(154.5*3, 140,
                                                image=puente_x2_im), "x2"]
        self.puente14b = [graficos.create_image(154.5*4, 140,
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

        self.orbe = graficos.create_image(154.5*4, 140*3, image=red_orb1_im)
        graficos.lift(self.player)

        for p in range(4):  # Punto de partida
            if p != 1:  # Punto sin trampa
                self.trap[p+4] = graficos.create_image(40, 139*(p+1),
                                                       image=trampa_im[0])
        for i in range(4):  # Punto de llegada
            if i != 2:  # Punto sin trampa
                self.trap[i] = graficos.create_image(1035, 139*(i+1),
                                                     image=trampa_im[0])

        self.tiempo = 11  # String para el tiempo del nivel
        return self.trampas(), self.orbe_mov(), self.tiempo_bonus()

    def nivel_3(self):  # --- --- --- --- 18 Puentes

        self.len_x = 0
        self.len_y = 3
        self.orbe_x = 3
        self.orbe_y = 1

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
        self.puente34b = [graficos.create_image(154.5*4, 140*3,
                                                image=puente_f1ll2_im),
                          "f1ll2"]
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
        self.puente36b = [graficos.create_image(154.5*6, 140*3,
                                                image=puente_ac2_im), "ac2"]

        self.orbe = graficos.create_image(154.5*3, 140, image=red_orb1_im)
        graficos.lift(self.player)

        for p in range(4):  # Punto de partida
            if p != 2:  # Punto sin trampa
                self.trap[p+4] = graficos.create_image(40, 139*(p+1),
                                                       image=trampa_im[0])
        for i in range(4):  # Punto de llegada
            if i != 1:  # Punto sin trampa
                self.trap[i] = graficos.create_image(1035, 139*(i+1),
                                                     image=trampa_im[0])

        self.tiempo = 14  # String para el tiempo del nivel
        return self.trampas(), self.orbe_mov(), self.tiempo_bonus()

    def nivel_4(self):  # --- --- --- --- 17 Puentes

        self.len_x = 0
        self.len_y = 3
        self.orbe_x = 6
        self.orbe_y = 1

        self.piso = 4
        graficos.coords(self.player, 154.5*0.25, 140*3)

        self.puente21b = [graficos.create_image(154.5, 140*2,
                                                image=puente_bd2_im), "bd2"]
        self.puente31 = [graficos.create_image(154.5, 140*3,
                                               image=puente_bc_im), "bc"]
        self.puente41b = [graficos.create_image(154.5, 140*4,
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
        self.puente34b = [graficos.create_image(154.5*4, 140*3,
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
        self.puente36b = [graficos.create_image(154.5*6, 140*3,
                                                image=puente_abc2_im), "abc2"]

        self.orbe = graficos.create_image(154.5*6, 140, image=red_orb1_im)
        graficos.lift(self.player)

        for p in range(4):  # Punto de partida
            if p != 2:  # Punto sin trampa
                self.trap[p+4] = graficos.create_image(40, 139*(p+1),
                                                       image=trampa_im[0])
        for i in range(4):  # Punto de llegada
            if i != 2:  # Punto sin trampa
                self.trap[i] = graficos.create_image(1035, 139*(i+1),
                                                     image=trampa_im[0])

        self.tiempo = 11  # String para el tiempo del nivel
        return self.trampas(), self.orbe_mov(), self.tiempo_bonus()

    def nivel_5(self):  # --- --- --- --- 17 Puentes

        self.len_x = 0
        self.len_y = 1
        self.orbe_x = 2
        self.orbe_y = 1

        self.piso = 5
        graficos.coords(self.player, 154.5*0.25, 140)

        self.puente11 = [graficos.create_image(154.5, 140,
                                               image=puente_ac_im), "ac"]
        self.puente21b = [graficos.create_image(154.5, 140*2,
                                                image=puente_y2_im), "y2"]
        self.puente31 = [graficos.create_image(154.5, 140*3,
                                               image=puente_acd_im), "acd"]
        self.puente41b = [graficos.create_image(154.5, 140*4,
                                                image=puente_bc2_im), "bc2"]
        self.puente12b = [graficos.create_image(154.5*2, 140,
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
        self.puente15b = [graficos.create_image(154.5*5, 140,
                                                image=puente_x2_im), "x2"]
        self.puente25 = [graficos.create_image(154.5*5, 140*2,
                                               image=puente_y_im), "y"]
        self.puente16 = [graficos.create_image(154.5*6, 140,
                                               image=puente_ac_im), "ac"]
        self.puente26b = [graficos.create_image(154.5*6, 140*2,
                                                image=puente_abc2_im), "abc2"]

        self.orbe = graficos.create_image(154.5*2, 140, image=red_orb1_im)
        graficos.lift(self.player)

        for p in range(4):  # Punto de partida
            if p != 0:  # Punto sin trampa
                self.trap[p+4] = graficos.create_image(40, 139*(p+1),
                                                       image=trampa_im[0])
        for i in range(4):  # Punto de llegada
            if i != 1:  # Punto sin trampa
                self.trap[i] = graficos.create_image(1035, 139*(i+1),
                                                     image=trampa_im[0])

        self.tiempo = 13  # String para el tiempo del nivel
        return self.trampas(), self.orbe_mov(), self.tiempo_bonus()

    def nivel_6(self):  # --- --- --- --- 18 Puentes

        self.len_x = 0
        self.len_y = 2
        self.orbe_x = 3
        self.orbe_y = 2

        self.piso = 6
        graficos.coords(self.player, 154.5*0.25, 140*2)

        self.puente11 = [graficos.create_image(154.5, 140,
                                               image=puente_ac_im), "ac"]
        self.puente21 = [graficos.create_image(154.5, 140*2,
                                               image=puente_bc_im), "bc"]
        self.puente31b = [graficos.create_image(154.5, 140*3,
                                                image=puente_y2_im), "y2"]
        self.puente41 = [graficos.create_image(154.5, 140*4,
                                               image=puente_ac_im), "ac"]
        self.puente12b = [graficos.create_image(154.5*2, 140,
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
        self.puente24b = [graficos.create_image(154.5*4, 140*2,
                                                image=puente_ad2_im), "ad2"]
        self.puente34 = [graficos.create_image(154.5*4, 140*3,
                                               image=puente_ac_im), "ac"]
        self.puente44b = [graficos.create_image(154.5*4, 140*4,
                                                image=puente_x2_im), "x2"]
        self.puente35 = [graficos.create_image(154.5*5, 140*3,
                                               image=puente_y_im), "y"]
        self.puente45 = [graficos.create_image(154.5*5, 140*4,
                                               image=puente_acd_im), "acd"]
        self.puente36 = [graficos.create_image(154.5*6, 140*3,
                                               image=puente_abc_im), "abc"]
        self.puente46b = [graficos.create_image(154.5*6, 140*4,
                                                image=puente_ac2_im), "ac2"]

        self.orbe = graficos.create_image(154.5*3, 140*2, image=red_orb1_im)
        graficos.lift(self.player)

        for p in range(4):  # Punto de partida
            if p != 1:  # Punto sin trampa
                self.trap[p+4] = graficos.create_image(40, 139*(p+1),
                                                       image=trampa_im[0])
        for i in range(4):  # Punto de llegada
            if i != 2:  # Punto sin trampa
                self.trap[i] = graficos.create_image(1035, 139*(i+1),
                                                     image=trampa_im[0])

        self.tiempo = 10  # String para el tiempo del nivel
        return self.trampas(), self.orbe_mov(), self.tiempo_bonus()

    def nivel_7(self):  # --- --- --- --- 19 Puentes

        self.len_x = 0
        self.len_y = 4
        self.orbe_x = 5
        self.orbe_y = 1

        self.piso = 7
        graficos.coords(self.player, 154.5*0.25, 140*4)

        self.puente21 = [graficos.create_image(154.5, 140*2,
                                               image=puente_ad_im), "ad"]
        self.puente31 = [graficos.create_image(154.5, 140*3,
                                               image=puente_x_im), "x"]
        self.puente41 = [graficos.create_image(154.5, 140*4,
                                               image=puente_bc_im), "bc"]
        self.puente22b = [graficos.create_image(154.5*2, 140*2,
                                                image=puente_x2_im), "x2"]
        self.puente32b = [graficos.create_image(154.5*2, 140*3,
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
        self.puente34b = [graficos.create_image(154.5*4, 140*3,
                                                image=puente_ac2_im), "ac2"]
        self.puente44 = [graficos.create_image(154.5*4, 140*4,
                                               image=puente_y_im), "y"]
        self.puente15 = [graficos.create_image(154.5*5, 140,
                                               image=puente_ac_im), "ac"]
        self.puente25 = [graficos.create_image(154.5*5, 140*2,
                                               image=puente_ac_im), "ac"]
        self.puente35 = [graficos.create_image(154.5*5, 140*3,
                                               image=puente_x_im), "x"]
        self.puente45b = [graficos.create_image(154.5*5, 140*4,
                                                image=puente_ac2_im), "ac2"]
        self.puente26b = [graficos.create_image(154.5*6, 140*2,
                                                image=puente_x2_im), "x2"]

        self.orbe = graficos.create_image(154.5*5, 140, image=red_orb1_im)
        graficos.lift(self.player)

        for p in range(4):  # Punto de partida
            if p != 3:  # Punto sin trampa
                self.trap[p+4] = graficos.create_image(40, 139*(p+1),
                                                       image=trampa_im[0])
        for i in range(4):  # Punto de llegada
            if i != 1:  # Punto sin trampa
                self.trap[i] = graficos.create_image(1035, 139*(i+1),
                                                     image=trampa_im[0])

        self.tiempo = 11  # String para el tiempo del nivel
        return self.trampas(), self.orbe_mov(), self.tiempo_bonus()

    def nivel_8(self):  # --- --- --- --- 22 Puentes

        self.len_x = 0
        self.len_y = 1
        self.orbe_x = 4
        self.orbe_y = 4

        self.piso = 8
        graficos.coords(self.player, 154.5*0.25, 140)

        self.puente11 = [graficos.create_image(154.5, 140,
                                               image=puente_bd_im), "bd"]
        self.puente21 = [graficos.create_image(154.5, 140*2,
                                               image=puente_ad_im), "ad"]
        self.puente41 = [graficos.create_image(154.5, 140*4,
                                               image=puente_bd_im), "bd"]
        self.puente12b = [graficos.create_image(154.5*2, 140,
                                                image=puente_abd2_im), "abd2"]
        self.puente22 = [graficos.create_image(154.5*2, 140*2,
                                               image=puente_ac_im), "ac"]
        self.puente32 = [graficos.create_image(154.5*2, 140*3,
                                               image=puente_x_im), "x"]
        self.puente42 = [graficos.create_image(154.5*2, 140*4,
                                               image=puente_ad_im), "ad"]
        self.puente13 = [graficos.create_image(154.5*3, 140,
                                               image=puente_bcd_im), "bcd"]
        self.puente23b = [graficos.create_image(154.5*3, 140*2,
                                                image=puente_bc2_im), "bc2"]
        self.puente43 = [graficos.create_image(154.5*3, 140*4,
                                               image=puente_y_im), "y"]
        self.puente14 = [graficos.create_image(154.5*4, 140,
                                               image=puente_x_im), "x"]
        self.puente24 = [graficos.create_image(154.5*4, 140*2,
                                               image=puente_y_im), "y"]
        self.puente34 = [graficos.create_image(154.5*4, 140*3,
                                               image=puente_ad_im), "ad"]
        self.puente44b = [graficos.create_image(154.5*4, 140*4,
                                                image=puente_ac2_im), "ac2"]
        self.puente15 = [graficos.create_image(154.5*5, 140,
                                               image=puente_y_im), "y"]
        self.puente25 = [graficos.create_image(154.5*5, 140*2,
                                               image=puente_ac_im), "ac"]
        self.puente35 = [graficos.create_image(154.5*5, 140*3,
                                               image=puente_bd_im), "bd"]
        self.puente45 = [graficos.create_image(154.5*5, 140*4,
                                               image=puente_ac_im), "ac"]
        self.puente16b = [graficos.create_image(154.5*6, 140,
                                                image=puente_ad2_im), "ad2"]
        self.puente26 = [graficos.create_image(154.5*6, 140*2,
                                               image=puente_y_im), "y"]
        self.puente36b = [graficos.create_image(154.5*6, 140*3,
                                                image=puente_abd2_im), "abd2"]
        self.puente46 = [graficos.create_image(154.5*6, 140*4,
                                               image=puente_ad_im), "ad"]

        self.orbe = graficos.create_image(154.5*4, 140*4, image=red_orb1_im)
        graficos.lift(self.player)

        for p in range(4):  # Punto de partida
            if p != 0:  # Punto sin trampa
                self.trap[p+4] = graficos.create_image(40, 139*(p+1),
                                                       image=trampa_im[0])
        for i in range(4):  # Punto de llegada
            if i != 2:  # Punto sin trampa
                self.trap[i] = graficos.create_image(1035, 139*(i+1),
                                                     image=trampa_im[0])

        self.tiempo = 13  # String para el tiempo del nivel
        return self.trampas(), self.orbe_mov(), self.tiempo_bonus()

    def nivel_9(self):  # --- --- --- --- 23 Puentes / Final

        self.len_x = 0
        self.len_y = 3
        self.orbe_x = 5
        self.orbe_y = 1

        self.piso = 9
        graficos.coords(self.player, 154.5*0.25, 140*3)

        self.puente11b = [graficos.create_image(154.5, 140,
                                                image=puente_bd2_im), "bd2"]
        self.puente21 = [graficos.create_image(154.5, 140*2,
                                               image=puente_x_im), "x"]
        self.puente31 = [graficos.create_image(154.5, 140*3,
                                               image=puente_bd_im), "bd"]
        self.puente41 = [graficos.create_image(154.5, 140*4,
                                               image=puente_ad_im), "ad"]
        self.puente12 = [graficos.create_image(154.5*2, 140,
                                               image=puente_bc_im), "bc"]
        self.puente22 = [graficos.create_image(154.5*2, 140*2,
                                               image=puente_ad_im), "ad"]
        self.puente32b = [graficos.create_image(154.5*2, 140*3,
                                                image=puente_bc2_im), "bc2"]
        self.puente42 = [graficos.create_image(154.5*2, 140*4,
                                               image=puente_y_im), "y"]
        self.puente13b = [graficos.create_image(154.5*3, 140,
                                                image=puente_bd2_im), "bd2"]
        self.puente23 = [graficos.create_image(154.5*3, 140*2,
                                               image=puente_bd_im), "bd"]
        self.puente33 = [graficos.create_image(154.5*3, 140*3,
                                               image=puente_f1ll_im), "f1ll"]
        self.puente43b = [graficos.create_image(154.5*3, 140*4,
                                                image=puente_abc2_im), "abc2"]
        self.puente14 = [graficos.create_image(154.5*4, 140,
                                               image=puente_y_im), "y"]
        self.puente34 = [graficos.create_image(154.5*4, 140*3,
                                               image=puente_ac_im), "ac"]
        self.puente44 = [graficos.create_image(154.5*4, 140*4,
                                               image=puente_ad_im), "ad"]
        self.puente15 = [graficos.create_image(154.5*5, 140,
                                               image=puente_bc_im), "bc"]
        self.puente25 = [graficos.create_image(154.5*5, 140*2,
                                               image=puente_abc_im), "abc"]
        self.puente35b = [graficos.create_image(154.5*5, 140*3,
                                                image=puente_ac2_im), "ac2"]
        self.puente45 = [graficos.create_image(154.5*5, 140*4,
                                               image=puente_y_im), "y"]
        self.puente16 = [graficos.create_image(154.5*6, 140,
                                               image=puente_ac_im), "ac"]
        self.puente26b = [graficos.create_image(154.5*6, 140*2,
                                                image=puente_y2_im), "y2"]
        self.puente36 = [graficos.create_image(154.5*6, 140*3,
                                               image=puente_x_im), "x"]
        self.puente46b = [graficos.create_image(154.5*6, 140*4,
                                                image=puente_ac2_im), "ac2"]

        self.orbe = graficos.create_image(154.5*5, 140, image=red_orb1_im)
        graficos.lift(self.player)

        for p in range(4):  # Punto de partida
            if p != 2:  # Punto sin trampa
                self.trap[p+4] = graficos.create_image(40, 139*(p+1),
                                                       image=trampa_im[0])
        for i in range(4):  # Punto de llegada
            if i != 0:  # Punto sin trampa
                self.trap[i] = graficos.create_image(1035, 139*(i+1),
                                                     image=trampa_im[0])

        self.tiempo = 18  # String para el tiempo del nivel
        return self.trampas(), self.orbe_mov(), self.tiempo_bonus()

    def despausa(self):
        mixer.Sound.play(select1_se)
        self.interrupcion = False
        graficos.delete(self.cuadro, self.retorno, self.selector, self.salida)
        del self.reanudar, self.sele, self.exit
        graficos.bind("<Button-1>", self.giro)  # Giro de los caminos
        self.home.config(command=self.pausa)
        self.reinicio.config(command=self.reiniciar)
        graficos.update()

        return (self.nivel_ganado(), self.lava_mov(),  # Despausa animaciones
                self.trampas(), self.orbe_mov(), self.tiempo_bonus())

    def regresar(self, destino="selec", desbloqueado=1, puntos="00"):  # Return
        mixer.Sound.play(select1_se)
        self.interrupcion = True
        graficos.unbind("<Button-1>")
        graficos.delete("all")
        mixer.Channel(1).stop()

        if destino == "selec":  # Retorno + New Lvl
            return Seleccion().abrir_selector(self.char,
                                              desbloqueados=desbloqueado,
                                              punto=puntos)
        elif destino == "menu":
            return Menu().crear_menu()


Menu().crear_menu()

# -- -- -- Mainloop
if __name__ == "__main__":
    root.mainloop()
