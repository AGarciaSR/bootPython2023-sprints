import time
from functions.banner import banner
def muestra_clientes(listaClientes):
    banner('Nuestros clientes')
    i = 1
    for cliente in listaClientes:
        print(f'{i}) {cliente.nombre} {cliente.apellido}')
        i += 1
    try:
        clienteChoose = int(input('Seleccione cliente: '))
        if clienteChoose <= 0 or clienteChoose > len(listaClientes):
            raise IndexError
        else:
            return clienteChoose
    except IndexError:
        print("Ha seleccionado una opción incorrecta")
        clienteChoose = 0
    except ValueError: 
        print("Ha introducido un caracter inválido")
        clienteChoose = 0