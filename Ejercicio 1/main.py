import numpy as np
from pilaenla import Pilaanidada

class Pila:
    __arreglo = None
    __tope = None
    __cant = None
    def __init__(self,cant):
        self.__tope = -1
        self.__cant = 10
        self.__arreglo = np.empty(self.__cant,dtype=int)
    def vacia(self):
        band = False
        if self.__tope == -1:
            band = True
        else:
            band = False
        return band
    def insertar(self,x):
        if self.__tope<(self.__cant-1):
            self.__tope+=1
            self.__arreglo[self.__tope] = x
        return x
    def suprimir(self):
        x = None
        if self.vacia():
            print('Pila vacia')
            return 0
        else:
            x=self.__arreglo[self.__tope]
            self.__tope-=1
        return x
    def mostrar(self):
        i = self.__tope
        if not self.vacia():
            while i >=0:
              print(self.suprimir())
              i -= 1
        else:
            print('Pila Vacia')

if __name__ == '__main__':
    pila = Pila(10)
    pila.insertar(1)
    pila.insertar(2)
    pila.insertar(3)
    pila.insertar(4)
    pila.mostrar()
    pila.mostrar()
    print('Pila anidada')
    pilaanidada = Pilaanidada()
    pilaanidada.insertar(1)
    pilaanidada.insertar(2)
    pilaanidada.mostrar()
    pilaanidada.mostrar()