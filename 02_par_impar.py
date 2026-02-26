#Separador de numeros en par y impar, y checker de mayoria de edad!

num = int(input("Escoja un numero: "))
if num%2==0: 
    print(f"Su numero {num} es par.")
else: 
    print(f"Su numero {num} es impar.")

edad = int(input("Escriba su edad: "))
while edad < 0:
    edad = int(input("No hay edades negativas. Escriba su edad: "))
if edad >= 18: 
    print(f"Hola, tienes {edad} años asi que eres mayor de edad")
else: 
    print(f"Hola, tienes {edad} años asi que eres menor de edad")
