from ClasePersonal import Personal

class Investigador(Personal):
    __Area=None
    __Tipo=None
    def __init__(self,Cuil,Apellido,Nombre,Sueldo,Antiguedad,Area,Tipo,Carrera,Cargo,Catedra):
        super().__init__(Cuil,Apellido,Nombre,Sueldo,Antiguedad,Area,Tipo,Carrera,Cargo,Catedra)
        self.__Area=Area
        self.__Tipo=Tipo
    def CalcularSueldo(self):
        return super().CalcularSueldo()
    def GetArea(self):
        return self.__Area
    def GetTipo(self):
        return self.__Tipo
    def __str__(self):
        return super().__str__()+"Investigador"
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self.GetCuil(),
                apellido=self.GetApellido(),
                nombre=self.GetNombre(),
                sueldo=self.GetSueldo(),
                antiguedad=self.GetAntiguedad(),
                area=self.__Area,
                tipo=self.__Tipo,
                carrera="",
                cargo="",
                catedra=""
            ))
        return d
