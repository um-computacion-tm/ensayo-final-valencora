from dispositivo import Dispositivo

class Database:
    def __init__(self, data):
        lista = data.get("dispositivos", [])
        self.database = []
        for i in lista:
            self.database.append(Dispositivo(diccionario=i))
        
                
    def delete_by_id(self, id):
        for dispositivo in self.database:
            if dispositivo.id == id:
                self.database.remove(dispositivo)
                
    def add_dispositivo(self, dispositivo=None, diccionario=None):
        if diccionario:
            dispositivo = Dispositivo(diccionario=diccionario)
        if dispositivo:
            self.database.append(dispositivo)