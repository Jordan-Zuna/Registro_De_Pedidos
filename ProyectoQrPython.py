import random
import qrcode  # generar QR
# se usa la palabra reservada "pass" para rellenar hasta trabajar con la funcion
# es un tipo pasar para que no de errores 
detalleCompras = [[],[],[],[],[],[]]

def menuOpciones():
    print("¿Qué acción va a realizar?")
    print("* 1) Registrar pedidos")
    print("* 2) Mostrar pedidos")
    print("* 3) Mostrar detalle de un pedido")
    print("* 4) Eliminar un pedido")
    print("* 5) Salir del sistema")
    opcion=int(input("Elija una opcion: "))
    return opcion

def ingresarPedido():
    print("Ingrese los datos del cliente")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")

    detalleCompras[0].append(nombre)
    detalleCompras[1].append(apellido)
    detalleCompras[2].append(telefono)
    detalleCompras[3].append(direccion)
    detalleCompras[4].append(random.randrange(1000, 9999))

    print("Seleccione el paquete ofimático a contratar")
    print("""   1) Opción 1: PC + Monitor = $500
    2) Opcion 2: PC + Monitor 4k = $2000
    3) Opcion 3: Laptop UltraProIA = $1500
    4) Opcion 4: Worstation servidor = $3000""")
    opcion = int(input("Elija una opcion: "))

    if opcion == 1:
        detalleCompras[5].append(500+(0.15*500))
    elif opcion == 2:
        detalleCompras[5].append(2000+(0.15*2000))
    elif opcion == 3:
        detalleCompras[5].append(1500+(0.15*1500))
    elif opcion == 4:
        detalleCompras[5].append(3000+(0.15*3000))
    
    print("Pedido registrado")

def mostrarPedido(i):
    print("\n--- Datos del cliente ---\n")
    print("* Nombre: ", detalleCompras[0][i])
    print("* Apellido: ", detalleCompras[1][i])
    print("* Telefono: ", detalleCompras[2][i])
    print("* Dirección: ", detalleCompras[3][i])
    print("* Código de pedido: ", detalleCompras[4][i])
    print("* Total a pagar con IVA: ", detalleCompras[5][i])

def mostrarPedidos():
    if len(detalleCompras[0])==0:
        print("No hay pedidos registrados")
        return
    else:
        print("Lista de pedidos")
        for c in range(len(detalleCompras[0])):
            mostrarPedido(c)

def mostrarDetallePedido():
    if len(detalleCompras[0]) == 0:
        print("No hay pedidos registrados")
        return
    else:
        codigo = int(input("Ingrese el codigo del pedido: "))
        if codigo in detalleCompras[4]:
            codigoIndex = detalleCompras[4].index(codigo)
            mostrarPedido(codigoIndex)
            pagoQrPichincha(codigoIndex)
        else:
            print("El codigo ingresado no existe")    

def eliminarPedido():
    codigo = int(input("Ingrese el codigo del pedido: "))
    if codigo in detalleCompras[4]:
        codigoIndex = detalleCompras[4].index(codigo)  # usamos index para que en base al codigo ingresado me muestre la posicion
        for f in range(len(detalleCompras[0])):
            detalleCompras[f].pop(codigoIndex)
            print("Pedido eliminado con éxito")
    else:
        print("El codigo ingresado no existe")

def pagoQrPichincha(i):
    #   SE GENERAN CODIGOS QR
    textoPago = f"Datos del pago\n * Código del pedido: {detalleCompras[4][i]}\n * Pago final: $ {detalleCompras[5][i]}\n"
    codigoQr = qrcode.make(textoPago)
    nombreArchivo = "CodigoQr.png"
    codigoQr.save(nombreArchivo, scale=8)
    print("Codigo QR generado exitosamente para el pago")

def main():
    print("\n--- BIENVENIDO A TECHWORLD ----\n")
    opcion = menuOpciones()
    while opcion != 5:
        if opcion == 1:
            ingresarPedido()
        elif opcion == 2:
            mostrarPedidos()
        elif opcion == 3:
            mostrarDetallePedido()
        elif opcion == 4:
            eliminarPedido()
        opcion = menuOpciones()
        print("Gracias por usar el sistema")
main()