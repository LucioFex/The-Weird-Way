from tkinter import Canvas, Frame, Tk, PhotoImage, Label, Button

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
pantalla.grid(pady=alto/20)

# -- -- -- Canvas

graficos = Canvas(pantalla, width=ancho, height=alto, bg=c_pantalla,
                  borderwidth=0, highlightthickness=0)
graficos.grid(pady=alto/20)

# -- -- -- Botones Menu


class Menu:
    def crear_menu(self):
        self.num = 0

        self.ani_menu = graficos.create_rectangle(0, 0, ancho, 0)
        self.logo = Label(graficos, image=logo_img, bg=c_pantalla)

        self.nueva = Button(graficos, text="Nueva Partida", fg=c_fg,
                            cursor="hand2", font=("Century Gothic", 20),
                            bg=c_bg_fg, width=30, command=self.cerrar_menu,
                            activeforeground=c_fg, activebackground=c_bg_press)

        self.continuar = Button(graficos, text="Continuar Partida", fg=c_fg,
                                cursor="hand2", font=("Century Gothic", 20),
                                bg=c_bg_fg, width=27, activeforeground=c_fg,
                                activebackground=c_bg_press,
                                command=self.cerrar_menu)

        self.salir = Button(graficos, text="Salir", fg=c_fg, cursor="hand2",
                            font=("Century Gothic", 20), bg=c_bg_fg, width=24,
                            activeforeground=c_fg, activebackground=c_bg_press,
                            command=self.cerrar_menu)

        self.logo.grid(padx=ancho/6, row=0, column=0)
        self.nueva.grid(pady=19, row=1, column=0)
        self.continuar.grid(pady=20, row=2, column=0)
        self.salir.grid(pady=19, row=3, column=0)

    def cerrar_menu(self):
        self.num += 5
        graficos.coords(self.ani_menu, 0, 0, ancho, self.num)
        if self.num != 675:
            root.after(1000, self.cerrar_menu)

        else:
            self.logo.grid_remove()
            self.nueva.grid_remove()
            self.continuar.grid_remove()
            self.salir.grid_remove()


jojer = Menu().crear_menu()

# -- -- -- Mainloop
if __name__ == "__main__":
    root.mainloop()
