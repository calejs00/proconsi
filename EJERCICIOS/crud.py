#CASOS QUE HE TNENIDO EN CUENTA
#-Que el usuario meta o edite un datos con formato incorrecto (el dni, el tipo de cliente, la fecha...)
#-Que el usuario meta o edite datos nulos o vacíos
#-Que el usuario meta o edite un importe o cuota no numérico o negativo
#-Que se intenten añadir clientes o recibos ya existentes
#-Que se intenten consultar, editar o eliminar clientes o recibos inexistentes


import psycopg2
from datetime import datetime
import re

#establezco la conexion con la base de datos (previamente he creado la bd con el postgresSql)
conexion = psycopg2.connect(
    dbname="agenda_db",
    user="postgres",
    password="contraseña",
    host="localhost",
    port="5432"
)
cursor = conexion.cursor()

#Crear tablas con sus atributos y condiciones
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    dni VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo_cliente VARCHAR(20) NOT NULL CHECK (tipo_cliente IN ('REGISTRADO','SOCIO')),
    cuota_max DECIMAL(10,2),
    fecha_alta TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS recibos (
    numero INT PRIMARY KEY,
    dni_cliente VARCHAR(20) REFERENCES clientes(dni) ON DELETE CASCADE,
    importe DECIMAL(10,2) NOT NULL,
    fecha_emision TIMESTAMP NOT NULL
);
""")
conexion.commit()

#método para añadir cliente
def añadir_cliente():
    dni = input("DNI: ").strip().upper()
    if not re.fullmatch(r"\d{8}[A-Z]", dni):
        print("DNI con formato incorrecto")
        return
    cursor.execute("SELECT dni FROM clientes WHERE dni=%s", (dni,))
    if cursor.fetchone(): #devuelve el primer registro que encuentra en la bd
        print("Cliente con ese DNI ya existe.")
        return
    #para introducir los atributos
    nombre = input("Nombre y apellidos: ").strip()
    if not nombre or not all(x.isalpha() or x.isspace() for x in nombre):
        print("Nombre o apellidos inválidos")
        return
    tipo = input("Tipo de cliente (REGISTRADO/SOCIO): ").strip().upper()
    if tipo not in ("REGISTRADO", "SOCIO"):
        print("Tipo de cliente inválido")
        return
    if tipo == "REGISTRADO":
        try:
            cuota_max = float(input("Cuota máxima permitida: "))
            if cuota_max <= 0:
                print("Cuota inválida")
                return
        except ValueError:
            print("Cuota debe ser un número")
            return
    else:
        cuota_max = None

    fecha_alta = datetime.now().strftime("%Y/%m/%d %H%M%S")
    cursor.execute("""
        INSERT INTO clientes (dni, nombre, tipo_cliente, cuota_max, fecha_alta)
        VALUES (%s, %s, %s, %s, %s)
    """, (dni, nombre, tipo, cuota_max, fecha_alta))
    conexion.commit()
    print("Cliente añadido")

#para consultar clientes
def consultar_cliente():
    dni = input("DNI del cliente: ").strip().upper()
    cursor.execute("SELECT * FROM clientes WHERE dni=%s", (dni,))
    cliente = cursor.fetchone()
    if cliente:
        print(cliente)
    else:
        print("Cliente no encontrado")

#editar atributos de un cliente ya existente
def editar_cliente():
    dni = input("DNI del cliente a editar: ").strip().upper()
    cursor.execute("SELECT * FROM clientes WHERE dni=%s", (dni,))
    if not cursor.fetchone():
        print("Cliente no encontrado")
        return

    nombre = input("Nuevo nombre y apellidos: ").strip()
    if not nombre or not all(x.isalpha() or x.isspace() for x in nombre):
        print("Nombre o apellidos inválidos")
        return
    tipo = input("Nuevo tipo de cliente (REGISTRADO/SOCIO): ").strip().upper()
    cuota_max = None
    if tipo not in ("REGISTRADO", "SOCIO"):
        print("Tipo de cliente inválido")
        return
    if tipo == "REGISTRADO":
        try:
            cuota_max = float(input("Cuota máxima permitida: "))
            if cuota_max <= 0 or cuota_max > 1000:  # ejemplo de límite máximo
                print("Cuota inválida")
                return
        except ValueError:
            print("Cuota debe ser un número")
            return
    else:
        cuota_max = None
    cursor.execute("""
        UPDATE clientes
        SET nombre=%s, tipo_cliente=%s, cuota_max=%s
        WHERE dni=%s
    """, (nombre, tipo, cuota_max, dni))
    conexion.commit()
    print("Cliente actualizado")

#eliminar un cliente
def eliminar_cliente():
    dni = input("DNI del cliente a eliminar: ").strip().upper()
    cursor.execute("SELECT nombre FROM clientes WHERE dni=%s", (dni,))
    cliente = cursor.fetchone()
    if not cliente:
        print("Cliente inexistente.")
        return
    nombre_cliente = cliente[0]
    cursor.execute("SELECT COUNT(*) FROM recibos WHERE dni_cliente=%s", (dni,))
    recibos = cursor.fetchone()[0]
    if recibos > 0:
        print(f"No se puede eliminar al cliente {nombre_cliente}: tiene {recibos} recibo(s) asociado(s).")
        return
    cursor.execute("DELETE FROM clientes WHERE dni=%s", (dni,))
    conexion.commit()
    print(f"Cliente {nombre_cliente} eliminado correctamente.")

#muestra todos los clientes
def listar_clientes():
    orden = input("Ordenar por (DNI/fecha): ").strip().lower()
    if orden == "dni":
        cursor.execute("SELECT * FROM clientes ORDER BY dni")
    else:
        cursor.execute("SELECT * FROM clientes ORDER BY fecha_alta")
    for cliente in cursor.fetchall():
        print(cliente)

#para añadir un recibo a un cliente
def añadir_recibo():
    while True:
        try:
            numero = int(input("Número de recibo: "))
        except ValueError:
            print("Número de recibo debe ser un número entero.")
            continue

        cursor.execute("SELECT numero FROM recibos WHERE numero=%s", (numero,))
        if cursor.fetchone():
            print("Recibo con ese número ya existe")
        else:
            break
    while True:
        dni = input("DNI del cliente: ").strip().upper()
        cursor.execute("SELECT tipo_cliente, cuota_max, fecha_alta FROM clientes WHERE dni=%s", (dni,))
        cliente = cursor.fetchone()
        if not cliente:
            print("Cliente no encontrado.")
        else:
            tipo, cuota_max, fecha_alta_str = cliente
            break
    while True:
        try:
            importe = float(input("Importe del recibo: "))
            if importe <= 0:
                print("El importe debe ser mayor que 0")
                continue
            if tipo == "REGISTRADO" and importe > cuota_max:
                print(f"Importe supera la cuota máxima ({cuota_max}) del cliente REGISTRADO")
                continue
            break
        except ValueError:
            print("El importe debe ser un número válido.")

    while True:
        fecha_emision_str = input("Fecha de emisión (yyyy/MM/dd HHmmss) o ENTER para ahora: ").strip()
        if fecha_emision_str == "":
            fecha_emision = datetime.now()
        else:
            try:
                fecha_emision = datetime.strptime(fecha_emision_str, "%Y/%m/%d %H%M%S")
            except ValueError:
                print("Formato de fecha incorrecto. Inténtalo de nuevo.")
                continue
        break
    cursor.execute("""
        INSERT INTO recibos (numero, dni_cliente, importe, fecha_emision)
        VALUES (%s, %s, %s, %s)
    """, (numero, dni, importe, fecha_emision))
    conexion.commit()
    print("Recibo añadido")

#consultar recibos d eun cliente
def consultar_recibos_cliente():
    dni = input("DNI del cliente: ").strip().upper()
    cursor.execute("SELECT * FROM recibos WHERE dni_cliente=%s ORDER BY fecha_emision", (dni,))
    recibos = cursor.fetchall()
    if recibos:
        for r in recibos:
            print(r)
    else:
        print("No hay recibos")

#eliminar recibo
def eliminar_recibo():
    try:
        numero = int(input("Número de recibo a eliminar: "))
    except ValueError:
        print("El número de recibo debe ser un número entero.")
        return
    cursor.execute("SELECT dni_cliente FROM recibos WHERE numero=%s", (numero,))
    resultado = cursor.fetchone()
    if not resultado:
        print("Recibo inexistente.")
        return
    dni_cliente = resultado[0]
    cursor.execute("SELECT nombre FROM clientes WHERE dni=%s", (dni_cliente,))
    cliente = cursor.fetchone()
    if not cliente:
        print("Cliente asociado inexistente.")
        return
    cursor.execute("DELETE FROM recibos WHERE numero=%s", (numero,))
    conexion.commit()
    print(f"Recibo {numero} eliminado correctamente para el cliente {dni_cliente}.")

#editar atributos de un recibo
def editar_recibo():
    numero = int(input("Número de recibo a editar: "))
    cursor.execute("SELECT dni_cliente, importe FROM recibos WHERE numero=%s", (numero,))
    recibo = cursor.fetchone()
    if not recibo:
        print("No existe ese recibo")
        return

    dni, _ = recibo
    cursor.execute("SELECT tipo_cliente, cuota_max FROM clientes WHERE dni=%s", (dni,))
    tipo, cuota_max = cursor.fetchone()
    while True:
        try:
            nuevo_importe = float(input("Nuevo importe: "))
            if nuevo_importe <= 0:
                print("El importe debe ser mayor que 0")
                continue
            if tipo == "REGISTRADO" and nuevo_importe > cuota_max:
                print(f"Importe supera la cuota máxima ({cuota_max}) del cliente REGISTRADO")
                continue
            break
        except ValueError:
            print("El importe debe ser un número válido.")

    while True:
        nueva_fecha_emision_str = input("Fecha de emisión (yyyy/MM/dd HHmmss) o ENTER para ahora: ").strip()
        if nueva_fecha_emision_str == "":
            nueva_fecha_emision = datetime.now()
        else:
            try:
                nueva_fecha_emision = datetime.strptime(nueva_fecha_emision_str, "%Y/%m/%d %H%M%S")
            except ValueError:
                print("Formato de fecha incorrecto. Inténtalo de nuevo.")
                continue
        break    
    cursor.execute("""
        UPDATE recibos
        SET importe=%s, fecha_emision=%s
        WHERE numero=%s
    """, (nuevo_importe, nueva_fecha_emision, numero))
    conexion.commit()
    print("Recibo actualizado")

#muestra todos los recibos, según cliente o fecha
def listar_recibos():
    orden = input("Ordenar por (cliente/fecha): ").strip().lower()
    if orden == "cliente":
        cursor.execute("SELECT * FROM recibos ORDER BY dni_cliente")
    else:
        cursor.execute("SELECT * FROM recibos ORDER BY fecha_emision")
    for r in cursor.fetchall():
        print(r)

def main():
    while True:
        print("1. Añadir cliente")
        print("2. Consultar cliente")
        print("3. Editar cliente")
        print("4. Eliminar cliente")
        print("5. Listar clientes\n")
        print("6. Añadir recibo")
        print("7. Consultar recibos de cliente")
        print("8. Editar recibo")
        print("9. Eliminar recibo")
        print("10. Listar todos los recibos")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1": añadir_cliente()
        elif opcion == "2": consultar_cliente()
        elif opcion == "3": editar_cliente()
        elif opcion == "4": eliminar_cliente()
        elif opcion == "5": listar_clientes()
        elif opcion == "6": añadir_recibo()
        elif opcion == "7": consultar_recibos_cliente()
        elif opcion == "8": editar_recibo()
        elif opcion == "9": eliminar_recibo()
        elif opcion == "10": listar_recibos()
        elif opcion == "0": break
        else: print("Opción inválida.")

if __name__ == "__main__":
    a = main()
