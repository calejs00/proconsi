import random
import math
#lista con colores
COLORES = ["rojo", "verde", "azul", "amarillo", "morado", "naranja", "rosa"]

#clase base figura (con color y centro)
class Figura:
    def __init__(self):
        self.color = random.choice(COLORES)
        self.centro = (random.randint(0, 100), random.randint(0, 100))

    def __str__(self):
        cad=" Color: " + str(self.color)
        cad+=" Centro: "+str(self.centro)
        return cad

#clase circulo (depende de Figura)
class Circulo(Figura):
    def __init__(self):
        super().__init__()
        self.radio = random.uniform(1.0, 10.0)

    def area(self):
        return math.pi * self.radio**2

    def __str__(self):
        cad=" Círculo -> Radio: " + str(self.radio)
        cad+=" Área: "+str(self.area())
        cad+= super().__str__()
        return cad

#clase cuadrado (depende de Figura)
class Cuadrado(Figura):
    def __init__(self):
        super().__init__()
        self.lado = random.uniform(1.0, 10.0)

    def area(self):
        return self.lado**2

    def __str__(self):
        cad=" Cuadrado -> Lado:" + str(self.lado)
        cad+=" Área: "+str(self.area())
        cad+= super().__str__()
        return cad

#clase triangulo (depende de Figura)
class Triangulo(Figura):
    def __init__(self):
        super().__init__()
        self.base = random.uniform(1.0, 10.0)
        self.altura = random.uniform(1.0, 10.0)  
        
    def area(self):
        return (self.base * self.altura) / 2

    def __str__(self):
        cad=" Triángulo -> Base: " + str(self.base)
        cad+=" Altura: "+str(self.altura)
        cad+=" Área: "+str(self.area())
        cad+= super().__str__()
        return cad

def main():
    #se piden la cantidad de figuras
    nCir = int(input("Número de círculos: "))
    nTri = int(input("Número de triángulos: "))
    nCua = int(input("Número de cuadrados: "))

    #se crean, (ya de manera ordenada)
    figuras = []
    for i in range(nCir):
        figuras.append(Circulo())
    for z in range(nCua):
        figuras.append(Cuadrado())
    for j in range(nTri):
        figuras.append(Triangulo())

    #se muestran
    print("\nTodas las figuras (orden de tipo):")
    for f in figuras:
        print(f)
    return

if __name__ == "__main__":
    main()