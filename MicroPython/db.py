import time
import pymysql

conn = pymysql.connect(
host="localhost",
user="pico",
password="sanluis",
db="test"
)

# Crea el cursor para poder acceder y manipular datos en la base de datos (Simulando que hemos pasado una tarjeta RFID)
cursor = conn.cursor()

# Consigue tiempo actual del sistema
current_time = time.strftime('%Y-%m-%d %H:%M:%S')

# Fomatear kernel_time a un formato legible para MicroPyton
time_string = "{}/{}/{} {}:{}:{}".format(current_time[0], current_time[1], current_time[2], current_time[3], current_time[4], current_time[5])

# Crea la tabla en la que se van a pasar los datos de tiempo
cursor.execute("CREATE TABLE IF NOT EXISTS rfid_record (rfid VARCHAR(64), timestamp DATETIME(2))")

# Comprueba continuamente si ha pasado una tarjeta RFID
while True:
    rfid = input("Esperando tarjeta RFID: ")


# Manda el tiempo actual del sistema a la base de datos
    cursor.execute("INSERT INTO rfid_record (timestamp) VALUES (%s)", time_string)

# Notifica de que todo ha funcionado correctamente
    print("Datos escaneados y enviados correctamente")
    
# Cerrar el cursor
cursor.close()