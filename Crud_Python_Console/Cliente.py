import pyodbc
class Cliente:
    
    #Conexion a SQL Server CONEXION
    def Conn():
        Conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=MARIOROSALES\DIGITALDB;'
                      'Database=operaciones;'
                      'UID=sa;'
                      'PWD=123456;')
        return Conn


        #Conexion a SQL Server READ
    def Obtener():
        Conn    = Cliente.Conn()
        Cursor  = Conn.cursor();
        try:
            Cursor.execute('SELECT * FROM CLIENTE with(nolock)')
            for row in Cursor:
                print(row)
        except():
            print("Error en Coneccion")
        finally:
            Conn.close()

        #Conexion a SQL Server CREATE
    def ADD(NOMBRE,RUT,TELEFONO_1,TELEFONO_2,ID_CIUDAD,DIRECCION,EMAIL,ID_COMERCIAL,ESTADO,NOMBRE_CONTACTO,COD_POSTAL,GIRO):
        try:
            Conn    = Cliente.Conn()
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
