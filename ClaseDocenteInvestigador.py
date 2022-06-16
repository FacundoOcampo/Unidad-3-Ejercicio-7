from ClaseDocente import Docente
from ClaseInvestigador import Investigador

class DocenteInv(Docente,Investigador):
    __Categoria=None
    __Importe=None
    def __init__(self,Cuil,Apellido,Nombre,Sueldo,Antiguedad,Area,Tipo,Carrera,Cargo,Catedra,Categoria,Importe):
        super().__init__(Cuil,Apellido,Nombre,Sueldo,Antiguedad,Area,Tipo,Carrera,Cargo,Catedra)
        self.__Categoria=Categoria
        self.__Importe=Importe
    def GetCategoria(self):
        return self.__Categoria
    def GetImporte(self):
        return self.__Importe
    def CalcularSueldo(self):
        return super().CalcularSueldo()+self.__Importe
    def __str__(self):
        return super().__str__()
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self.GetCuil(),
                apellido=self.GetApellido(),
                nombre=self.GetNombre(),
                sueldo=self.GetSueldo(),
                antiguedad=self.GetAntiguedad(),
                categoria=self.__Categoria,
                importe=self.__Importe,
                area=self.GetArea(),
                tipo=self.GetTipo(),
                carrera=self.GetCarrera(),
                cargo=self.GetCargo(),
                catedra=self.GetCatedra()
            ))
        return d
