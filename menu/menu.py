from ejercicios.ejercicio1_cine import calcular_importe_total
from ejercicios.ejercicio2_combustible import calcular_rendimiento, calcular_costo

def menu():
    while True:
        print("Seleccione una opción:")
        print("1. Calcular importe de boletos de cine")
        print("2. Calcular rendimiento y costo de combustible")
        print("3. Salir")
        
        opcion = input("Ingrese el número de la opción deseada: ")
        
        if opcion == "1":
            cantidad = int(input("Ingrese la cantidad de boletos a comprar: "))
            importe_total = calcular_importe_total(cantidad)
            print(f"El importe total a pagar es: ${importe_total:.2f}")
        
        elif opcion == "2":
            distancia = float(input("Ingrese la distancia recorrida en kilómetros: "))
            litros = float(input("Ingrese la cantidad de litros consumidos: "))
            rendimiento = calcular_rendimiento(distancia, litros)
            costo = calcular_costo(litros)
            print(f"Rendimiento: {rendimiento:.1f} km/l")
            print(f"Costo: ${costo:.2f}")
        
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Por favor, intente nuevamente.")