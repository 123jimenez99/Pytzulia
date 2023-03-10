import time
import mysql.connector


mydb = mysql.connector.connect(
host="localhost",
user="pico",
password="sanluis",
database="test"
)

# Crea el cursor para poder acceder y manipular datos en la 
mycursor = mydb.cursor()

# Crea la tabla en la que se van a pasar los datos de tiempo
mycursor.execute("CREATE TABLE IF NOT EXISTS rfid_record (rfid VARCHAR(255), timestamp VARCHAR(255))")

# Comprueba continuamente si ha pasado una tarjeta RFID
while True:
    rfid = input("Esperando tarjeta RFID: ")

# Consigue tiempo actual del sistema
    kernel_time = time.strftime('%Y-%m-%d %H:%M:%S')

# Manda el tiempo actual del sistema a la base de datos
    sql = "INSERT INTO rfid_record (rfid, timestamp) VALUES (%s, %s)"
    val = (rfid, kernel_time)
    mycursor.execute(sql, val)
    mydb.commit()

# Notifica de que todo ha funcionado correctamente
    print("Datos escaneados y enviados correctamente")