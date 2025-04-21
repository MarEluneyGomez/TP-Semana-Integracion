def suma_binaria(num1, num2):
    max_leng = max(len(num1), len(num2))
    num1 = num1.zfill(max_leng) #Utilizamos el .zfill para rellenar la cadena con ceros
    num2 = num2.zfill(max_leng)

    resultado = ""
    carry = 0
    
    #Utilizamos un for para recorrer los numeros de derecha a izquierda
    for i in range(max_leng -1, -1, -1 ):
        bit1 = int(num1[i])
        bit2 = int(num2[i])

        suma = bit1 + bit2 + carry
        resultado2 = suma % 2 #Esta suma me da el bit 0 o 1 
        carry = suma // 2 #Utilizando la division entera nos va a decir si hay que llevar 1 bit de carry en la prixima iteracion

        resultado = str(resultado2) + resultado #Aqui convertimos el resultado2 en cadena, para agregarlo al resultado principal

    #Utilizamos un if para agregar si es que hay, el carry (acarreo) al final 
    if carry:
        resultado = "1" + resultado
    return resultado

bin1 = input("Ingrese el primer numero binario: ")
bin2 = input("Ingrese el segundo numero binario: ")

#Validamos que los numeros ingresador solo tengan 0 y 1, de lo contrario va a pedir que ingrese los numeros correctos
if not all(bit in '01' for bit in bin1) or not all(bit in '01' for bit in bin2):
    print("Por favor, ingrese solo números binarios (0 y 1).")
else:
    resultado = suma_binaria(bin1, bin2)
    print(f"La suma de {bin1} y {bin2} es: {resultado}")