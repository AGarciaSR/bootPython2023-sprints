# Importaciones de módulos
import time
from excepcion.excepcion_usuario import NuevaExcepcion
from functions.banner import banner
from functions.muestra_clientes import muestra_clientes
from models.Usuario import Usuario
from models.Cliente import Cliente
from models.Bodega import Bodega
from models.OrdenCompra import OrdenCompra
from models.Proveedor import Proveedor
from models.Producto import Producto
# Stock inicial de productos y clientes
stock = []
fields = {}
listaClientes = []
compras = []
    
def dump_csv_data(file,typefile):
    global fields
    # Abrimos el archivo
    users_file = open(file,'r', encoding = 'utf-8')
    # Leemos las líneas del archivo
    data = users_file.readlines()
    # Cerramos el archivo para liberar recursos
    users_file.close()
    # Pasamos la primera línea del CSV a una lista aparte, para manejarlo después
    fields[typefile] = data[0].strip().split(';')
    # Eliminamos la primera línea,que contiene los nombres de campo, para dejar sólo los datos de usuario
    data.pop(0)
    # Dependiendo de lo que le pasemos en "typefile", tratará el CSV como clientes, productos, etcétera
    if typefile == "users":
        for user in data:
            user = user.strip().split(';')
            nuevo_cliente = Cliente(user[0],user[1],user[2],user[3],user[4],user[5],user[6],int(user[7]),user[8])
            listaClientes.append(nuevo_cliente)
        
def write_csv_data(file,typefile):
    users_file = open(file,'w', encoding = 'utf-8')
    for data in fields[typefile]:
        users_file.write(data+";")
    users_file.write("\n")
    if typefile == "users":
        for user in listaClientes:
            users_file.write(f"{user.id};{user.nombre};{user.apellido};{user.correo};{user.fecha_registro};{user.password};{user.ciudad};{int(user.get_saldo())};{user.compras}\n")
    
# Verificar el stock antes de procesar la compra
def verifica_stock(producto,cantidad):
    if stock[producto] >= cantidad:
        return True
    else:
        return False
    
def ingresa_saldo():
    cliente = muestra_clientes(listaClientes)
    ingreso = int(input('Ingrese el saldo a añadir: '))
    listaClientes[cliente-1].add_saldo(ingreso)
    
def ver_saldo():
    cliente = muestra_clientes(listaClientes)
    print(listaClientes[cliente-1].get_saldo())

def ver_promedio_compras():
    cliente = muestra_clientes(listaClientes)
    print(listaClientes[cliente-1].promedio_compras())
        
class Administrativo(Usuario):
    def __init__(self, id, nombre, apellido, password, fecha_incorporacion, oficina, salario, fecha_nacimiento = None):
        super().__init__(id, nombre, apellido, password)
        self.fecha_incorporacion = fecha_incorporacion
        self.oficina = oficina
        self.salario = salario
        self.fecha_nacimiento = fecha_nacimiento
        
    # Almacenar nuevos productos
    def ingresa_producto(self):
        banner('Ingresar nuevo producto')
        sku = int(input('Ingrese el SKU del nuevo producto: '))
        producto = input('Ingrese el nombre del nuevo producto: ')
        categoria = input('Ingrese la categoría del producto: ')
        valor_neto = int(input('¿Cuál es el valor del producto?: '))
        cantidad = int(input('¿Cuántas unidades tendremos de este producto?: '))
            
        nuevo_producto = Producto(sku, producto, categoria, cantidad, valor_neto)
        # Composición de la clase Producto, asignándole un proveedor, hardcodeado para la ocasión, pero la idea es crearlo con un método "ingresa_proveedor"
        nuevo_producto.proveedor = Proveedor("12345678-9", "La Falsa Polar", "Comercializadora de Productos de Dudoso Origen La Polar SpA", "Chile", "Jurídica")
        stock.append(nuevo_producto)
        print('El producto ha sido añadido al catálogo')
        time.sleep(2)
    
    # Ingresa nuevo cliente a la "base de datos" (necesario recodificar a modo de objetos)
    """def ingresa_cliente(self):
        banner('Ingresar nuevo cliente')
        nombre = input('Ingrese el nombre del cliente: ')
        password = input('Ingrese la contraseña del cliente: ')
        if nombre not in listaClientes:
            id = int(list(listaClientes)[-1]) + 1
            clientes[str(id)] = {'nombre' : nombre, 'password' : password}
            print('Se añadió el cliente a la base de datos')
        else:
            print('El cliente ya está registrado, se ignorarán los datos')
        time.sleep(2)"""
        
    # Mostrar clientes registrados
    def listado_clientes(self):
        banner('Nuestros clientes')
        i = 0
        for key in listaClientes:
            print(f'{i+1}) {key.nombre} {key.apellido}')
            i += 1
        
