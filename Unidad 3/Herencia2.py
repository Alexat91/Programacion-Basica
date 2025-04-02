# Herencia
# Clase base o padre
class Cantantes:
    def __init__(self, nombre, genero):
        self.nombre = nombre
        self.genero = genero

    def presentarse(self):
        return f"Hola, me llamo {self.nombre} y canto música del genero {self.genero} ."


class Discos(Discos):
    def __init__(self, nombre, precio, cantante):
        super().__init__(nombre, precio, cantante)
        self.precio = precio

    def presentarse(self):
        return f"Este album es de  {self.nombre}, se llama {self.tituloa} y cuesta  {self.precio}."


# Clase derivada o hija
class Cancion(Cancion):
    def __init__(self, nombre, titulo, tiempo):
        super().__init__(nombre, tiempo, titulo)  # Llamada al constructor de la clase padre
        self.tiempo = tiempo

    def presentarse(self):
        # Sobrescribimos el método de la clase padre
        return f"La  cancion es de  {self.nombre}, dura {self.tiempo} y el titulo es {self.titulo}."


# Programa principal
if __name__ == "__main__":
    cantantes = Cantantes("Jenni Rivera", "Regional Mexicano")
    discos = Discos("Jenni RIvera", "X", "$300")
    cancion = Cancion("Jenni Rivera", "2.45 min", "X")

    print(cantantes.presentarse())
    print(discos.presentarse())
    print(cancion.presentarse())