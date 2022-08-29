from SimulaCola import Simulacion

if __name__ == '__main__':
 tiempoatencioncajero= int(input('Ingresar tiempo de atencion del cajero '))
 frecuenciallegada=  int(input('Ingresar frecuencia de llegada de clientes '))
 tiempomaximo= int(input('Ingresar tiempo maximo de simulacion '))
 simular = Simulacion(frecuenciallegada , tiempoatencioncajero , tiempomaximo)
 simular.Simular()