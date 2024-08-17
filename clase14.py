

"""entrada = "a b c d e "

salida = ""

for i in entrada:
    salida += * 3
print (salida)"""

"""# herencia y poliforismo

class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar (self):
        return f"{self.marca} {self.modelo} esta arrancando"
    


class Carro(Vehiculo):
    def acelerar(self):
        return f"{self.marca} {self.modelo} esta acelerando"
    
class Motocicleta(Vehiculo):
    def caballito(self):
        return f"{self.marca}{self.modelo} esta haciendo un caballito"
    
carro = Carro ("toyota", "TXL")
Motocicleta = Motocicleta ("Ducati", "1199")

# heredar datos 
print(carro.acelerar())
print(Motocicleta.caballito())


#POLIFORMISMO
print(Motocicleta.arrancar())
print(carro.arrancar())

"""


## MANEJO DE ERRORES##
numero1 = 5
numero2 = 1



try:
    #intenta ejecutar
    print(numero1 + numero2)

except:
    #se ejecuta si hay una excepcion:
    print("se ha producido un error")

print ("------------")

#flujo completo de una excepcion: 
try:
    #intenta ejecutar 
    print( numero1 + numero2)
    print("no se produce ningun error")

except:
    #se ejecuta si hay alguna excepcion
    print("se ha producido un error")

else:
    #opcional se ejecuta si no se produce ningun excepcion 
    print("no se presenta ningun error, se sigue ejecutando de manera normal")

finally:
    #opcional siempre se ejecute hayan o no hayan excepciones
    print("la ejecucion continua")
