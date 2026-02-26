#Simulador de tarifa de taxi con diferentes condiciones!

dist = int(input("Que tan largo fue su viaje (en km): "))
while dist < 0: 
    dist = int(input("Error. No hay distancias negativas\nEscriba una distancia valida: "))

hora = int(input("A que hora viajo? (solo hora, no minutos, formato 24hrs): "))
while hora not in range(0,23):
    hora = int(input("Escriba una hora valida de 00 a 23 hrs: "))
horario = "."
tarifaBase = 1 
costokm = 0
if hora >= 6 and hora <= 19:
    costokm = costokm + 0.5
    horario = "diurno"
else: 
    costokm = costokm + 0.65
    horario = "nocturno"
adicional = 0

if dist >= 10:
    adicional = adicional + 2

total = tarifaBase + (dist*costokm) + adicional

print(f"Horario: {horario}\nDistancia: {dist}km\nDebe en total: {total:.2f}$.")