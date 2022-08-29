import numpy as np


class Pila:
    cant = None
    tope = None
    arreglo = None

    def __init__(self, cant=10):
        self.cant = cant
        self.tope = -1
        self.arreglo = np.empty(self.cant, dtype=int)

    def incrementar(self, x):
        if self.tope < self.cant:
            self.tope += 1
            self.arreglo[self.tope] = x
        else:
            print('La pila no puede crecer mas')

    def vacia(self):
        return (self.tope == -1)

    def suprimir(self):
        valor = None
        if self.vacia():
            print('No se puede suprimir, pila vacia')
        else:
            valor = self.arreglo[self.tope]
            self.arreglo[self.tope] = 0
            self.tope -= 1
        return valor

    def retornar(self):
        return self.arreglo
    def mostrar(self):
        if self.vacia():
            print('pila vacia')
        else:
            tope = self.tope
            i = 1
            for i in range(self.tope+1):
                print('[',self.arreglo[tope],']')
                tope -= 1

    def mostrarsup(self):
        if self.vacia():
            print('pila vacia')
        else:
            while self.tope >= 0:
                print(self.suprimir())

    def getentero(self):
        return self.arreglo[self.tope]