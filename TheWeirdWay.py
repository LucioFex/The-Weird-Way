from tkinter import Canvas, Frame, Tk, PhotoImage, Button

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
c_bg_fg = "#222027"
c_bg_press = "#1c1b20"

# -- -- -- Root

root = Tk()
root.title(titulo)
root.resizable(False, False)
root.geometry("{}x{}+{}+{}".format(ancho, alto, 245, 55))
root.iconbitmap("LucioPalIco.ico")
root.config(bg=c_fondo)

# -- -- -- Imagenes

logo_img = PhotoImage(file="Imagenes/Logo.png")

# -- -- -- Frame

pantalla = Frame(root, width=ancho, height=alto, bg=c_pantalla)
pantalla.pack()

# -- -- -- Canvas

graficos = Canvas(pantalla, width=ancho, height=alto, bg=c_pantalla,
                  borderwidth=0, highlightthickness=0)
graficos.pack()

# -- -- -- Botones Menu


class Menu:

    def crear_menu(self):
        self.num = alto
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

        self.logo = graficos.create_image(ancho/2, alto/2 - alto/4,
                                          image=logo_img)
        self.nueva = graficos.create_window(ancho/2, alto/2 + alto/50,
                                            window=self.nueva)
        self.continuar = graficos.create_window(ancho/2, alto/2 + alto/5,
                                                window=self.continuar)
        self.salir = graficos.create_window(ancho/2, alto/2 + alto/2.70,
                                            window=self.salir)

    def cerrar_menu(self, selected):
        self.num -= 75
        graficos.coords(self.ani_menu, -1, alto, ancho, self.num)
        if selected == "nueva":
            graficos.move(self.nueva, 0 - 90, 0)
        elif selected == "continuar":
            graficos.move(self.continuar, 0 + 90, 0)
        elif selected == "salir":
            graficos.move(self.salir, 0 - 90, 0)

        if self.num > -75:
            root.after(150, lambda: self.cerrar_menu(selected))

        else:
            graficos.delete("all")




jojer = Menu().crear_menu()

# -- -- -- Mainloop
if __name__ == "__main__":
    root.mainloop()
