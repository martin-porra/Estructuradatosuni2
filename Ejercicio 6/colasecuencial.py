import numpy as np
class Cola:
    __items  =None
    __max = None
    __pr = None
    __ul = None
    __cant = None
    def __init__(self, max=0):
     self.__max = max
     self.__pr = 0
     self.__ul = 0
     self.__cant = 0
     self.__items = np.empty(self.__max,dtype=int)
    def vacia(self):
     return (self.__cant == 0)
    def insertar(self,x):
     item = 0
     if (self.__cant < self.__max):
      self.__items[self.__ul] = x
      self.__ul = (self.__ul + 1) % self.__max
      self.__cant+=1
      item =  x
     return item
    def suprimir(self):
     x = None
     if self.vacia():
      print("Pila vacia")
      return 0
     else:
      x = self.__items[self.__pr]
      self.__pr = (self.__pr + 1) % self.__max
      self.__cant-=1
     return x
    def recorrer(self):
     if not self.vacia():
      i=self.__pr
      for i in range(self.__cant):
          print(self.__items[i])