#Simulador de calificaciones con inputs!

nota1 = int(input("Escriba la primera calificacion (0-100): "))
if nota1 <0 or nota1 > 100:
    print("Error, nota no valida")
    exit()
nota2 = int(input("Escriba la segunda calificacion (0-100): "))
if nota2 <0 or nota2 > 100:
    print("Error, nota no valida")
    exit()
nota3 = int(input("Escriba la tercera calificacion (0-100): "))
if nota3 <0 or nota3 > 100:
    print("Error, nota no valida")
    exit()

promedio = float((nota1+nota2+nota3)/3)
estado = 0 
if promedio >= 90:
    estado = "Excelente"
elif promedio >= 80:
    estado = "Muy bueno"
elif promedio >= 70:
    estado = "Bueno"
elif promedio >= 60:
    estado = "Supletorio"
else:
    estado = "Reprobado"

print(f"Notas ingresadas: {nota1}, {nota2}, {nota3}\nPromedio: {promedio:.2f}\nClasificacion: {estado}")