from Pila import  Pila

def binario(x):
    pila = Pila(10)
    resto = 0
    cant=x
    while x >1:
        z = int(x%2)
        x = int(x/2)
        pila.insertar(z)
    pila.insertar(x)
    print('El binario del numero {} es '.format(cant))
    pila.mostrar()
if __name__ == '__main__':
    print('Ingresar numero entero para pasar a binario ')
    entero = int(input())
    binario(entero)