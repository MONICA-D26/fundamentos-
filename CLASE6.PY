"""
numero = range(1,51)
for e in numero:

    if e % 3 == 0 and e % 5 == 0: 
        print("fiz.buzz")
        
    elif e % 3 == 0:
        print("fizz")
    elif e % 5 == 0:
        print("buzz")

    

    else:
        print(e)
"""



personas =[
    {"nombre": "Ana", "edad": 10},
    {"nombre": "Luis", "edad": 16},
    {"nombre": "Carlos", "edad": 25},
    {"nombre": "María", "edad": 70},
    {"nombre": "Marta", "edad": 50},
    {"nombre": "José", "edad": 13},
    {"nombre": "Lucía", "edad": 64},
    {"nombre": "Miguel", "edad": 65}
]

for personas in personas:
    nombre = personas["nombre"]
    edad = personas["edad"]


    if edad < 13:
        print(f"niño")
    elif edad >= 13 and edad <= 17:
        print(f"adolecente")
    elif edad >= 18 and edad <= 64:
        print(f"adulto")
    else:
        print(f"anciano",{edad>64})



  