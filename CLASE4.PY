"""variable =int(input("ingrese un numero"))

if numero >0:
    print(f"{numero} es un numero entero")

else:
    print(f"{numero}es un numero negativo")"""

"""numero=
variable= int(input("ingrese un numero"))
if numero ==0:
    print(f"si {numero}es o")"""


while True:
    
    print("calcuradora geometrica de areas")
    print("1. circulo")
    print("2.cuadrado")
    print("3.rectangulo")
    print("4.triangulo")
    print("5.salir")

    opcion= int(input("ingrese una opcion"))

    if opcion == 1: 
        radio=float (input("ingrese el radio del circulo"))
        area= 3.1416 * radio * radio
        print(f"el area del circulo es {area:.2f}")

    elif opcion == 2:
        lado = float(input("ingrese el lado"))
        area = lado*lado
        print(f"El area del cuadrado es {area}")

    elif opcion ==3:

        largo= float(input("ingrese el largo"))
        ancho= float(input("ingrse el ancho"))
        area = largo*ancho
        print(f"el area del rectangulo es {area}")

    elif opcion ==4:

        base= float(input("ingrese el base"))
        altura= float(input("ingrse el altura"))
        area = base*altura
        print(f"el area del triangulo es {area}")

