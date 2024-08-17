
"""lista = [25, 26, 27, 28, 29]

numero = int(input("ingrese numero"))

if numero in lista:
    elemento = lista.index(numero)
    lista[elemento] = 6 

print(lista)"""

"""lista = [25, 26, 27, 28, 29]

numero = int(input("ingrese numero"))



for i in range(len(lista)):
    if numero == lista [i]:
       del lista[i] 
       break

print(lista)"""


 # manera de sumar elementos de nuestra lista 
"""  
""lista = [25, 26, 27, 28, 29]
print(sum(lista))"""""

"""# tuplas
frutas = ( "manzana", "pera", "chontaduro", "kiwi")
print(frutas[1])
print(frutas[-2])

lista_frutas = list(frutas)
print(frutas)
print(lista_frutas)
print(tuple(lista_frutas))
"""
 # DICCIONARIO
contacto = {"Diego": "12345678",
            "tomas": "15567898",
            "juan":  "134567876"}
print(contacto["juan"])

contacto[ " ana "] = "132435465"
print(contacto)

del contacto ["Diego"]
print(contacto)


for nombre, telefono in contacto.items():
    print(nombre, telefono)