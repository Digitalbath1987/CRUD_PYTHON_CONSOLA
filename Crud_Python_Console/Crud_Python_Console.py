import pyodbc

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





