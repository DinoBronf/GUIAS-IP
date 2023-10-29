import array 
import random
import math
import numpy as np 
#Ejercicio1
#1.1
def pertenece(x,l) -> bool:
    if x in l:
        return True
    else:
        return False
def pertenece2(x,e) -> bool:
    if x in e:
        return True
    else:
        return False
#1.2
def divide_a_todos(x:[int],e:int) -> bool:
   for i in x:
       if i % e != 0:
           return False
       else:
           return True
#1.3
def sumaTotal(s:[int]):
    y = 0
    for i in range(0,len(s)):
        y = y + s[i]
    return y 
#1.4
def ordenados(x:[int]) -> bool:
    for i in range(0,len(x)-1):
        if x[i] > x[i+1]:
            return False
    else:
        return True
#1.5 
def mayor_a_7(palabritas:str)-> bool:
    for i in palabritas:
        if len(i) > 7:
            return True
        else:
            return False
#1.6
def palindromo(text:str)->bool:
    if text == da_vuelta_Str(text):
        return True
    else:
        return False
#1.7
def contraseña(contraseña:str) -> str:
    if len(contraseña) > 8:
        if any(c.islower() for c in contraseña):
            if any(d.isupper() for d in contraseña):
                if any(k.isdigit() for k in contraseña):
                    return "Verde"
    if len(contraseña) < 5:
        return "Rojo"
    else:
        return "Amarillo"
#1.8
def cuentaBancaria(historial:"list[tuple[str,int]]")-> int:
    y = 0
    for tuple in historial:
        if tuple[0] == "R":
            y = y - tuple[1]
        else: 
            y = y + tuple[1]
    return y 
#1.9
def vocales3(palabra) -> bool:
    vocals = "a","e","i","o","u"
    for x in vocals:
        if pertenece(x,palabra):
            for y in [v for v in vocals if v!=x]:  
                if pertenece(y,palabra):
                    for z in [v for v in vocals if v!= x and v!=y]:
                        if pertenece(z,palabra):
                            return True
    else: 
        return False
#Ejercicio 2
#2.1
def ceros_en_paresInOut(lista:list):
    for i in range(len(lista)):
        if i % 2 == 0:
            lista[i] = 0
        else:
            lista[i] = lista[i]  
    else:
        return lista
#2.2
def ceros_en_paresIn(lista:list):
    listaNueva: lista = []
    for i in range(len(lista)):
        if i % 2 == 0:
            listaNueva.append(0)
        else:
            listaNueva.append(lista[i])
    return listaNueva
#2.3
def borrar_vocales(text:str)-> str:
    vocals = ["a","e","i","o","u"]
    vocalsM = ["A","E","I","O","U"]
    textNuevo = ""
    for i in range(len(text)):
        if pertenece(text[i],vocals) or pertenece(text[i],vocalsM):
            textNuevo = textNuevo
        else: 
            textNuevo += text[i]
    return textNuevo
#2.4
def reemplaza_vocales(text:str):
    vocals = ["a","e","i","o","u"]
    vocalsM = ["A","E","I","O","U"]
    textNuevo = ""
    for i in range(len(text)):
        if pertenece(text[i],vocals) or pertenece(text[i],vocalsM):
            textNuevo += "_"
        else:
            textNuevo += text[i]
    return textNuevo
#2.5
def da_vuelta_Str(text:str):
    textNuevo = ""
    for i in range(len(text)):
        textNuevo= text [i] + textNuevo
    return textNuevo
#2.6
def eliminar_repetidos(text:str):
    textNuevo = ""
    for i in range(len(text)):
        if pertenece3(text[i],textNuevo):
            textNuevo = textNuevo
        else:
            textNuevo += text[i]
    return textNuevo

def pertenece3(x,palabra:str) -> bool:
    if x in palabra:
        return True
    else:
        return False
#Ejercicio 3
def problema_aprobado(notas:list)-> int:
    for i in range(len(notas)):
        if notas[i] <4:
         return 3
    if sum(notas)/len(notas) >= 7:
         return 1
    if sum(notas)/len(notas) < 7:
         return 2
    
def sumatoria(x:list)->int:
    suma = 0 
    for i in range(len(x)):
        while i in x:
            suma += x[i]
    return suma 
#Ejercicio 4
#4.1
def lista_estudiantes()-> list:
    lista = []
    nombre = input("Estudiante: ")
    if nombre != "listo":
        lista.append(nombre)
        return lista_estudiantes() + lista
    else:
        return lista
#4.2
def SUBE()-> list:
    historial=[]
    operacion = input("Operación deseada? ") 
    if operacion == "C":
        carga = input("cuanto desea cargar? ")
        historial.append(("C",carga))
        return SUBE() +  historial
    if operacion == "D":
        gasto= input("cuanto sale el viaje? ")
        historial.append(("D",gasto))
        return SUBE() + historial
    if operacion == "X":
        return historial 
#estas no hacian falta pero bueno       
def carga2() -> tuple:
    operacion = input("cuanto desea cargar? ")
    return ("C",operacion)

def gasto2() -> tuple:
    operacion = input("cuanto sale el viaje? ")
    return ("D",operacion)
#4.3
def juego7_y_medio() -> list:
    historial = []
    puntaje = 0  
    mazo = [x for x in range(1,13) if x not in [8,9]]
    while puntaje <= 7.5:
        primeracarta=random.choice(mazo)
        print(f"Carta sacada:{primeracarta}")
        historial.append(primeracarta)
        if primeracarta not in [10,11,12]:
         puntaje += primeracarta 
         print(f"Tu puntaje parcial es de: {puntaje}")
        else:
         puntaje += 0.5
         print(f"Tu puntaje parcial es de: {puntaje}")
        if puntaje == 7.5:
           return "Ganaste broo"
        if puntaje > 7.5:
           print(f"Perdiste bro :(, tu puntaje es de {puntaje} y te salieron las cartas {historial}")
           break 
        SigoOMePlanto = input("Seguis o te plantas cagon? ")
        if SigoOMePlanto == "Sigo":
         if puntaje > 7.5:
          print(f"Perdiste :(, tu puntaje es de {puntaje}")
          break 
        if SigoOMePlanto == "Me planto":
          print(f"Tu puntaje final es de {puntaje} y te salieron las cartas {historial}")
          break 
#Ejercicio 5
#5.1
def pertenece_a_cada_uno(x:int,l:[list]):
    SioNo : l[bool] = []
    for sublista in l:
        if pertenece(x,sublista):
            SioNo.append(True)
        else:
            SioNo.append(False)
    return SioNo
#5.2
def es_Matriz(l:[list])-> bool:
    for sublista1 in l:
        for sublista2 in l:
            if len(sublista1) != len(sublista2):
             return False
    return True
#5.3
def filas_ordenadas(l:[list])->bool:
    if es_Matriz(l):
        for sublista in l:
            if not ordenados(sublista):
                return  False
        return True
#5.4 

             

     


          



