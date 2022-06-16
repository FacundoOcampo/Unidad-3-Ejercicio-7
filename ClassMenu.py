from ClaseDocente import Docente
from ClaseInvestigador import Investigador
from ClaseDocenteInvestigador import DocenteInv
from ClassPersonalApoyo import PersonalApoyo
from ObjectEncoder import ObjetEncoder
class Menu:
    __Switcher=None
    def __init__(self):
        self.__Switcher={
            1:self.Opcion1,
            2:self.Opcion2,
            3:self.Opcion3,
            4:self.Opcion4,
            5:self.Opcion5,
            6:self.Opcion6,
            7:self.Opcion7,
            8:self.Opcion8,
            0:self.Salir
        }
    def Opciones(self,Op,Lista):
        func=self.__Switcher.get(Op, lambda :print("Numero ingresado no valido"))
        if Op<9 and Op>=0:
            func(Lista)
        else:
            func()
    def CrearElemento(self):
        op=input("Ingrese un miembro del personal: 1_ Docente,2_ Investigador,3_Docente Investigador,4_ Personal de Apoyo:\n")
        cuil=input("Ingrese el cuil:")
        nombre=input("Ingrese el nombre:")
        apellido=input("Ingrese el apellido:")
        sueldo=float(input("Ingrese el sueldo:"))
        antiguedad=int(input("Ingrese antiguedad:"))
        Band=True
        while(Band):
            if op=="1":
                Carrera=input("Ingrese la carrera:")
                Catedra=input("Ingrese la catedra:")
                Cargo=input("Ingrese el cargo:")
                Area=tipo=''
                elemento=Docente(cuil,apellido,nombre,sueldo,antiguedad,Area,tipo,Carrera,Cargo,Catedra)
                Band=False
            elif op=="2":
                Area=input("Ingrese el area:")
                tipo=input("Ingrese el tipo de investigacion:")
                Carrera=Cargo=Catedra=''
                elemento=Investigador(cuil,apellido,nombre,sueldo,antiguedad,Area,tipo,Carrera,Cargo,Catedra)
                Band=False
            elif op=="3":
                Area=input("Ingrese el area:")
                tipo=input("Ingrese el tipo de investigacion:")
                Carrera=input("Ingrese la carrera:")
                Catedra=input("Ingrese la catedra:")
                Cargo=input("Ingrese el cargo:")
                Categoria=input("Ingrese la categoria:")
                Importe=float(input("Ingrese el importe:"))
                elemento=DocenteInv(cuil,apellido,nombre,sueldo,antiguedad,Area,tipo,Carrera,Cargo,Catedra,Categoria,Importe)
                Band=False
            elif op=="4":
                Categoria=int(input("Ingrese una categoria"))
                elemento=PersonalApoyo(cuil,apellido,nombre,sueldo,antiguedad,Categoria)
                Band=False
            else:
                print("Opcion Incorrecta")
                op=input("Ingrese un miembro del personal: 1_ Docente,2_ Investigador,3_Docente Investigador,4_ Personal de Apoyo:\n")
        return elemento
    def Opcion1(self,Lista):
        Elemento=self.CrearElemento()
        Band=True
        while Band:
            try:
                Pocicion=int(input("Ingrese una posicion:"))
                Lista.InsertarElemento(Elemento,Pocicion-1)
                Band= not(Band)
            except IndexError:
                print("Indice no valido")
    def Opcion2(self,Lista):
        elemento=self.CrearElemento()
        Lista.AgregarElemento(elemento)
    def Opcion3(self,Lista):
        Band=True
        while Band:
            try:
                Posicion=int(input("Ingrese una posicion:"))
                print(Lista.MostrarElemento(Posicion-1))
                Band=not(Band)
            except IndexError:
                print("Indice no valido")
    def Opcion4(self,Lista):
        Listado=[]
        i=0
        for agente in Lista:
            if type(agente)==DocenteInv:
                Listado.append(agente)
        Listado.sort()
        for agente in Listado:
            print(agente)
    def Opcion5(self,Lista):
        area=input("Ingrese un area de investigacion:")
        cont=0
        contAux=0
        for agente in Lista:
            if type(agente)==Investigador and agente.GetArea()==area:
                cont+=1
            if type(agente)==DocenteInv and agente.GetArea()==area:
                contAux+=1
        print("La cantidad de investigadores en el area es de {}\nLa cantidad de docentes investigadores en el area es de {}\n".format(cont,contAux))
    def Opcion6(self,Lista):
        Listado=[]
        for agente in Lista:
            Listado.append(agente)
        Listado.sort()
        for elemento in Listado:
            print(elemento)
    def Opcion7(self,Lista):
        Cat=input("Ingrese una categoria (I,II,III, o IV):")
        total=0
        for agente in Lista:
            if type(agente)==DocenteInv and agente.GetCategoria()==Cat:
                print(agente)
                total+=agente.GetImporte()
        print("El importe total es: {}".format(total))
    def Opcion8(self,Lista):
        jsonF=ObjetEncoder()
        d=Lista.toJSON()
        jsonF.GuardarJSONArchivo(d,"Personal.json")
    def Salir(self):
        print("Usted ha salido con exito")
