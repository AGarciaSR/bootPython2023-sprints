import json
from .Usuario import Usuario

class Cliente(Usuario):
    def __init__(self, id, nombre, apellido, correo, fecha_registro, password, ciudad, saldo, compras = None):
        self.apellido = apellido
        self.correo = correo
        self.fecha_registro = fecha_registro
        self.ciudad = ciudad
        self.__saldo = saldo
        self.compras = json.loads(compras)
        super().__init__(id, nombre, apellido, password)
    
    #Método para añadir saldo    
    def mod_saldo(self, ingreso):
        self.__saldo += ingreso
        
    #Método para obtener saldo del cliente
    def get_saldo(self):
        return self.__saldo
        
    def promedio_compras(self):
        promedio = 0
        for compra in self.compras:
            promedio += compra['ValorTotal']
        try:
            promedio /= len(self.compras)
        except ZeroDivisionError:
            promedio = "El cliente seleccionado no ha efectuado ninguna compra"
        return promedio