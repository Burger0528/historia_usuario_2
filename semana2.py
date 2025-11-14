# Historia de usuario - Semana 2
# Control de flujo y manejo de listas en el inventario

# En este sistema el usuario puede:
# - Registrar nuevos productos
# - Consultar el inventario
# - Actualizar productos
# - Eliminar productos
# - Buscar productos por código


productos={}

def mostrar_menu():
    print("======menu principal=======")
    print("1. ver productos ")
    print("2. registrar productos")
    print("3. actualizar producto")
    print("4. eliminar un producto")
    print("5. buscar un producto")
    print("0. salir ")

# funcion para ver productos
def mostrar_productos():
    if not productos:
        print("============================")
        print("no hay productos para mostra")
        print("============================")
    else:
        print("=====Inventario=====")
        #recorremos los datos para mostrar el inventario
        for codigo,(nombre,precio,cantidad) in productos.items():
            print(F" codigo  -  nombre  -  precio  -  cantidad")
            print(F"{codigo} - {nombre} - {precio} - {cantidad}")

#Mostra productos
def registrar_productos():
    try:
        codigo=int(input("Ingrese el codigo del producto: "))
        if codigo in productos:
            print("======================")
            print("El producto ya existe ")
            print("======================")
            return      
          #salimos si el producto existe
        nombre=input("Ingrese el nombre del producto: ")
        precio=input("Ingrese el precio del producto: ")
        cantidad=input("Ingrese la cantidad del producto: ")

        productos[codigo]=(nombre, precio, cantidad)
        print(f"{nombre} registrado con exito")
    except ValueError:
        print("ingrese un numero valido, intente nuevamente")

def eliminar_producto():
    try: 
        codigo = int(input("ingrese el codigo del producto a eliminar"))
        if codigo in productos:
            eliminado = productos.pop(codigo)
            print("el producto fue eliminado del inventario")
        else:
            print("el producto no existe")
    except ValueError:
        print("ingrese un numero codigo valido")

def actualizar_producto():
    try:
        codigo = int(input("ingrese el codigo del producto a actualizar"))
        if codigo in productos:
            nombre=input("Ingrese el nombre del producto: ")
            precio=input("Ingrese el precio del producto: ")
            cantidad=input("Ingrese la cantidad del producto: ")
            #recorremos y renombramos donde encuentra al la clave codigo
            productos[codigo]=(nombre, precio, cantidad)
            print(f"{nombre} actualizado con exito")

        else:
            print("producto no existe")

    except ValueError:
        print("ingrese un numero valido")
 
def buscar_producto():
    try:
        codigo=int(input("Ingrese el codigo del producto que deseas buscar"))
        if codigo in productos:
            nombre, precio, cantidad = productos[codigo]
            print("producto encontrado")
            print(f"el produco con codigo {codigo}, nombre: {nombre}, precio: {precio}, cantidad: {cantidad}")

        else:
            print("el producto no existe")

    except ValueError:
        print("ingrese un numero valido")
    


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            registrar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            buscar_producto()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente nuevamente")

# Ejecutar el programa
if __name__ == "__main__":
    main()
