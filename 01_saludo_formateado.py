nombre = str(input("Escriba su nombre: "))
edad = int(input("Escriba su edad: "))
while edad < 0: 
    edad = int(input("No hay edades negativas. Escriba edad valida: "))
ciudad =  str(input("Escriba su ciudad de residencia: "))

print(f"Hola {nombre}, tienes {edad} anos, y vives en {ciudad}")
