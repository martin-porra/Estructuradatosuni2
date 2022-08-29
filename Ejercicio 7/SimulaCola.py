import  random
from ColaEnlazada import ColaEnlazada
from cliente import  Cliente
class Simulacion:
        __frecuenciaLlegada = None
        __tiempoAtencion = None
        __tiempoSimulacion = None
        __tiempoAcualCajero = None
        __tiempollegada = None
        __maximo = None
        __cajero = None
        __cola = None

        def __init__(self, tiempollega=None, tiempoatencion=None, tiempomaximo=None):
            self.__tiempoAtencion = tiempoatencion
            self.__tiempoSimulacion = tiempomaximo
            self.__frecuenciaLlegada = tiempollega
            self.__maximo = -1
            self.__tiempoActualCajero = 0
            self.__cajero = False
            self.__cola = ColaEnlazada()
            self.__tiempollegada = 1/ self.__frecuenciaLlegada
        def Simular(self):
            reloj = 0
            while reloj <= self.__tiempoSimulacion:
                self.llegaCliente(reloj)
                self.ManejaCajero(reloj)
                reloj += 1
            print("El tiempo maximo que espero un cliente fue: " + str(self.__maximo) + " minutos")

        def llegaCliente(self, reloj):
            if self.__tiempollegada == (1 / random.randint(1, self.__frecuenciaLlegada)):
                cliente = Cliente(reloj)
                self.__cola.insertar(cliente)

        def ManejaCajero(self, reloj):
            if self.__cajero == False:
                if self.__cola.vacia() == False:
                    cliente = self.__cola.suprimir()
                    tiempo = cliente.calcular(reloj)
                    self.__tiempoActualCajero = self.__tiempoAtencion
                    self.__cajero = True
                    if tiempo > self.__maximo:
                        self.__maximo = tiempo
            else:
                self.__tiempoActualCajero -= 1
                if self.__tiempoActualCajero == 0:
                    self.__cajero = False