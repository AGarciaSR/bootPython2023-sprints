class Producto:
    def __init__(self, sku, nombre, categoria, stock, valor_neto) -> None:
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.stock = stock
        self.valor_neto = valor_neto
        self.__impuesto = 0.19
        self.proveedor = None
        
    def get_impuesto(self):
        return self.__impuesto