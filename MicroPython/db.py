import time
import pymysql
import pymysql.cursors

mydb = pymysql.connect(
host="localhost",
user="pico",
password="sanluis",
database="test"
)

# Crea el cursor para poder acceder y manipular datos en la base de datos (Simulando que hemos pasado una tarjeta RFID)
cursor = mydb.cursor()

# Crea la tabla en la que se van a pasar los datos de tiempo
cursor.execute("CREATE TABLE IF NOT EXISTS rfid_record (rfid VARCHAR(64), timestamp DATETIME(2))")

# Comprueba continuamente si ha pasado una tarjeta RFID
while True:
    rfid = input("Esperando tarjeta RFID: ")

# Consigue tiempo actual del sistema
    kernel_time = time.strftime('%Y-%m-%d %H:%M:%S')

# Manda el tiempo actual del sistema a la base de datos
    sql = "INSERT INTO rfid_record (timestamp) VALUES (%s)"
    val = (kernel_time)
    mydb.commit()

# Notifica de que todo ha funcionado correctamente
    print("Datos escaneados y enviados correctamente")