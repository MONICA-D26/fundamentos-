"""# clasess

class Persona:
    def __init__(self, nombre, edad): #metodo clase inicializador 
        self.nombre = nombre
        self.edad =edad

    def saludar(self): #metodo de la clase 
        print(f"hola mi nombre es {self.nombre} y tengo {self.edad} años")    




#creo mi instancia 

persona1 =Persona("Juan", 40)
persona2 =Persona("Carla",18)

# llamar metodo
persona1.saludar()
persona2.saludar()"""

"""
class Calculadora:
    def suma(self, num1, num2):
        return num1 + num2

    def resta(self, num1, num2):
        return num1 - num2
    
    def multiplicacion(self, num1, num2):
        return num1 * num2
    
    def division(self, num1, num2):
        if num2 ==0:
             return "no se puede dividir en cero"
        else:
             return num1 / num2
    

numero1= int(input("ingrese un numero "))
numero2= int(input("ingrese un numero "))

calculadora =Calculadora()

print(calculadora.suma(numero1,numero2))

print(calculadora.resta(numero1,numero2))

print(calculadora.multiplicacion(numero1,numero2))

print(calculadora.division(numero1,numero2))

"""



class Calculadora2:
     def __init__(self, numero,): 
        self.resultado = numero

def suma(self, numero):
        
        self.resultado = self.resultado + numero 

        self.resultado = self.resultado - numero 

        self.resultado = self.resultado * numero 

        self.resultado = self.resultado / numero 



calculo = Calculadora2 (0)




