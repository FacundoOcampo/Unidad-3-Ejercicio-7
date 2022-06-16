from ClasePersonal import Personal
class Nodos:
    __Siguiente=None
    __Dato=None
    def __init__(self,persona):
        if(isinstance(persona,Personal)):
            self.__Dato=persona
            self.__Siguiente=None
        else:
            print("Error al ingreso de datos al nodo")
    def GetSiguiente(self):
        return self.__Siguiente
    def SetSiguiente(self,Pos):
        self.__Siguiente=Pos
    def GetDato(self):
        return self.__Dato
