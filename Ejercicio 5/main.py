from cmath import pi
from ClasePila import Pila

def jugar():
    contador = 0
    x = int(input('Ingrese el numero de discos con los que se jugara '))
    jugadasmin= (2**x) - 1
    pila1 = Pila(x)
    pila2 = Pila(x)
    pila3 = Pila(x)
    for i in range(x,0,-1):
        pila1.incrementar(i)
    band1 = pila1.vacia()
    band2 = pila2.vacia()
    while not band1 or not band2:
        print('Ingresar Pila de la cual Desapilar y Pila a la cual Apilar ')
        print('1 2 3')
        desapilar = int(input('desapilar '))
        apilar = int(input('apilar '))
        if apilar != desapilar:
            if desapilar == 1:
                x = pila1.getentero()
                if not pila1.vacia():
                    if apilar == 2:
                        b = pila2.getentero()
                        if x < b or pila2.vacia():
                            pila1.suprimir()
                            pila2.incrementar(x)
                            contador += 1
                    else:
                        b = pila3.getentero()
                        if x < b or pila3.vacia():
                         pila1.suprimir()
                         pila3.incrementar(x)
                         contador += 1
            elif desapilar == 2:
                x = pila2.getentero()
                if not pila2.vacia():
                    if apilar == 1:
                         b = pila1.getentero()
                         if x < b or pila1.vacia():
                          pila2.suprimir()
                          pila1.incrementar(x)
                          contador += 1
                    else:
                        b = pila3.getentero()
                        if x < b or pila3.vacia():
                         x = pila2.suprimir()
                         pila3.incrementar(x)
                         contador += 1
            elif desapilar == 3:
                x = pila3.getentero()
                if not pila3.vacia():
                    if apilar == 2:
                        b = pila2.getentero()
                        if x < b or pila2.vacia():
                         pila3.suprimir()
                         pila2.incrementar(x)
                         contador += 1
                    else:
                        b = pila1.getentero()
                        if x < b or pila1.vacia():
                          pila3.suprimir()
                          pila1.incrementar(x)
                          contador+=1
        print('Pila 1 ')
        pila1.mostrar()
        print('pila 2')
        pila2.mostrar()
        print('pila 3')
        pila3.mostrar()
        band1 = pila1.vacia()
        band2 = pila2.vacia()
    print('Gano el Juego!')
    print('El numero de jugadas que hizo es {} y el de jugadas minimas para ganar eran {}'.format(contador,jugadasmin))

if __name__ == '__main__':
    jugar()