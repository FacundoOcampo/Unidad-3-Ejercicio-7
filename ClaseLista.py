from zope.interface import implementer
from ClassNodo import Nodos
from ClassInterfaz import Interfaz
@implementer(Interfaz)

class List:
    __Comienzo=None
    __Actual=None
    __Indice=0
    __Tope=0
    def __init__(self):
        self.__Comienzo=None
        self.__Actual=None
        self.__Indice=0
        self.__Tope=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.__Tope==self.__Indice:
            self.__Actual=self.__Comienzo
            self.__Indice=0
            raise StopIteration
        else:
            self.__Indice+=1
            dato=self.__Actual.GetDato()
            self.__Actual=self.__Actual.GetSiguiente()
            return dato
    def AgregarElemento(self,Elemento):
        Nodo=Nodos(Elemento)
        Nodo.SetSiguiente(self.__Comienzo)
        self.__Comienzo=Nodo
        self.__Actual=Nodo
        self.__Tope+=1

    def InsertarElemento(self,Elemento,Posicion):
        self.__Actual=self.__Comienzo
        self.__Indice=0
        ant=None
        if Posicion==0:
            self.AgregarElemento(Elemento)
        else:
            while self.__Indice!=Posicion and self.__Actual!=None:
                ant=self.__Actual
                self.__Actual=self.__Actual.GetSiguiente()
                self.__Indice+=1
            if self.__Indice==Posicion:
                NuevoNodo=Nodos(Elemento)
                NuevoNodo.SetSiguiente(self.__Actual)
                ant.SetSiguiente(NuevoNodo)
                self.__Tope+=1
                self.__Indice=0
                self.__Actual=self.__Comienzo
            else:
                raise IndexError

    def MostrarElemento(self,Posicion):
        Valor=None
        if self.__Tope<=Posicion or Posicion<0:
            print("Posicion indicada no valida")
        else:
            self.__Actual=self.__Comienzo
            self.__Indice=0
            while (self.__Indice != Posicion):
                self.__Actual=self.__Actual.GetSiguiente()
                self.__Indice+=1
            Valor=type(self.__Actual.GetDato())
        return Valor
    def toJSON(self):
        d=dict(__class__=self.__class__.__name__,Personal=[persona.toJSON() for persona in self])
        return d
