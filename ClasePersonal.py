class Personal:
    __Cuil=None
    __Apellido=None
    __Nombre=None
    __Sueldo=None
    __Antiguedad=None
    def __init__(self,Cuil,Apellido,Nombre,Sueldo,Antiguedad,Area="",Tipo="",Carrera="",Cargo="",Catedra=""):
        if(type(Antiguedad)==int and type(Sueldo)==float):
            self.__Cuil=Cuil
            self.__Apellido=Apellido
            self.__Nombre=Nombre
            self.__Sueldo=Sueldo
            self.__Antiguedad=Antiguedad
        else:
            print("Error en la carga de personal")
    def GetSueldo(self):
        return self.__Sueldo
    def GetAntiguedad(self):
        return self.__Antiguedad
    def GetNombre(self):
        return self.__Nombre
    def GetApellido(self):
        return self.__Apellido
    def GetCuil(self):
        return self.__Cuil
    def CalcularSueldo(self):
        return self.GetSueldo()*(1+self.GetAntiguedad()/100)
    def __lt__(self, other):
        valor=None
        if (isinstance(self,Personal)and isinstance(other,Personal)):
            valor=(self.GetApellido()<other.GetApellido())
        else:
            print("No son del mismo tipo")
        return valor
    def __str__(self):
        return "{}, {}      Sueldo: {}       Tipo de investigacion:".format(self.GetApellido(),self.GetNombre(),self.CalcularSueldo())
    def toJSON(self):
        pass
