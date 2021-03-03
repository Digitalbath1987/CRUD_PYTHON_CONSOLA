import Cliente

print("1. Obtener")
print("2. Crear")
print("3. Editar")
print("4. Eliminar")
op = input("Selecciona una opcion : ")

if op == "1":
    oCliente  = Cliente.Cliente
    oCliente.Obtener()
elif op == "2":
    oCliente  = Cliente.Cliente
    NOMBRE = input("Ingrese el NOMBRE : ")
    RUT = input("Ingrese el RUT : ")
    TELEFONO_1 = input("Ingrese el TELEFONO_1 : ")
    TELEFONO_2 = input("Ingrese el TELEFONO_2 : ")
    ID_CIUDAD = 1
    DIRECCION = input("Ingrese el DIRECCION : ")
    EMAIL = input("Ingrese el EMAIL : ")
    ID_COMERCIAL = 1
    ESTADO = 1
    NOMBRE_CONTACTO = input("Ingrese el NOMBRE_CONTACTO : ")
    COD_POSTAL = input("Ingrese el COD_POSTAL : ")
    GIRO = input("Ingrese el GIRO : ")
    oCliente.ADD(NOMBRE,RUT,TELEFONO_1,TELEFONO_2,ID_CIUDAD,DIRECCION,EMAIL,ID_COMERCIAL,ESTADO,NOMBRE_CONTACTO,COD_POSTAL,GIRO)
elif op == "3":
    oCliente  = Cliente.Cliente
    oCliente.Obtener()
    ID_CLIENTE = input("cual ID_CLIENTE desea EDITAR : ")
    NOMBRE = input("Ingrese el NOMBRE : ")
    RUT = input("Ingrese el RUT : ")
    TELEFONO_1 = input("Ingrese el TELEFONO_1 : ")
    TELEFONO_2 = input("Ingrese el TELEFONO_2 : ")
    ID_CIUDAD = 1
    DIRECCION = input("Ingrese el DIRECCION : ")
    EMAIL = input("Ingrese el EMAIL : ")
    ID_COMERCIAL = 1
    ESTADO = 1
    NOMBRE_CONTACTO = input("Ingrese el NOMBRE_CONTACTO : ")
    COD_POSTAL = input("Ingrese el COD_POSTAL : ")
    GIRO = input("Ingrese el GIRO : ")
    oCliente.EDIT(NOMBRE,RUT,TELEFONO_1,TELEFONO_2,ID_CIUDAD,DIRECCION,EMAIL,ID_COMERCIAL,ESTADO,NOMBRE_CONTACTO,COD_POSTAL,GIRO,ID_CLIENTE)
elif op == "4":
    oCliente  = Cliente.Cliente
    oCliente.Obtener()
    ID_CLIENTE = input("cual cliente desea ELIMINAR : ")
    oCliente.DELETE(ID_CLIENTE)
else:
    print("Opcion Invalida")





