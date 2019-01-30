import codecs

class MiArchivo:

    def __init__(self):
        self.archivo = codecs.open("data/archivo.txt", "r") #Abre el archivo (ruta,r =read)

    def obtener_informacion(self): #Lee las lineas 
        return self.archivo.readlines()

    def cerrar_archivo(self): 
        self.archivo.close()


class MiArchivoEscribir:

    
    def __init__(self):

        self.archivo = codecs.open("data/demo2.csv", "a") #Que vaya a esta direccon y sino existe lo crea y añade lo que agrego al finla del archivo

    def agregar_informacion(self, p): #Recibe un parametro de tipo persona
        self.archivo.write("%s-%s-%d-%d\n" % (p.nombre, p.apellido,\
                p.edad, p.codigo))

    def cerrar_archivo(self):
        self.archivo.close()
