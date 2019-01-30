class Persona: #Creamos la clase Persona 
	def __init__(self, n,a,e): #Creamos el constructor que recibe 4 parametros  
		self.nombre = n #Inicializamos los atributos 
		self.apellido = a
		self.edad = int(e)

	def setNombre(self, n): #Metodo set de Nombre
		self.nombre = n

	def getNombre(self): #Metodo get de nombre
		return self.nombre

	def setApellido(self, n): #Metodo set de Apellido
		self.apellido = n

	def getApellido(self): #Metodo get de Apellido
		return self.apellido

	def setEdad(self, n): #Metodo set de Edad
		self.edad = int(n)

	def getEdad(self): #Metodo get de Edad
		return self.edad

	def __str__(self): #Metodo STR similar a to String
		return "%s-%s-%d"%(self.nombre, self.apellido, self.edad)
