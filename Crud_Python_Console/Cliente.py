import pyodbc
class Cliente:

    def Obtener():
        #Conexion a SQL Server
        try:
            Conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=MARIOROSALES\DIGITALDB;'
                      'Database=operaciones;'
                      'UID=sa;'
                      'PWD=123456;')
            Cursor  = Conn.cursor();
            Cursor.execute('SELECT * FROM CLIENTE with(nolock)')
            for row in Cursor:
                print(row)
        except():
            print("Error en Coneccion")
        finally:
            Conn.close()

    def ADD(NOMBRE,RUT,TELEFONO_1,TELEFONO_2,ID_CIUDAD,DIRECCION,EMAIL,ID_COMERCIAL,ESTADO,NOMBRE_CONTACTO,COD_POSTAL,GIRO):
        #Conexion a SQL Server
        try:
            Conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=MARIOROSALES\DIGITALDB;'
                      'Database=operaciones;'
                      'UID=sa;'
                      'PWD=123456;')
            Cursor  = Conn.cursor();
            Query   = ('INSERT INTO CLIENTE'
                       '(NOMBRE'
                       ',RUT'
                       ',TELEFONO_1'
                       ',TELEFONO_2'
                       ',ID_CIUDAD'
                       ',DIRECCION'
                       ',EMAIL'
                       ',ID_COMERCIAL'
                       ',ESTADO'
                       ',NOMBRE_CONTACTO'
                       ',COD_POSTAL'
                       ',GIRO)'
                       'VALUES(?,?,?,?,?,?,?,?,?,?,?,?)')
            Cursor.execute(Query,[NOMBRE,RUT,TELEFONO_1,TELEFONO_2,ID_CIUDAD,DIRECCION,EMAIL,ID_COMERCIAL,ESTADO,NOMBRE_CONTACTO,COD_POSTAL,GIRO])
            Cursor.commit()
            print("REGISTRO REALIZADO CORRECTAMENTE")
        except():
            print("Error en Coneccion")
        finally:
            Conn.close()
