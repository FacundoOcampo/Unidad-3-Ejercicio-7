from ClasePersonal import Personal

class PersonalApoyo(Personal):
    __Categoria=None
    def __init__(self,Cuil,Apellido,Nombre,Sueldo,Antiguedad,Categoria):
        if type(Categoria)==int:
            super().__init__(Cuil,Apellido,Nombre,Sueldo,Antiguedad)
            self.__Categoria=Categoria
        else:
            print("Error de creacion de Personal de Apoyo")
    def CalcularSueldo(self):
        sueldo=super().CalcularSueldo()
        if self.__Categoria<=10:
            sueldo=sueldo*1.1
        elif self.__Categoria>10 and self.__Categoria<=20:
            sueldo=sueldo*1.2
        elif self.__Categoria>=21 and self.__Categoria<=22:
            sueldo=sueldo*1.3
        return sueldo
    def __str__(self):
        return super().__str__()+"Personal de apoyo"
    def toJSON(self):
          d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self.GetCuil(),
                apellido=self.GetApellido(),
                nombre=self.GetNombre(),
                sueldobasico=self.GetSueldo(),
                antiguedad=self.GetAntiguedad(),
                categoria=self.__Categoria
            )
          )
          return d
