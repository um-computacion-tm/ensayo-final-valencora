class Dispositivo:
    def __init__(self, id=None, nombre=None, marca=None, tipo=None, diccionario=None):
        if diccionario:
            self.id = diccionario.get('id', None)
            self.nombre = diccionario.get('nombre', None)
            self.marca = diccionario.get('marca', None)
            self.tipo = diccionario.get('tipo', None)
        else:
            self.id = id
            self.nombre = nombre
            self.marca = marca
            self.tipo = tipo