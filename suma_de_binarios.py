#Para sumar 2 numeros binarios, primero necesitamos que la cadena de numeros binarios sean 1 y 0, para eso vamos a utilizar la estructura condicional IF.
# Si bien no hace falta que ambos numeros binarios tengan la misma longitud, vamos a utilizar el .zfill para rellenar con ceros a la izquierda y asi nos aseguramos de que los bits esten alineados. 
# Luego, sumamos los bits de derecha a izquierda, teniendo en cuenta el acarreo (carry) que se produce cuando la suma de dos bits es mayor o igual a 2.
# Finalmente, si al final de la suma hay un acarreo, lo agregamos al resultado.

def suma_binaria(num1, num2):
    max_leng = max(len(num1), len(num2)) #Utilizamos el max para obtener la longitud del numero mas largo   
    num1 = num1.zfill(max_leng)  #Utilizamos el metodo .zfill para rellenar la cadena con ceros a la izquierda, para que ambos numeros tengan la misma longitud 
    num2 = num2.zfill(max_leng)

    resultado = "" #La variable resultado va a almacenar el resultado de la suma
    carry = 0
    
    #Utilizamos un for para recorrer los numeros de derecha a izquierda
    for i in range(max_leng -1, -1, -1 ):
        bit1 = int(num1[i])
        bit2 = int(num2[i])

        suma = bit1 + bit2 + carry #Sumamos los dos bits y el acarreo (carry) de la iteracion anterior
        carry = suma // 2 #Utilizando la division entera nos va a decir si hay que llevar 1 bit de carry en la prixima iteracion
        resultado2 = suma % 2 #Utilizamos el modulo para obtener el resultado de la suma en binario (0 o 1)

        resultado = str(resultado2) + resultado #Aqui convertimos el resultado2 en cadena, para agregarlo al resultado principal

    #Utilizamos un if para agregar si es que hay, el carry (acarreo) al final     
    if carry:
        resultado = "1" + resultado
    return resultado

#El usuario ingresa los dos numeros binarios a sumar
bin1 = input("Ingrese el primer numero binario: ")
bin2 = input("Ingrese el segundo numero binario: ")

#Validamos que los numeros ingresador solo tengan 0 y 1, de lo contrario va a pedir que ingrese los numeros correctos
if not all(bit in '01' for bit in bin1) or not all(bit in '01' for bit in bin2):
    print("Por favor, ingrese solo números binarios (0 y 1).")
else:
    resultado = suma_binaria(bin1, bin2)
    print(f"La suma de {bin1} y {bin2} es: {resultado}")


#Por Ejemplo:
#Para sumar ----->  11100101
#                 +    10101
#                 ------------
#                   11111010