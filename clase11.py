"""

class Persona:
    def __init__(self, nombre, edad): 
        self.nombre = nombre
        self.edad =edad

    def saludar(self): 
        print(f"hola mi nombre es {self.nombre} y tengo {self.edad} años")    



persona1 =Persona("Juan", 40)
persona2 =Persona("Carla",18)
persona3 =Persona("marina",52)

persona1.saludar()
persona2.saludar()
persona3.saludar()
"""
"""

class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año 


    def libro (self):
        print(f"el libro con tituli{self.titulo} escrito por {self.autor} en el año{self.año}")


libro1 = Libro("cien años de soledad", "Garcia Marquex", 1967)
libro1.libro()

"""



"""class Carro :
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def descripcion (self):
        print(f"el carro {self.toyota} ")"""


class Estudiante :
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

    def comparacion (self):
        calificacion = self.nota >= 3.5
        if calificacion == True:
            return f"el estudiante paso con una nota de {self.nota}" 
        else:
            return "perdio"
         

    def informacion (self):
        print (f" es estudiante {self.nombre} de edad {self.edad} tiene una nota de {self.nota}")


estudiante1 = Estudiante (" francisco", 19 , 3.4)

print(estudiante1.comparacion())
estudiante1.informacion()