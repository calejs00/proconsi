#CASOS DE ENTRADA QUE HE TENIDO EN CUENTA
#-Que el usuario meta un valor no numérico o un valor nulo
#-Que el usuario meta un número negativo o decimal de decimales
#-Que el usuario meta un 0 en la división o módulo


#Primero defino las funciones de lo que se me pide hacer, todas redondeando a los numeros decimales requeridos
#función suma
def sum(n1,n2, dec):
    return round(n1+n2, dec)

#función resta
def rest(n1,n2, dec):
    return round(n1-n2, dec)

#función división
def div(n1,n2, dec):
    if n2 == 0:
        return "Error: División por cero"
    return round(n1/n2, dec)

#función multiplicación
def mult(n1,n2, dec):
    return round(n1*n2, dec)

#función módulo
def mod(n1,n2, dec):
    if n2 == 0:
        return "Error: Módulo por cero"
    return round(n1%n2, dec)

#función para saber si el primer numero es mayor, igual o menor
def mayor(n1,n2):
    if n1==n2:
        print("Los números son iguales")
    elif n1>n2:
        print("El primer número es mayor al segundo")
    else:
        print("El primer número es menor al segundo")

def main():
    #pido los numeros por pantalla
    while True:
        num1 = input("Introduce la primera cantidad: ")
        if isinstance(num1, str):
            try:
                num1 = float(num1)
            except ValueError:
                print("Por favor, introduce un número válido. Volvamos a empezar")
                continue

        num2 = input("Introduce la segunda cantidad: ")
        if isinstance(num2, str):
            try:
                num2 = float(num2)
            except ValueError:
                print("Por favor, introduce un número válido. Volvamos a empezar")
                continue

        numDecimales = input("Di cuántos decimales quieres redondear: ")
        if isinstance(numDecimales, str):
            try:
                numDecimales = int(numDecimales)
            except ValueError:
                print("Por favor, introduce un número válido para los decimales. Volvamos a empezar")
                continue 

        if numDecimales < 0:
            print("El número de decimales debe ser un entero no negativo. Volvamos a empezar")
        else:
            break


    #printeo y ejecuto todo lo que se pide
    print("La suma de",num1, "y", num2, "es", format(sum(num1, num2, numDecimales),f".{numDecimales}f"))
    print("La resta de",num1, "y", num2, "es", format(rest(num1, num2, numDecimales),f".{numDecimales}f"))
    print("La división de",num1, "y", num2, "es", format(div(num1, num2, numDecimales),f".{numDecimales}f"))
    print("La multiplicación de",num1, "y", num2, "es", format(mult(num1, num2, numDecimales),f".{numDecimales}f"))
    print("El módulo de",num1, "y", num2, "es", format(mod(num1, num2, numDecimales),f".{numDecimales}f"))
    mayor(num1, num2)
    return

if __name__ == "__main__":
    a = main()