import array
import math
import random
from queue import LifoQueue as Pila
from queue import Queue as Cola
import os 
import re 
#PARTE 1: ARCHIVOS
#Ejercicio 1
#1.1
#forma 1
def contar_lineas(nombre_archivo:str) -> int:
    abrir = open(nombre_archivo,"r")
    contador : int = 0
    for i in abrir.readlines():
        contador += 1
    abrir.close()
    return contador
#forma 2
def contar_lineas2(nombre_archivo:str) -> int:
    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()
    return len(lineas)
#1.2
def existe_palabra(palabra: str, nombre_archivo: str) -> bool:
    with open(nombre_archivo,"r") as archivo:
        for linea in archivo:
            if palabra in linea:
                return True
    return False
#1.3
def cantidad_apariciones(palabra:str,nombre_archivo:str) -> int:
    contador : int = 0
    with open(nombre_archivo,"r") as archivo:
        for linea in archivo:
            palabras = linea.split()
            if palabra in palabras:
                 contador += 1
        return contador 
#Ejercicio 2
def clonar_sin_comentarios(nombre_archivo:str):
    with open(nombre_archivo,"r") as archivo:
     with open("newFile.txt","w") as archivo2:
         for linea in archivo:
             if not linea.startswith("#"):
                 archivo2.write(linea)
#Ejercicio 3
def reverso(nombre_archivo:str):
    with open(nombre_archivo,"r") as archivo:
      lineas = archivo.readlines()
      with open("Reverso","w") as archivo2:
            for linea in reversed(lineas):
              archivo2.write(linea) 
#Ejercicio 4
def agregar_frase(frase:str, nombre_archivo:str):
    with open(nombre_archivo,"a") as archivo:
        archivo.write(frase)
#Ejercicio 5
"""
def agregar_frase_al_principio(frase:str,nombre_archivo:str):
    with open(nombre_archivo,"r+") as archivo:
     with open("temporal","w") as temporal:
       for linea in archivo:
        temporal.write(linea)
        archivo.truncate(0)
        archivo.write(frase)
    with open(nombre_archivo,"r+") as archivo:
     with open("temporal","r+") as temporal:
      for otraslineas in temporal:
        archivo.write(otraslineas)
      temporal.close()
      archivo.close()
      os.remove("temporal") """
def agregar_frase_al_principio(frase:str,nombre_archivo:str):
    with open(nombre_archivo,"r+") as archivo:
        contenido = archivo.read()
        archivo.seek(0)
        archivo.write(frase)
        archivo.write("\n")
        archivo.write(contenido)
        #DUDA: POR QUE NO QUEDA DOS VECES EL CONTENIDO?
#Ejercicio 6
#Ejercicio 7
notas_csv = "C:\\Users\\dinob\\OneDrive\\Escritorio\\Guia8\\notas.csv"
def promedio_de_alumno(libreta:str)->float:
   notas = []
   with open(notas_csv) as archivo:
       for line in archivo:
           datos = line.split(',')
           if len(datos) == 4:
               LU, Materia, Fecha, Nota = datos 
               if LU.strip() == libreta:
                   notas.append(float(Nota))
   if len(notas) == 0:
       return 0.0
   else: 
       promedio = sum(notas)/len(notas)
       return promedio 
#PARTE 2: PILAS
#Ejercicio 8
def generar_numeros_al_azar(n:int,x:int,y:int)-> Pila:
   p = Pila() 
   i : int = 1
   while i <= n:
    p.put(random.randint(x,y))
    i += 1
   return p.queue 
#Ejercicio 9
def cantidad_elementos(p:Pila) -> int:
    cantidad = 0 
    temp_pila = Pila()
    while not p.empty():
            elemento = p.get()
            temp_pila.put(elemento)
            cantidad += 1
    while not temp_pila.empty():
        p.put(temp_pila.get())
    return cantidad
p1 = Pila()
p1.put(1)
p1.put(2)
p1.put(2)
print(f"la pila tiene {cantidad_elementos(p1)} elementos")
#Ejercicio 10
def buscar_el_maximo(p:Pila) -> int:
    n = max(p.queue)
    return n 
p2= Pila()
p2.put(10)
p2.put(11)
p2.put(15)
p2.put(6)
print(f"el maximo es {buscar_el_maximo(p2)}")
#Ejercicio 11
def esta_bien_balanceada(funcion:str) -> bool:
    p = Pila() 
    for i in range(len(funcion)):
        if funcion[i] == '(':
         p.put(funcion[i])
        if funcion[i] == ')':
            if p.empty():
                return False
            else: p.get()
    if p.empty():
     return True
#Ejercicio 12
def notacion_postfix(expresion) -> int:
    p = Pila()   
    elemento = expresion.split()
    for i in range(len(expresion)):
        if expresion[i].isdigit():
            p.put(expresion[i])
        if expresion[i] == '+':
            suma = p.get() + p.get()
            p.put(suma)
        if expresion[i] == '-':
            resta = p.get() - p.get()
            p.put(resta)
        if expresion[i] == '*':
            multiplicacion = p.get() * p.get()
            p.put(multiplicacion)
        if expresion[i] == '/':
            division = p.get() / p.get()
            p.put(division)
    return sum(p.queue)

        



           
        
       


        