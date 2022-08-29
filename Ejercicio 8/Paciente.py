class Paciente:
    __nombre = None
    __documento= None
    __tiempocola = None
    __tiempollegadacola = None
    __tiempoespecialidad = None
    __tiempollegadaEspecialidad = None

    def __init__(self,nomb=None,docu=None,llegada=None):
        self.__documento = docu
        self.__nombre = nomb
        self.__tiempollegadacola = llegada
        self.__tiempocola = 0
        self.__tiempoespecialidad = 0

    def setiempollegada(self,tiempo):
        self.__tiempollegadaEspecialidad = tiempo

    def calculartiempocola(self,tiempo):
        self.__tiempocola = tiempo - self.__tiempollegadacola
        return  self.__tiempocola
    def calculartiempoespecialidad(self,tiempo):
        self.__tiempoespecialidad = tiempo - self.__tiempollegadaEspecialidad
        return self.__tiempoespecialidad
    def getnombre(self):
        return self.__nombre
    def getdni(self):
        return self.__documento
