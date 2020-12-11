import pickle


class Memoria:
    """
    Almacenamiento de los niveles superados y
    estrellas recolectadas en partida.
    """

    def __init__(self):
        """Genera el archivo de guardado binario en caso de que no exista,
        si existe, le entrega a la variable 'contenido'."""
        with open("the_weird_save.pckl", "ab+") as fichero:
            fichero.seek(0)
            try:  # El fichero existe
                self.contenido = pickle.load(fichero)
            except EOFError:  # El fichero no existe
                self.contenido = [1, ["10", "20", "30", "40", "50",
                                      "60", "70", "80", "90"], "dross"]
            fichero.close()
        self.guardar()

    def añadir_n(self, niveles):
        """Añade la suma de todos los niveles completados."""
        self.contenido[0] = niveles
        return self.guardar()

    def añadir_e(self, estrellas):
        """Añade la lista de todas las estrellas ganadas en los niveles."""
        self.contenido[1] = estrellas
        return self.guardar()

    def añadir_p(self, personaje):
        """Retorna el actual personaje en uso."""
        self.contenido[2] = personaje
        return self.guardar()

    def guardar(self):
        """Guarda los avances."""
        fichero = open("the_weird_save.pckl", "wb")
        pickle.dump(self.contenido, fichero)
        fichero.close()

    def vaciar(self):
        """Restaura todos los avances obtenidos a 0."""
        fichero = open("the_weird_save.pckl", "wb")
        self.contenido = [1, ["10", "20", "30", "40", "50",
                              "60", "70", "80", "90"], "dross"]
        pickle.dump(self.contenido, fichero)
        fichero.close()

    def cargar(self):
        """Carga los valores obtenidos, y los retorna en el método."""
        return self.contenido


# c = Memoria()
# c.añadir(1, ["10", "20", "30", "40", "50", "60", "70", "80", "90"], "dross")
# print(c.cargar())
# del c
