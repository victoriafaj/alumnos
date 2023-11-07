import mysql.connector
from mysql.connector import Error

open_menu = 1


def estado():
    try:
        conexion = mysql.connector.connect(
            host = "localhost",
            port = '3306',
            user='root',
            password="",
            db="alumno"
        )

        if conexion.is_connected():
            print("Conexión existosa.")
            infoServer = conexion.get_server_info()
            print("Información del servidor: ", infoServer)
    except Error as ex:
        print("Error de conexión con la base de datos ", ex)
    finally: 
        if conexion.is_connected():
            conexion.close()
            print("La conexión ha finalizado.")

def mostrar():
    try:
        conexion = mysql.connector.connect(
            host = "localhost",
            port = '3306',
            user='root',
            password="",
            db="alumno"
        )

        if conexion.is_connected():
            print("Conexión existosa.")
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM alumno")
            registro = cursor.fetchone()
            print("Conectado a la DB", registro)
            resultados = cursor.fetchall()
            for fila in resultados:
                print(fila[0], "//", fila[1], "//", fila[2], "//", fila[3], "//", fila[4])
            print("Total de registros: ", cursor.rowcount)
    except Error as ex:
        print("Error de conexión con la base de datos ", ex)
    finally: 
        if conexion.is_connected():
            conexion.close()
            print("La conexión ha finalizado.")

def agregar():

    try:
        conexion = mysql.connector.connect(
            host = "localhost",
            port = '3306',
            user='root',
            password="",
            db="alumno"
        )
        if conexion.is_connected():
            nombre1 = input("Nombre: ")
            dni1 = int(input("Dni: "))
            domicilio1 = input("Domicilio: ")
            email1 = input("Mail: ")
            print("Conexión existosa.")
            cursor = conexion.cursor()
            cursor.execute(f"INSERT INTO alumno (Nombre, DNI, Domicilio, Email) VALUES ('"+ nombre1 +"', '"+str(dni1)+"', '"+domicilio1+"', '"+email1+"')")
            conexion.commit()

    except mysql.connector.Error as ex:
        print("Error al ejecutar ", ex)
    finally: 
        if conexion.is_connected():
            conexion.close()
            print("La conexión ha finalizado.")

def editar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            db="alumno"
        )

        if conexion.is_connected():
            print("Conexión exitosa.")
            cursor = conexion.cursor()

            dato_actualizar = int(input("Ingrese el DNI del registro que desea actualizar: "))

            nombre1 = input("Nuevo nombre: ")
            dni1 = int(input("Nuevo dni: "))
            domicilio1 = input("Nuevo domicilio: ")
            email1 = input("Nuevo mail: ")

            update_query = f"UPDATE alumno SET nombre = '{nombre1}', dni = {dni1}, domicilio = '{domicilio1}', email = '{email1}' WHERE DNI = {dato_actualizar}"

            cursor.execute(update_query)
            conexion.commit()

    except Error as ex:
        print("Error de conexión con la base de datos: ", ex)
    finally:
        if conexion.is_connected():
            conexion.close()
            print("La conexión ha finalizado.")


def eliminar():

    dni_nuevo = int(input("DNI a eliminar: "))
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            port='3306',
            user='root',
            password="",
            db="alumno"
        )

        if conexion.is_connected():
            print("Conexión exitosa.")
            cursor = conexion.cursor()
            
            alumno_dni = dni_nuevo 

            delete_query = f"DELETE FROM alumno WHERE DNI = {alumno_dni}"

            cursor.execute(delete_query)
            conexion.commit() 

    except Error as ex:
        print("Error de conexión: ", ex)
    finally:
        if conexion.is_connected():
            conexion.close()
            print("La conexión ha finalizado.")


while open_menu != 0:
    print("1. Mostrar datos")
    print("2. Registrar")
    print("3. Editar")
    print("4. Eliminar")
    print("5. Salir del menú")

    opcion = int(input("Elija una opción: "))

    if opcion == 6:
        open_menu = 0
    elif opcion == 1:
        mostrar()
    elif opcion == 2:
        agregar()
    elif opcion == 3:
        editar()
    elif opcion == 4:
        eliminar()
    


print("Fin")

