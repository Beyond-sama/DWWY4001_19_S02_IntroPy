#!/usr/bin/python3
#guardar en la carpeta de proyecto como: Persona.py

class Persona:
	""" clase que representa a una persona 
	en chile!
	self-> rol similar al this de java
	el constructor se llama siempre (doble underscore)init(doble underscore)
	todas las operaciones de la clase reciben al self como primer parametro!!!
	"""
	def __init__(self, nombre, rut):
		self.nombre = nombre
		self.rut = rut
	
	#ojo todos los metodos reciben el self como parametro!
	def imprimir(self):
		texto = " ".join(["soy", self.nombre, ", mi rut es", self.rut ])
		print(texto)
		
