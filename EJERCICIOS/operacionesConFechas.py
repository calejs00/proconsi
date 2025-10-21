#CASOS DE ENTRADA QUE HE TENIDO EN CUENTA
#-Que el usuario meta una fecha en un formato incorrecto
#-Que el usuario meta una fecha inválida (ej: 2023/13/09)
#-Que el usuario meta la misma fecha dos veces
#-Que el usuario meta cadenas vacías o de texto
#-Fechas en años bisiestos
import calendar
import datetime as dt

#función para calcular el inicio y fin de un año
def inicioYfin(fecha):
    inicio = dt.date(fecha.year,1,1)
    fin = dt.date(fecha.year,12,31)
    return inicio, fin

#función para calcular los días de un año
def numDias(año):
    if calendar.isleap(año):
        return 366
    else:
        return 365
    
def validar_fecha(fecha_str):
    try:
        fecha = dt.datetime.strptime(fecha_str, "%Y/%m/%d")
        return fecha.date() 
    except ValueError:
        return None

def main():
    #pido las fechas
    while True:
        fecha1_str = input("Dame una fecha en formato yyyy/mm/dd: ")
        fecha1 = validar_fecha(fecha1_str)
        if fecha1 is None:
            print("Fecha inválida o formato incorrecto. Inténtalo de nuevo.")
        else:
            break
    while True:
        fecha2_str = input("Dame otra fecha: ")
        fecha2 = validar_fecha(fecha2_str)
        if fecha2 is None:
            print("Fecha inválida o formato incorrecto. Inténtalo de nuevo.")
        else:
            break

    # #convierto las fechas a formato date, para poder trabajar mejor con ellas
    # año, mes, dia = map(int, fecha1.split("/"))
    # fecha1 = date(año, mes, dia)
    # año, mes, dia = map(int, fecha2.split("/"))
    # fecha2 = date(año, mes, dia)

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

