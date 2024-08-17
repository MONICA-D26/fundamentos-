

"""numeroDado = 7

if numeroDado % 2 == 0:
    print("el numero es par")

else:
    print ("el numero es impar")

    numero = 16 
    if numero % 2 == 0:
        print("el numero es par")
    else:
        print (" el numero es impar")




    nombre = input("escriba su nombre:")
    print(nombre)"""
    


peso = float(input("ingrese su peso en kg"))
altura = float(input("ingrese su altura:"))

imc = peso / (altura*altura)

if  imc < 18.5:
    print("bajo peso")


elif imc >= 18.5 and imc <= 24.9:
    print("peso normal")

elif imc <=25 and imc >= 29.9:
    print("sobrepeso")

else:  
    print("obesidad")


print(f"su imc es :{imc.4f}")
print(f"su clasificacion es:{clasificacion}")

