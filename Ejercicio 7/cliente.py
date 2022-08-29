class Cliente:
        __tiempollegada = None
        __tiempo_espera = None

        def __init__(self,tiempo):
            self.__tiempollegada = tiempo
            self.__tiempoespera = 0

        def calcular(self, tiempo):
              self.__tiempoespera = tiempo - self.__tiempollegada
              return  self.__tiempoespera