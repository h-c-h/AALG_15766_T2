import random
import math

def pedir_entero_positivo(prompt):
    while True:
        valor = int(input(prompt))
        if valor <= 0:
             print("El valor debe ser mayor que cero. Intente de nuevo.")
        else:
             return valor
        

def generar_coordenadas(n):
    matriz = []
    for _ in range(n):
        x = random.randint(-81, 81)
        y = random.randint(-81, 81)
        matriz.append([x, y])
    return matriz

def distancia_desde_origen(coord):
    x, y = coord
    return math.sqrt(x**2 + y**2)

def coordenada_mas_alejada(matriz):
    def divide_y_venceras(lista):
        if len(lista) == 0:
            return None
        if len(lista) == 1:
            x, y = lista[0]
            if x > 0 and y < 0:
                return lista[0]
            else:
                return None

        mitad = len(lista) // 2
        izquierda = divide_y_venceras(lista[:mitad])
        derecha = divide_y_venceras(lista[mitad:])

        if izquierda and derecha:
            return izquierda if distancia_desde_origen(izquierda) > distancia_desde_origen(derecha) else derecha
        elif izquierda:
            return izquierda
        else:
            return derecha

    return divide_y_venceras(matriz)

print("Problema 1")
n = pedir_entero_positivo("Ingrese la cantidad de pares de coordenadas: ")
coordenadas = generar_coordenadas(n)

print("\nLista de coordenadas generadas:")
print(coordenadas)

resultado = coordenada_mas_alejada(coordenadas)

print("\nResultado:")
if resultado:
    print(f"La coordenada más alejada con X > 0 e Y < 0 es: {resultado}")
    print(f"Distancia desde el origen: {distancia_desde_origen(resultado):.2f}")
else:
    print("No se encontró ninguna coordenada con X > 0 e Y < 0.")