"""i = 1

while i <= 10:
    print(i)
    i = i + 1

numero = int(input("ingrese un numer ( y cero 0 para terminar ):"))
suma = 0

while numero != 0:
   
    suma = suma + numero
    numero = int(input("ingrese un numero( y cero 0 para terminar ):"))

print("la suma es", suma)

numero = int(input("ingrese un numero( y un numero impar para terminar)"))

suma= 0 

while numero % 2==0:
   
   suma = suma + numero

   numero = int(input("ingrese un numer ( y un numero impar para terminar)"))
    
print("la suma es", suma)"""






# FUNCIONES 

def saludo():
    print("hola")

saludo()

def operaciones():
    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. division")
    print("5. resto")
    print("6. salir")
          
operaciones()


def suma (n1, n2):
  return n1+n2

def resta(n1, n2):
  return n1 - n2

def multiplicacion(n3):
   return n3 * 10

def division(n1, n2):
   return n1/n2

def resto (n1, n2 ):
   return n1% n2

operracion= int(input("ingrese un numero segun la operacion "))
numero= int(input("ingrese un numero 2 "))
numero= int(input("ingrese un numero 1 "))

if operacion == 1:
   print("suma")