class Vendedor(Usuario):
    def __init__(self, id, nombre, apellido, password, run, fecha_incorporacion, salario, seccion = None):
        super().__init__(id, nombre, apellido, password)
        self.fecha_incorporacion = fecha_incorporacion
        self.seccion = seccion
        self.salario = salario
        self.run = run
        self.__comision = 0
    
    # Añadir unidades a un producto del catálogo
    def actualiza_stock(self):
        banner('Actualizar stock')
        print('Seleccione el producto al cual añadiremos unidades')
        stockNames = []
        stockList = []
        i = 1
        try:
            for key in stock:
                stockNames.append(key)
                stockList.append(stock[key])
                print(f'{i}) {key}')
                i += 1
            producto = int(input('Ingrese el número del producto:'))
            cantidad = int(input('¿Cuántas unidades añadiremos?: '))
            stock[stockNames[producto-1]] = stock[stockNames[producto-1]] + cantidad
        except TypeError:
            print('Esta función está en mantenimiento, le informaremos pronto')
        
    # Mostrar unidades por producto
    def muestra_unidades(self):
        banner('Unidades por producto')
        for producto in stock:
            print(f'{producto.nombre}: {producto.stock}')
            
    # Mostrar unidades de un producto en particular
    def muestra_unidades_producto(self):
        banner('Unidades de un producto')
        print('Seleccione el producto del cual quiere saber las unidades en stock')
        # Listas auxiliares para mostrar los nombres de los productos y almacenar temporalmente el stock
        stockNames = []
        stockList = []
        i = 1
        for key in stock:
            stockNames.append(key)
            stockList.append(stock[key])
            print(f'{i}) {key}')
            i += 1
        producto = int(input('Ingrese el número del producto:'))
        if producto <= len(stockList) and producto > 0:
            print(f'Tenemos actualmente {stockList[producto-1]} unidades de {stockNames[producto-1]}')
        else:
            print('Introdujo una opción incorrecta')
            time.sleep(2)

