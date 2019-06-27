class Trabajador:
    def __init__(self,nombre,apellidos,edad):
        self.nombre = input ("dime tu nombre ")
        self.apellidos = input ("dime tus apellidos ")
        self.edad = input ("dime tu edad ")
ficha = ()    
    
    def fichaArchivo (self):
        ficha=(self.nombre,self.apellidos,str(self.edad))

        return ficha



datos = Trabajador("","","")

print (ficha)