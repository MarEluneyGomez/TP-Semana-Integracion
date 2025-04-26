import random

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

def generar_binario ():

    binario = ''

    #genera una longitud random entre 4 y 10
    longitud = random.randint(3,10)

    for i in range(longitud):

        #asigna un '1' o un '0' aleatoriamente en cada iteracion
        bit = random.choice(['0','1'])

        #concatena cada digito asignado en cada iteracion
        binario += bit

    return binario


def binario_a_decimal (binario):
    # Logica para el codigo:
    '''Como la potencia inicial SIEMPRE es cero, sabemos que la longitud de un binario menos 1 nos da la potencia más alta a asignar
        #Por ejemplo: Binario '1010', Longitud:'4', Potencia_Maxima= 4-1'''

    ''' Tambien sabemos que si empezamos a 'asignar' potencias a cada digito de un binario, si comenzamos por la izquierda, la mayor potencia a asignar, le corresponde al primer digito y...
        las potencias de los otros digitos estan dadas por la potencia anterior menos 1
            Por ejemplo: Binario:'1010', Potencia_Maxima:'3'
            Primer_digito:'1', primera_potencia:'3','segundo_digito:'0', segunda_potencia:'3-1', tercer_digito '1', tercer_potencia:'2-1', cuarto_digito '0', cuarta_potencia:'1-1' '''

    '''Por ultimo sabemos que la potencia se asigna a el 2 que multiplica el digito y que estos digitos multiplicados por 2 a la potencia 'X', sumados dan el decimal deseado
        esto nos queda: 
        1.(2^3) + 0.(2^2) + 1.(2^1) + 0.(2^0) = 8 + 0 + 2 + 0 = 10 '''
    
    #Sabiendo esto:
    decimal = 0
    respuesta=''
    for i in range(len(binario)):

        bit = int(binario[i])

        potencia = len(binario) - i - 1

        decimal += bit * (2 ** potencia)

        if respuesta:
                respuesta += ' + '

        respuesta +=f'{bit} x 2^{potencia}'
    
    respuesta+= f' = {decimal}'
        

    return decimal, respuesta

def suma_binaria(num1, num2):
    max_leng = max(len(num1), len(num2))
    num1 = num1.zfill(max_leng)
    num2 = num2.zfill(max_leng)

    resultado = ""
    pasos = []
    carry = 0

    for i in range(max_leng - 1, -1, -1):
        bit1 = int(num1[i])
        bit2 = int(num2[i])

        suma = bit1 + bit2 + carry
        resultado_bit = suma % 2
        carry = suma // 2

        paso = f"Suma de bits {bit1} + {bit2} + {carry} (acarreo anterior) = {suma}, el bit resultante es {resultado_bit} y el nuevo acarreo es {carry}."
        pasos.append(paso)
        resultado = str(resultado_bit) + resultado

    if carry:
        resultado = "1" + resultado
        pasos.append(f"Se agrega el acarreo final: 1.")

    return resultado, pasos

def main():
    puntuacion = 0
    #--------------------------------
    binario_b_d = generar_binario()
    decimal_b_d, respuesta_b_d = binario_a_decimal(binario_b_d)
    print(f'Calcule el equivalente en decimal del binario {binario_b_d}')
    decimal_usuario = input('Ingrese su resultado:')

    if int(decimal_usuario) == decimal_b_d:
        print('Correcto!')
        puntuacion += 1
    else:
        print('Incorrecto, la respuesta correcta es:')
        print(respuesta_b_d)
    # -------------------------------

    decimal = random.randint(10, 1000)
    resultado_d_b, pasos_d_b, bits_d_b = decimal_a_binario(decimal)
    print(f'calcule el equivalente en binario del decimal {decimal}')
    binario_usuario = input('Ingrese su resultado:')

    if binario_usuario == resultado_d_b:
        print('Correcto!')
        puntuacion += 1
    else:
        print('Incorrecto, la respuesta correcta es:')
        print(f"Convertimos {decimal} a binario:\n{pasos_d_b}Leemos los residuos de abajo hacia arriba.\nObtenemos un número de {bits_d_b} bits.\nEl resultado es {resultado_d_b}")
    # -------------------------------

    bin1_sum = generar_binario()
    bin2_sum = generar_binario()

    resultado_suma, pasos_suma = suma_binaria(bin1_sum,bin2_sum)

    print(f'Calcule la suma de los binarios {bin1_sum} y {bin2_sum}')
    suma_usuario = input('ingrese su resultado')

    if resultado_suma == int(suma_usuario):
        print('Correcto!')
        puntuacion += 1
    else:
        print('Incorrecto, la respuesta correcta es:')
        print(pasos_suma)
        print(resultado_suma)

    print(f'Tu puntuacion final es {puntuacion}')
    if puntuacion <= 1:
        print('Te recomiendo repasar los ejercicios.')
    if 1 < puntuacion <= 2:
        print('¡Muy bien! Repasa los errores para mejorar aún más.')
    elif puntuacion == 3:
        print('Excelente, haz logrado una puntuacion perfecta!')
    


if __name__ == "__main__":
    main()
