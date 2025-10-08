#Primero defino las funciones de lo que se me pide hacer, todas redondeando a los numeros decimales requeridos
#función suma
def sum(n1,n2, dec):
    return round(n1+n2, dec)

#función resta
def rest(n1,n2, dec):
    return round(n1-n2, dec)

#función división
def div(n1,n2, dec):
    return round(n1/n2, dec)

#función multiplicación
def mult(n1,n2, dec):
    return round(n1*n2, dec)

#función módulo
def mod(n1,n2, dec):
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
    num1 = float(input("Introduce la primera cantidad: "))
    num2 = float(input("Introduce la segunda cantidad: "))
    numDecimales = int(input("Di cuántos decimales quieres redondear:"))

    #printeo y ejecuto todo lo que se pide
    print("La suma de",num1, "y", num2, "es", sum(num1, num2, numDecimales))
    print("La resta de",num1, "y", num2, "es", rest(num1, num2, numDecimales))
    print("La división de",num1, "y", num2, "es", div(num1, num2, numDecimales))
    print("La multiplicación de",num1, "y", num2, "es", mult(num1, num2, numDecimales))
    print("El módulo de",num1, "y", num2, "es", mod(num1, num2, numDecimales))
    mayor(num1, num2)
    return

if __name__ == "__main__":
    a = main()