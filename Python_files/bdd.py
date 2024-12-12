from StrToDic import Str2Doc

class Documento():
    def __init__(self, id, contenido = None):
        self.id = id
        self.contenido = contenido if contenido is not None else {}

    def obtn_valor(self,clave):
        return self.contenido.get(clave, None)
    
    def edit_valor(self, clave, valor):
        self.contenido[clave] = valor

    def __str__(self):
        return f"Documento(id={self.id}, contenido={self.contenido})"

class Coleccion():
    def __init__(self, nombre):
        self.nombre = nombre
        self.documentos = {}
        self.id = 0 #Se inicia en 0 para que sea autoincremental
    
    def add_doc(self, documento):
        self.documentos[documento.id] = documento

    def drop(self, id_documento):
        if id_documento in self.documentos:
            del self.documentos[id_documento]

    def search(self, id_documento):
        return self.documentos.get(id_documento, None)
    
    def import_colleccion(self, ruta): ###### TEST IMPORT CSV  ######
        userRuta = ruta

        with open(userRuta, "rt") as file:
            schema = file.readline().replace("/n","")
            csv = Str2Doc(schema)
            
            for line in file:
                nuevo = Documento(self.id, csv.convert(line.strip())) #strip elimina los espacios en blanco
                self.add_doc(nuevo)
                self.id +=1
    
    def __str__(self):
        return f"Coleccion {self.nombre} con {len(self.documentos)} documentos."

"""
c = Coleccion('Libros')
l1 = Documento(1, {"Titulo":"Python for all", "Autor":"BerZerK"})
l2 = Documento(2, {"Titulo":"HarryPotter", "Autor":"JK Row"})

c.add_doc(l1)
c.add_doc(l2)
libro = c.search(2)

print(libro.obtn_valor("Titulo"), libro.obtn_valor("Autor"))

#c.drop(l1[id])
"""

class BDD(object):
    def __init__(self, nombre):
        self.nombre = nombre
        self.colecciones = {}

    def create_collection(self, nombre_coleccion):
        if nombre_coleccion not in self.colecciones:
            self.colecciones[nombre_coleccion] = Coleccion(nombre_coleccion)
    
    def delete_collection(self, nombre_coleccion):
        if nombre_coleccion in self.colecciones:
            del self.colecciones[nombre_coleccion]
    
    def get_collection(self, nombre_colecion):
        return self.colecciones.get(nombre_colecion, None)
    
    def __str__(self):
        return f"Base de datos documental con {len(self.colecciones)} col"