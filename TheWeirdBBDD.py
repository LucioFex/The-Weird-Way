import pickle


class Memoria:

    """
    Almacenamiento de los niveles superados y
    estrellas recolectadas en partida.
    """

    def __init__(self):
        """
        Genera el archivo de guardado binario en caso de que no exista,
        si existe, le entrega a la variable 'contenido'."""
        with open("the_weird_save.pckl", "ab+") as fichero:
            fichero.seek(0)
            try:  # El fichero existe
                self.contenido = pickle.load(fichero)
            except EOFError:  # El fichero no existe
                self.contenido = [0, 0]
            fichero.close()

    def añadir(self, niveles, estrellas):
        """
        Añade los avances actuales, para luego
        almacenarlos en memoria llamando al método 'guardar'.
        """
        self.contenido = [niveles, estrellas]
        self.guardar()

    def guardar(self):
        """
        Guarda los avances.
        """
        fichero = open("the_weird_save.pckl", "wb")
        pickle.dump(self.contenido, fichero)
        fichero.close()

    def vaciar(self):
        """
        Restaura todos los avances obtenidos a 0.
        """
        fichero = open("the_weird_save.pckl", "wb")
        pickle.dump([0, 0], fichero)
        self.contenido = [0, 0]
        fichero.close()

    def cargar(self):
        """
        Carga los valores obtenidos, y los retorna en el método.
        """
        return self.contenido
