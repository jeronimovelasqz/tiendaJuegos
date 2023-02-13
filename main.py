import datetime
# tienda de video juegos
class Administrador_Stock:
    def __init__(self,gow1: int = 0, gow2: int = 0,gow3: int = 0, gow4: int = 0):

        self.gow1: int = gow1
        self.gow2: int = gow2
        self.gow3: int = gow3
        self.gow4: int = gow4

        self.stock: int = gow1 + gow2 + gow3 + gow4
        self.catalogo: list = ["gow1", "gow2", "gow3", "gow4"]
        self.juegos: int = 0


    def mostrar_stock(self):
        print(f"actualmente tenemos los juegos {[juego for juego in self.catalogo]}")

    def modificar_stock(self):
        modificar = int(input("usted esta a punto de modificar el catalogo de juegos,\n"
                              "presione 1 para modificar el gow1,\n"
                              "presione 2 para modificar el gow2,\n"
                              "presione 3 para modificar el gow3,\n"
                              "presione 4 para modificar el gow4,\n"
                              "presione 5 para modificar todos los anteriores"
                              "presione 6 para salir"))
        if modificar == 1:
            self.gow1 = int(input(f"actualice la cantidad de unidades del gow 1 , actualmente hay {self.gow1}"))
        if modificar == 2:
            self.gow2 = int(input(f"actualice la cantidad de unidades del gow 2 , actualmente hay {self.gow2}"))
        if modificar == 3:
            self.gow3 = int(input(f"actualice la cantidad de unidades del gow 3 , actualmente hay {self.gow3}"))
        if modificar == 4:
            self.gow3 = int(input(f"actualice la cantidad de unidades del gow 4 , actualmente hay {self.gow4}"))
        if modificar == 5:
            self.gow1 = int(input(f"actualice la cantidad de unidades del gow 1 , actualmente hay {self.gow1}"))
            self.gow2 = int(input(f"actualice la cantidad de unidades del gow 2 , actualmente hay {self.gow2}"))
            self.gow3 = int(input(f"actualice la cantidad de unidades del gow 3 , actualmente hay {self.gow3}"))
            self.gow4 = int(input(f"actualice la cantidad de unidades del gow 4 , actualmente hay {self.gow4}"))
        if modificar == 6:
            return None

    def agregar_juego(self):
        print("usted esta a punto de agregar mas juegos al catalogo de juegos actuales,\n")

        juego = str(input("copie el juego  que desea agregar a la tienda"))
        cantidad = int(input(f"copie la cantidad de unidades de {juego}"))

        setattr(self, juego, cantidad)
        self.catalogo.append(juego)
        self.stock += cantidad



eso = Administrador_Stock()


