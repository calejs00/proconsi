import calendar
from datetime import date

#función para calcular el inicio y fin de un año
def inicioYfin(fecha):
    inicio = date(fecha.year,1,1)
    fin = date(fecha.year,12,31)
    return inicio, fin

#función para calcular los días de un año
def numDias(año):
    if calendar.isleap(año):
        return 366
    else:
        return 365

def main():
    #pido las fechas
    fecha1 = str(input("Dame una fecha: "))
    fecha2 = str(input("Dame otra fecha: "))

    #convierto las fechas a formato date, para poder trabajar mejor con ellas
    año, mes, dia = map(int, fecha1.split("/"))
    fecha1 = date(año, mes, dia)
    año, mes, dia = map(int, fecha2.split("/"))
    fecha2 = date(año, mes, dia)

    print("La diferencia de días entre las dos fechas es", (fecha1-fecha2).days)
    inicio1, fin1 = inicioYfin(fecha1)
    inicio2, fin2 = inicioYfin(fecha2)
    print("EL inicio de año de la primera fecha es",inicio1, "y el fin es", fin1)
    print("EL inicio de año de la primera fecha es",inicio2, "y el fin es", fin2)
    print("El año de la primera fecha tiene",numDias(fecha1.year),"días")
    print("El año de la segunda fecha tiene",numDias(fecha2.year),"días")
    print("La primera fecha se encuentra en la semana", fecha1.isocalendar().week) #con isocalendar() podemos obtener datos como la semana en la que se encuentra una fecha
    print("La segunda fecha se encuentra en la semana", fecha2.isocalendar().week)
    return

if __name__ == "__main__":
    a = main()

