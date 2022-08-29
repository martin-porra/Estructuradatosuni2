from colasecuencial import Cola
from  ColaEnlazada import  ColaEnlazada
if __name__ == '__main__':
    colasec = Cola(10)
    colaenla = ColaEnlazada(10)
    colasec.insertar(2)
    colasec.insertar(3)
    colasec.recorrer()
    colaenla.insertar(2)
    colaenla.insertar(3)
    colaenla.insertar(3)
    colaenla.recorrer(1)
