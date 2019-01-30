"""
    Ejemplo tomado de 
    http://www.pythondiario.com/2018/08/ordenamiento-por-mezcla-merge-sort.html
"""
from archivos.Archivos import *    #Importamos la clase Archivos para utilizar sus metodos
from modelo.modelado import *	#Importamos la clase modelado para utilizar sus metodos
from ordenamiento.combinacion import *	#Importamos los metodos en combinacion para utilizar sus metodos
m = MiArchivo() #Creamos un objeto de tipo MiArchivo
lista = m.obtener_informacion()  #Obtenemos las lineas del archivo 
lista = [l.split(";") for l in lista] #Hacemos un split en cada ;
lista_personas= [] #Iniciamos una lista de objetos vacia para agregar objetos de tipo persona
lista_edades = [] #Iniciamos una lista vacia que recibira unicamente las edades
for d in lista: #Recorremos toda las lineas
	p = Persona(d[0],d[1],d[2]) #Creamos un objeto de tipo Persona enviandole los parametros correspondientes Nombre,Apellido,edad
	lista_personas.append(p) #Agregamos el objeto a la lista
	print (p) #Imprimimos con el metodo __str__ unicamente para corroborar que se agregaron los objetos

for d in lista_personas: #Recorremos la lista de objetos que hemos creado
	lista_edades.append(d.getEdad()) #Agregamos a la lista que contiene las edades el atributo edad obteniendolo de su metodo getEdad()
print(merge_sort(lista_edades)) #Imprimimos la lista ordenada 
