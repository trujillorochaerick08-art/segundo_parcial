'''
Un cine necesita desarrollar un programa que permita determinar el importe de una compra de boletos. 
Cada boleto cuesta $75.00. El usuario deberá indicar cuántos boletos desea comprar. Cuando se adquieran 4 
boletos o más, se aplicará un descuento del 10% sobre el subtotal. Para compras menores a 4 boletos, no se 
aplicará descuento.
'''
#PROBLEMA: Determinar el importe total de la compra de boletos en un cine, considerando descuentos por cantidad.
#ENTRADAS: Cantidad de boletos a comprar (número entero).
#SALIDAS: Importe total a pagar (número decimal).
#REGLAS Y SUPUESTOS: Cada boleto cuesta $75.00. Descuento del 10% para compras de 4 boletos o más. para compras menores a 4 boletos, no se aplica descuento.
#ALGORITMO:
#1. Leer la cantidad de boletos a comprar.
#2. Calcular el subtotal multiplicando la cantidad de boletos por el precio unitario.
#3. Si la cantidad de boletos es 4 o más, aplicar un descuento del 10% al subtotal.
#4. Mostrar el importe total a pagar.
#CASOS DE PRUEBA:
#1. Entrada: 1 boleto, Salida: $75.00
#2. Entrada: 3 boletos, Salida: $225.00
#3. Entrada: 4 boletos, Salida: $270.00
#4. Entrada: 6 boletos, Salida: $405.00

#RESTRICCIONES PARA EL AGENTE:
#1. No se permiten compras de boletos fraccionados.
#2. El sistema debe manejar entradas no válidas (por ejemplo, texto en lugar de números).

#CONTRATO DE FUNCIONES:
#leer_cantidad_boletos() -> int
#calcular_importe_total(cantidad: int) -> float
#mostrar_importe_total(importe: float) -> None

def leer_cantidad_boletos() -> int:
    return int(input("Ingrese la cantidad de boletos a comprar: "))

def calcular_importe_total(cantidad: int) -> float:
    precio_unitario = 75.0
    subtotal = cantidad * precio_unitario
    if cantidad >= 4:
        subtotal *= 0.9  # Aplicar descuento del 10%
    return subtotal

def mostrar_importe_total(importe: float) -> None:
    print(f"El importe total a pagar es: ${importe:.2f}")