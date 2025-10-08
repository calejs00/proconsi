import psycopg2

conexion = psycopg2.connect(
    dbname="agenda_db",
    user="postgres",
    password="tu_contraseña",
    host="localhost",
    port="5432"
)
cursor = conexion.cursor()
