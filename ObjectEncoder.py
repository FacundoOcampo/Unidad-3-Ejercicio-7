import json
from pathlib import Path

class ObjetEncoder():
    def LeerJSONArchivo(self,Archivo):
        with Path(Archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
        return diccionario
    def DecodificarDiccionario(self,d):
        manejador=None
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='Lista':
                personal=d['Personal']
                dpersonal=personal[0]
                manejador=class_()
                for i in range(len(personal)):
                    dpersonal=personal[i]
                    class_name=dpersonal.pop('__class__')
                    class_=eval(class_name)
                    atributos=dpersonal['__atributos__']
                    unapersona=class_(**atributos)
                    manejador.AgregarElemento(unapersona)
        return manejador
    def ConvertirTextoADiccionario(self,Texto):
        return json.loads(Texto)
    def GuardarJSONArchivo(self,diccionario,archivo):
        with Path(archivo).open("w",encoding="UTF-8")as destino:
            json.dump(diccionario,destino,indent=4)
            destino.close()
