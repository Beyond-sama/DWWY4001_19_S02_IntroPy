#!/usr/bin/python3
#guardar en la carpeta de proyecto como: usando_persona.py
#del archivo (modulo) persona.py importamos persona
from Persona import Persona

#ahora en el main voy a crear un objeto y voy a llamar al metodo
perrin = Persona("Juan Eduardo Lopez", "12365789-2")
perrin.imprimir()

#en python los atributos son siempre publicos y por eso los puedo modificar
perrin.rut = "19233221-7"
perrin.imprimir()

#sin embargo hay una convencion-> si un atributo parte con _ los programadores python lo tratan como si fuera privado
#perrin._nombre = "juan lopez"-> esto no se hace!
#voy a  crear una persona leyendo desde consola:
nombre = input("ingrese su nombre:")
rut = input("ingrese su rut:")
persona_nueva = Persona(nombre, rut)
persona_nueva.imprimir()