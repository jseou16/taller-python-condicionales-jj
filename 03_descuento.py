#Calculadora de descuento segun el tipo de cliente

descuento = 0 

subt = float(input("Ingrese el subtotal de su compra: "))
while subt < 0: 
    subt = float(input("Error, no se pueden ingresar numeros negativos\nEscriba un subtotal valido:"))

tipos = ["vip", "regular"]
tipo = str(input("Ingrese su tipo de membresia (vip o regular): ").strip().lower())
while tipo not in tipos:
    tipo = str(input("Error, escoja un tipo de membresia valido: ").strip().lower())

if tipo == "vip": 
    descuento = subt*0.15
else: 
    if subt >= 100:
        descuento = subt*0.05
    else:
        descuento = 0

total = subt-descuento       

print(f"El total de su compra fue {total:.2f}$, con el subtotal de {subt:.2f}$, y el descuento de {descuento:.2f}$ aplicado por su tipo de membresia {tipo}")