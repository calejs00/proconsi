#función para contar palabras repetidas
def repe(a):
    palabras = a.split() #divido el texto en las distintas palabras (separadas por espacios en blanco)
    contador = {} #creo un diccionario para almacenar cada palabra, y las veces que aparece
    palabrasRepe = [] #lista donde añadiré las palabnras que aparecen más de una vez
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    for palabra in contador:
        if contador[palabra] > 1:
            palabrasRepe.append(palabra)
    return palabrasRepe

def main():
    #string original
    text = 'Proconsi es una empresa de Tecnologías de la Información y la Comunicación especializada\nen el desarrollo e integración de soluciones informáticas para todo tipo de empresas. Más de tres décadas\nde experiencia avalan a una compañía tan flexible como responsable. Cuenta con un equipo multidisciplinar\nde más de 120 profesionales cualificados, expertos y comprometidos con un único objetivo: hallar la\nsolución tecnológica exacta para cada cliente. Proconsi es especialista en la creación y el desarrollo de\nsoftware de gestión, consultoría tecnológica, dirección y gestión de proyectos I+D+i basados en TIC,\nsoporte técnico, aplicaciones móviles y fomento de tendencias en nuevas tecnologías, como el cloud computing.\n'
    print("El texto tiene",len(text),"caracteres\n") #caracteres del texto entero
    print(text.upper()) #convertir en mayúsculas
    print(text.lower()) #convertir en minúsculas
    palabrasRepe = repe(text)
    print("Hay", len(repe(text)), "palabras que se repiten")
    print("Se repiten:")
    for i in palabrasRepe:
        print(i)
    print('\n')
    text2 = text.replace("Proconsi", "Isnocorp") #reemplazo una palabra por otra
    text2 = text.replace("proconsi", "Isnocorp") #reemplazo una palabra por otra

    print(text2)
    import time

    start = time.time() #empiezo a cronometrar el tiempo
    text3 = text * 1000 #concateno 1000 veces
    end = time.time() #paro de cronometrar
    print("El texto ha tardado en concatenarse", end -start, "segundos y la longitud final es", len(text3), "caracteres")
    return 

if __name__ == "__main__":
    a = main()
