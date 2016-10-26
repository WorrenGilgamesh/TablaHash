__author__ = 'dai'
import json
import string
import random as rnd
def palabrasazar(tam):
    return
class tablaHash:
    def __init__(self):
        self.tabla=[]
        self.cont=0
    def fnHash(self,dato):
        try:
            return dato[0]
        except Exception:
            raise Exception('mal dato');
    def inserta(self, dato):
        llave=self.fnHash(dato)
        if llave in self.tabla.keys():
            self.tabla[llave] +=[dato]
        else:
            self.tabla[llave]=[dato]
        self.cont+=1
    def toString(self):
        print self.table
        #return json.dump(self.tabla)
    def borrar(self, dato):
        llave=self.fnHash(dato)
        #if llave in self.tabla.key():
         #   for 1 in self.tabla[llave]:
          #      if i==dato:
           #         self.tabla[llave].remove(dato)
            #        break
        try:
            self.tabla[llave].remove(dato)
        except Exception:
            print 'no estaba'
    def colisiones(self):
        cuenta=0
        for i in self.tabla.key():
            if  len(self.tabla[i])>0:
                cuenta+=len(self.tabla[i])-1
        return cuenta
def main():
    tabla=tablaHash()
    tabla.inserta((1,'Fernando0'))
    #tabla.inserta((2,'Emiliano', 'elDeAlado'))
    #tabla.inserta((3,'Victor', 'yo'))
    for i in range(10):
      tabla.inserta((rnd.randint(0,100),palabrasazar(10)))
    tabla.toString()
    print tabla.colisiones()

if __name__ == "__main__":
    main()