import pymysql

#Establecemos la conexion con la base de datos a utilizar
def obtener_conexion():
    return pymysql.connect(host='localhost',
                          user='root',
                          password='',
                          db='Prueba_conexion') #aqui va el nombre de la base de datos a usar
    
#ahora creamos funciones que ejecuten los sql

#Create (Creacion)
def insertar_info(dato_1 ,dato_2, dato_3):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO tabla_prueba(columna_1,columna_2,columna_3) VALUES(%s,%s,%s)", (dato_1 ,dato_2, dato_3))     
    conexion.commit()
    conexion.close()
    
#Read (Lectura)
def obtener_info():
    conexion = obtener_conexion()
    datos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM tabla_prueba")
        datos = cursor.fetchall()
    conexion.close()
    return datos

#Update (Actualizar)
def actualizar_info(dato_1, dato_2, dato_3, dato_4):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE tabla_prueba SET columna_1= %s, columna_2= %s, columna_3= %s WHERE columna_4= %s", (dato_1, dato_2, dato_3, dato_4))        
        conexion.commit()
        conexion.close()
        

#Delete (Borrar)
def eliminar_info(dato):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM tabla_prueba WHERE columna=%s", (dato))
        conexion.commit()
        conexion.close()
        
