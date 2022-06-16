from ClasePersonal import Personal
class Docente(Personal):
    __Carrera=None
    __Cargo=None
    __Catedra=None
    def __init__(self,Cuil,Apellido,Nombre,Sueldo,Antiguedad,Area,Tipo,Carrera,Cargo,Catedra):
        super().__init__(Cuil,Apellido,Nombre,Sueldo,Antiguedad,Area,Tipo,Carrera,Cargo,Catedra)
        self.__Carrera=Carrera
        self.__Cargo=Cargo
        self.__Catedra=Catedra
    def GetCarrera(self):
        return self.__Carrera
    def GetCargo(self):
        return self.__Cargo
    def GetCatedra(self):
        return self.__Catedra
    def __str__(self):
        return (super().__str__()+"Docente")
    def CalcularSueldo(self):
        valor=super().CalcularSueldo()
        if self.__Cargo=="Simple":
            valor=valor*1.1
        elif self.__Cargo=="Semiexclusivo":
            valor=valor*1.2
        elif self.__Cargo=="Exclusivo":
            valor=valor*1.5
        return valor
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self.GetCuil(),
                apellido=self.GetApellido(),
                nombre=self.GetNombre(),
                sueldo=self.GetSueldo(),
                antiguedad=self.GetAntiguedad(),
                area="",
                tipo="",
                carrera=self.__Carrera,
                cargo=self.__Cargo,
                catedra=self.__Catedra
        ))
        return d
