import random
import numpy as np
from Especialidad import Especialidad
from Paciente import Paciente
from ColaEnlazada import ColaEnlazada

class simulador:
    __lista_nombres = ['Ginecologia', 'Clinica Medica', 'Oftalmologia', 'Pediatria']
    __manejadorEspecialidades = None
    __cola_turnos = None
    __F_Pacientes = 1
    __contador_tAtencion = 0
    __atencion_medicos = 0
    __cant_pacientes_cola = 0
    __cant_pacientes_atendidos = 0
    __tiempos_espera_pacientes = 0
    __tiempos_espera_especialidad = 0
    __tiempototal = 0

    def __init__(self):
        self.__cola_turnos = ColaEnlazada()
        self.__manejadorEspecialidades = np.empty(4, dtype=Especialidad)
        for i in range(4):
         self.__manejadorEspecialidades[i] = Especialidad(self.__lista_nombres[i])

    def simular(self):
        while self.__tiempototal <=10:
            if 1/self.__F_Pacientes > 1/(random.randint(1,3)):
              print('Llego un paciente ingrese sus datos')
              nombre = input('Ingrese el nombre: ')
              dni = input('Ingrese el dni del paciente: ')
              paciente = Paciente(nombre, dni, self.__tiempototal)
              self.__cola_turnos.insertar(paciente)
              self.__cant_pacientes_cola += 1

            if self.__tiempototal <= 5:
                self.__contador_tAtencion+=1
                if self.__contador_tAtencion == 2:
                    if not self.__cola_turnos.vacia():
                        pacienteAtender = self.__cola_turnos.suprimir()
                        print('Elija la especialidad a la que desea obtener el turno')
                        print('1- Ginecologia\n2-Clinica Medica\n3-Oftamologia\n4-Pediatria')
                        numero = int(input('Ingrese una opcion: '))
                        while numero < 1 or numero > 4:
                            print('ERROR: Entrada invalida, ingrese un numero del 1 al 4')
                            numero = int(input('Ingrese una opcion: '))
                        if not self.__manejadorEspecialidades[numero - 1].lleno():
                            self.__manejadorEspecialidades[numero - 1].agregarpaciente(pacienteAtender, self.__tiempototal)
                            self.__contador_tAtencion = 0
                            self.__cant_pacientes_atendidos += 1
                            self.__tiempos_espera_pacientes += pacienteAtender.calculartiempocola(self.__tiempototal)
                        else:
                            self.__contador_tAtencion = 0
                    else:
                        self.__contador_tAtencion = 0
            else:
                self.__atencion_medicos += 1
                if self.__atencion_medicos == 2:
                    self.__atencion_medicos = 0
                    for j in range(3):
                        if not self.__manejadorEspecialidades[j].vacia():
                            print('Se atedio a un paciente en la especialidad {}'.format(self.__manejadorEspecialidades[j].getnombre()))
                            paciente_atendido = self.__manejadorEspecialidades[j].atender(self.__tiempototal)
                            print('Nombre del paciente: {}'.format(paciente_atendido.getnombre()))
            self.__tiempototal += 1
        print('--- \t ------------------------------------- \t---')
        if self.__cant_pacientes_atendidos != 0:
            print('Tiempo de espera promedio de los pacientes en la cola de turno: {0: .2f}  minutos'.format(self.__tiempos_espera_pacientes / self.__cant_pacientes_atendidos))
        else:
            print('No hubieron pacientes atedidos!')

        print('--- \tTiempos promedio de espera en la cola de cada especialidad \t---')
        for k in range(4):
            print('Promedio en la especialidad {}: {} minutos'.format(self.__manejadorEspecialidades[k].getnombre(),self.__manejadorEspecialidades[k].calcularpromedio()))
        print('Cantidad de pacientes que no pudieron obtener turno: {}'.format(self.__cant_pacientes_cola - self.__cant_pacientes_atendidos))