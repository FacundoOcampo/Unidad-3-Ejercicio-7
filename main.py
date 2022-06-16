import json
from ObjectEncoder import ObjetEncoder
from ClassMenu import Menu
from ClaseLista import List
if __name__ == '__main__':
    Json=ObjetEncoder()
    Lista=List()
    diccionario=Json.LeerJSONArchivo("Personal.json")
    #Lista=Json.DecodificarDiccionario(diccionario)
    NuevoMenu=Menu()
    Op=int(input("Ingrese una opcion:\n1_Insertar un agente.\n2_Agregar un agente.\n3_Mostrar tipo de agente en una posicion.\n4_Generar listado de docentes investigadores.\n5_Cantidad de investigadores y docentes investigadores en un área.\n6_Listado con nombre apellido y tipo de agente ordenado.\n7_ Listar docentes investigadores de una categoria.\n8_ Guardar datos\n0_Salir.\n"))
    NuevoMenu.Opciones(Op,Lista)
    while(Op!=0):
        Op=int(input("Ingrese una opcion:\n1_Insertar un agente.\n2_Agregar un agente.\n3_Mostrar tipo de agente en una posicion.\n4_Generar listado de docentes investigadores.\n5_Cantidad de investigadores y docentes investigadores en un área.\n6_Listado con nombre apellido y tipo de agente ordenado.\n7_ Listar docentes investigadores de una categoria.\n8_ Guardar datos\n0_Salir.\n"))
        NuevoMenu.Opciones(Op,Lista)
