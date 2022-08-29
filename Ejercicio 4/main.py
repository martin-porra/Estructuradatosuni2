import numpy as np


class Arreglo2Pilas:
    tope1 = 0
    tope2 = 0
    arreglo = None

    def _init_(self, tamanio) -> None:
        self.tope1 = 0
        self.tope2 = int(tamanio) - 1
        self.arreglo = np.empty(int(tamanio), dtype=int)

    def IncrementarPila1(self, valor):
        if self.tope1 <= self.tope2 and self.tope1 <= len(self.arreglo):
            self.arreglo[self.tope1] = valor
            self.tope1 += 1
            print("Se incremento la pila 1")
        else:
            print("La pila 1 no puede crecer mas")

    def IncrementarPila2(self, valor):
        if self.tope1 <= self.tope2 and self.tope1 >= 0:
            self.arreglo[self.tope2] = valor
            self.tope2 -= 1
            print("Se incremento la pila 2")

        else:
            print("La pila 2 no puede crecer mas")

    def vacia1(self):
        return (self.tope1 == 0)

    def vacia2(self):
        return (self.tope2 == len(self.arreglo) - 1)

    def SuprimirPila1(self):
        valor_devolver = None
        if self.vacia1() == True:
            print("No se puede suprimir, pila 1 vacia")
        else:
            valor_devolver = self.arreglo[self.tope1 - 1]
            self.tope1 -= 1
        return valor_devolver

    def SuprimirPila2(self):
        valor_devolver = None
        if self.vacia2() == True:
            print("No se puede suprimir, pila 2 vacia")
        else:
            valor_devolver = self.arreglo[self.tope2 + 1]
            self.tope2 += 1
        return valor_devolver

    def Mostrar1(self):
        if self.vacia1() == True:
            print("Pila 1 Vacia")

        else:
            print("Pila 1: ")

            while self.tope1 > 0:
                print(self.SuprimirPila1())

    def Mostrar2(self):
        if self.vacia2() == True:
            print("Pila 2 vacia")
        else:
            print("Pila 2: ")
            while self.tope2 < len(self.arreglo) - 1:
                print(self.SuprimirPila2())