# Primero generamos un número decimal aleatorio, en el rango de 10 a 1000.
# Elijo este rango porque con un número menor a 10 sería fácil de adivinar su conversión a binario,
# un número mayor a 1000 ya nos da un binario muy largo.

import random
decimal = random.randint(10, 1000)

# Para convertir el número decimal a binario usamos el método de divisiones sucesivas:
# Dividimos el número decimal entre 2, guardamos el residuo (0 o 1), y repetimos la operación con el
# cociente obtenido hasta que este sea 0.
# Luego leemos la secuencia de residuos comenzando por el último hasta el primero (en orden inverso)
# y nos da el número binario.
# No sabemos cuántas veces se debe repetir la operacón, por eso elijo un bucle "while" con la condición
# de que el cociente no sea 0.
# En cada iteración del bucle guardamos el residuo de la division en una cadena que irá construyendo
# nuestro resultado binario, también aprovechamos para generar otra cadena con los resultados paso a 
# paso para poder ver el proceso y para tener un contador que nos dará la cantidad de bits del resultado.

def decimal_a_binario(decimal):
    binario = ""
    paso_a_paso = ""
    bits = 0
    while decimal > 0:
        paso_a_paso += f"{decimal} dividido 2 = {decimal // 2}, residuo {decimal % 2}\n"
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
        bits += 1
    return binario, paso_a_paso, bits

resultado, pasos, bits = decimal_a_binario(decimal)
print(f"Convertimos {decimal} a binario:\n{pasos}Leemos los residuos de abajo hacia arriba.\nObtenemos un número de {bits} bits.\nEl resultado es {resultado}")