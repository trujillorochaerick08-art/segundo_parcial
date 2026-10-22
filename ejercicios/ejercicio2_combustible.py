'''
Un conductor necesita conocer el rendimiento de combustible de su vehículo y el costo de un recorrido. El 
usuario deberá proporcionar la distancia recorrida en kilómetros y la cantidad de litros consumidos. El 
precio por litro será de $24.00.
'''
#PROBLEMA: Determinar el rendimiento de combustible y el costo de un recorrido en vehículo.

#ENTRADAS: Distancia recorrida en kilómetros (número decimal), Cantidad de litros consumidos (número decimal).

#SALIDAS: Rendimiento de combustible (kilómetros por litro, número decimal), Costo del recorrido (número decimal).

#REGLAS Y SUPUESTOS: El precio por litro de combustible es de $24.00. El rendimiento se calcula como la distancia
# dividida por la cantidad de litros consumidos. El costo del recorrido se calcula multiplicando la cantidad de
# litros consumidos por el precio por litro.

#algoritmo:
#1. Leer la distancia recorrida en kilómetros.
#2. Leer la cantidad de litros consumidos.
#3. Calcular el rendimiento de combustible dividiendo la distancia por la cantidad de litros consumidos.
#4. Calcular el costo del recorrido multiplicando la cantidad de litros consumidos por el precio por litro.
#5. Mostrar el rendimiento de combustible y el costo del recorrido.

#CASOS DE PRUEBA:
#1. Entrada: 120 km, 10 litros, Salida: Rendimiento: 12.0 km/l, Costo: $240.00
#2. Entrada: 250 km, 20 litros, Salida: Rendimiento: 12.5 km/l, Costo: $480.00
#3. Entrada: 180 km, 15 litros, Salida: Rendimiento: 12.0 km/l, Costo: $360.00
#4. Entrada: 300 km, 25 litros, Salida: Rendimiento: 12.0 km/l, Costo: $600.00

#RESTRICCIONES PARA EL AGENTE:
#1. No se permiten valores negativos para la distancia o la cantidad de litros consumidos.

#CONTRATO DE FUNCIONES:
#leer_datos() -> (float, float)
#calcular_rendimiento(distancia: float, litros: float) -> float
#calcular_costo(litros: float) -> float
#mostrar_resultados(rendimiento: float, costo: float) -> None

def leer_datos() -> (float, float):
    distancia = float(input("Ingrese la distancia recorrida en kilómetros: "))
    litros = float(input("Ingrese la cantidad de litros consumidos: "))
    return distancia, litros

def calcular_rendimiento(distancia: float, litros: float) -> float:
    if litros == 0:
        return 0
    return distancia / litros

def calcular_costo(litros: float) -> float:
    precio_por_litro = 24.00
    return litros * precio_por_litro

def mostrar_resultados(rendimiento: float, costo: float) -> None:
    print(f"Rendimiento: {rendimiento:.1f} km/l")
    print(f"Costo: ${costo:.2f}")