# Metodo para Vender Producto
    def vender_producto(self):
        # Diccionario con los productos que se irán comprando, formando así una colaboración
        productos_comprados = {}
        stockNames = []
        stockList = []
        valor_compra = 0
        clienteChoose = 0
        productoChoose = 0
        cantidad = 0
        while clienteChoose == 0:
            # Input con clientes 
            clienteChoose = muestra_clientes(listaClientes)
        while True:
            while productoChoose == 0:
                banner('Venta de Producto')
                print('Seleccione el producto a vender')
                i = 1
                for producto in stock:
                    stockNames.append(producto.nombre)
                    stockList.append(producto.stock)
                    print(f'{i}) {producto.nombre}')
                    i += 1
                try:
                    productoChoose = int(input('Ingrese el número del producto:'))
                    if productoChoose <= 0 or productoChoose > len(stock):
                        raise IndexError
                except IndexError:
                    print("Ha seleccionado una opción incorrecta")
                    productoChoose = 0
                except ValueError: 
                    print("Ha introducido un caracter inválido")
                    productoChoose = 0
                finally:
                    time.sleep(2)
            while cantidad == 0:
                try:
                    cantidad = int(input('¿Cuántas unidades venderemos?: '))
                    if cantidad <= 0:
                        raise ValueError
                    elif cantidad > 11:
                        raise NuevaExcepcion
                except ValueError: 
                    print("Ha introducido un caracter o cantidad inválidos")
                    cantidad = 0
                except NuevaExcepcion:
                    print("Solo pueden añadirse hasta 10 unidades de un artículo")
                    cantidad = 0
                finally:
                    time.sleep(2)
                
        
            # Comprobar que se tiene suficiente stock en la tienda
            try:
                if(stock[productoChoose-1].stock >= cantidad):
                    # Calculamos el valor total de la compra contando comisión del vendedor y el impuesto
                    # El impuesto lo guardamos como string
                    impuesto = stock[productoChoose-1].get_impuesto()
                    calImpuesto = stock[productoChoose-1].valor_neto * impuesto
                    valorTotal = (stock[productoChoose-1].valor_neto + calImpuesto) * cantidad
                    comision = valorTotal * 0.005
                    # Comprobar si el cliente tiene saldo suficiente
                    if listaClientes[clienteChoose-1].get_saldo() >= valorTotal:
                        self.__comision += comision
                        print(f"El Valor Neto es: {stock[productoChoose-1].valor_neto * cantidad}, El Impuesto es: {calImpuesto * cantidad} y el Valor Total es : {valorTotal}  ")
                        stock[productoChoose-1].stock -= cantidad
                        # Si tenemos menos de 50 en la tienda, pedir 300 más a la bodega
                        if(stock[productoChoose-1].stock < 50):
                            try:
                                if (bodega1.stock[stock[productoChoose-1].nombre] >= 300):
                                    bodega1.stock[stock[productoChoose-1].nombre] -= 300
                                    stock[productoChoose-1].stock += 300
                                    print(f"El stock de {stock[productoChoose-1].nombre} es bajo, se están pidiendo 300 más a la bodega")
                                else:
                                    raise NuevaExcepcion
                            except NuevaExcepcion:
                                print(f"El stock de {stock[productoChoose-1].nombre} es bajo, no existen suficientes unidades en la bodega para reponer")
                        if not stock[productoChoose-1].nombre in productos_comprados:
                            productos_comprados[stock[productoChoose-1].nombre] = cantidad
                        else:
                            productos_comprados[stock[productoChoose-1].nombre] += cantidad
                        valor_compra += valorTotal
                        time.sleep(2)
                        if input("¿Terminar compra? (1: SI - Otra tecla: NO): ") == "1":
                            selDespacho = int(input('¿Desea despacho a Domicilio?(0:no, 1:si)'))
                            sumaDespacho = selDespacho*5000
                            valor_compra += sumaDespacho
                            listaClientes[clienteChoose-1].mod_saldo(-valor_compra)
                            print(f"El valor total de su compra es: {valor_compra}, con un valor incluido de despacho de {sumaDespacho}")
                            # "Hardcodearemos" el ID, pero en una BDD, esto se haría con un AUTO_INCREMENT
                            nueva_orden_compra = OrdenCompra("NuevaOC", productos_comprados, selDespacho, listaClientes[clienteChoose-1].id, valor_compra)
                            compras.append(nueva_orden_compra)
                            listaClientes[clienteChoose-1].compras.append({'Productos' : productos_comprados , 'Despacho' : selDespacho , 'ValorTotal' : valor_compra})
                            write_csv_data('clientes.csv','users')
                            break
                    else:
                        print('El saldo del cliente no es suficiente para efectuar la compra.')
                        
                else:
                    raise NuevaExcepcion
            except NuevaExcepcion:
                print("El saldo del cliente no es suficiente para efectuar la compra.")
                time.sleep(2)
                break



# Creamos los objetos con las nuevas clases
administrativo = Administrativo('a1','Paulina','Fernández','Paulina_1992','2023/03/05','Quilpué',1120000)
vendedor = Vendedor('v1','Marcos','Pérez','Marcos_45','12345678-9','2023/04/15','Informática',800000)

dump_csv_data('clientes.csv','users')

producto1 = Producto('345675', 'Polera roja estampada', 'Vestuario Adulto', 12, 4500)
bodega1 = Bodega('bodega1', 'Bodega Santiago', {'Polera roja estampada' : 900})
stock.append(producto1)

functions = ['', '''administrativo.ingresa_cliente''', administrativo.ingresa_producto, vendedor.actualiza_stock, vendedor.muestra_unidades, vendedor.muestra_unidades_producto, administrativo.listado_clientes, ingresa_saldo, ver_saldo, ver_promedio_compras, vendedor.vender_producto]

while True:
    banner('Bienvenido')
    # Imprimir el menú
    print('1) Ingresa nuevo cliente\n2) Ingresar nuevo producto\n3) Añadir unidades a producto existente\n4) Mostrar unidades por producto\n5) Ver las unidades de un producto\n6) Mostrar listado de clientes\n7) Añadir saldo al cliente\n8) Obtener saldo del cliente\n9) Ver promedio de compras del cliente\n\n10) Vender producto \n0) Salir')
    try:
        eleccion = int(input('Su elección: '))
        if eleccion == 0:
            print('Gracias, vuelva pronto')
            time.sleep(2)
            break
        elif eleccion < 0:
            raise IndexError
        # Llamamos a la función correspondiente a la posición en la lista
        else:
            functions[eleccion]()
    except IndexError:
        print("Ha seleccionado una opción incorrecta")
    except ValueError: 
        print("Ha introducido un caracter inválido")
    input('Pulse Enter para continuar')