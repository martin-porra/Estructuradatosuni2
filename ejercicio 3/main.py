from pila import Pila
def factorizar(x):
    pila = Pila()
    i=1
    u=x
    for i in range(x):
        pila.insertar(u)
        u-=1

    cant=1
    i=1
    for i in range(x):
        cant=cant*pila.suprimir()
    print('El factorial del numero {} es {}'.format(x,cant))

if __name__ == '__main__':
    entero=int(input('Ingresar numero entero '))
    factorizar(entero)