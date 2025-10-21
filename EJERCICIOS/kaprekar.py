# 45: 45² = 2025; 20 + 25 = 45.
# 297: 297² = 88209; 88 + 209 = 297.
# 703: 703² = 494209; 494 + 209 = 703
#Viene a ser un número que elevándolo al cuadrado, lo puedes separar en dos partes,
#(siendo la segunda parte un número con los mismos digitos que el número original),
#y la suma de esas dos partes sea igual al número original
#CASOS QUE HE TENIDO EN CUENTA
#-Que el usuario meta un número no negativo para la cantidad de figuras
#-Que el usuario meta un valor no numérico

def Kaprika(n):
    n2=n**2 #calculo el cuadrado
    k = 1
    cont = 0
    if n == 1:
        return True, cont #caso de n = 1
    elif len(str(n2))==2: #caso para números menor que 10
        cont += 1
        if (int((str(n2)[0:1]))+int((str(n2)[1:]))) == n:
            return True, cont   
    for i in range(0, len(str(n2))-2):#caso estándar
        cont += 1
        while k != len(str(n2)): 
            if (int((str(n2)[0:i+k]))+int((str(n2)[i+k:]))) == n:
                cont += 1
                if(len((str(n2)[i+k:])) == len(str(n))):
                    return True, cont
            k+=1
    return False, cont

def main():
    while True:
        try:
            num = int(input("Introduce un número para ver si es Kaprekar o no: "))
            if num < 0:
                print("Por favor, introduce un número no negativo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero no negativo.")
    result, cont = Kaprika(num)
    if result==True:
        print("El número", num, "es válido Kaprekar!")
    else:
        print("El número", num, "NO es válido Kaprekar")
    print("Se han realizado", cont, "operaciones.")
    return

if __name__ == "__main__":
    a = main()