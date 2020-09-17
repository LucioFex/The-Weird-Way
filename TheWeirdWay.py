from tkinter import Canvas, Frame, Tk, PhotoImage, Label

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

# -- -- -- Root

root = Tk()
root.title(titulo)
root.resizable(False, False)
root.geometry("{}x{}+{}+{}".format(ancho, alto, 215, 55))
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

        # Logo
        # graficos.create_image(ancho / 2, alto / 5, image=logo_img)
        logo = Label(graficos, fg="red", image=logo_img, bg=c_pantalla)

        nueva = Label(graficos, text="Nueva Partida", fg=c_fg,
                      cursor="hand2", font=("Century Gothic", 20),
                      bg=c_bg_fg, width=30)

        continuar = Label(graficos, text="Continuar Partida", fg=c_fg,
                          cursor="hand2", font=("Century Gothic", 20),
                          bg=c_bg_fg, width=27)

        salir = Label(graficos, text="Salir", fg=c_fg, cursor="hand2",
                      font=("Century Gothic", 20), bg=c_bg_fg, width=24)

        logo.grid(padx=ancho/6, row=0, column=0)
        nueva.grid(pady=30, row=1, column=0)
        continuar.grid(pady=30, row=2, column=0)
        salir.grid(pady=15, row=3, column=0)


jojer = Menu()
jojer.crear_menu()

# -- -- -- Mainloop
root.mainloop()
