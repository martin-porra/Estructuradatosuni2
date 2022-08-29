from colasecuencial import Cola
from Paciente import  Paciente

class Especialidad:
    __nombre = None
    __cola = None
    __cantpaciente = None
    __contadortimepacientes = None
    __cantatendidos = None

    def __init__(self,nombre):
        self.__nombre = nombre
        self.__cantatendidos = 0
        self.__contadortimepacientes = 0
        self.__cantpaciente = 0
        self.__cola = Cola(10)
    def getnombre(self):
        return self.__nombre

    def getcant(self):
        return self.__cantatendidos

    def getcantidadpaciente(self):
        return self.__cantpaciente
    def lleno(self):
        return (self.__cantpaciente == 10)

    def vacia(self):
        return (self.__cantpaciente == 0)

    def agregarpaciente(self,paciente,tiempo):
        if not self.lleno():
            paciente.setiempollegada(tiempo)
            self.__cola.insertar(paciente)
            self.__cantpaciente+=1

    def atender(self,tiempo):
        paciente = self.__cola.suprimir()
        self.incrementarcont(paciente.calculartiempoespecialidad(tiempo))
        self.__cantpaciente-=1
        self.__cantatendidos+=1
        return paciente


    def incrementarcont(self,tiempo):
        self.__contadortimepacientes += tiempo

    def calcularpromedio(self):
        promedio = 0
        if self.__cantatendidos != 0:
            promedio = self.__contadortimepacientes/self.__cantatendidos
        return promedio
