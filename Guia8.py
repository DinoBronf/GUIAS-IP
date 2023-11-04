import array
import math
import random
from queue import LifoQueue as Pila
from queue import Queue as Cola
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
    for i in range(len(expresion)):
        if expresion[i].isdigit():
             p.put(expresion[i])
        if expresion[i] == '+':
            operand1 = p.get()
            operand2 = p.get()
            suma = int(operand1) + int(operand2)
            p.put(suma)
        if expresion[i] == '-':
            operand1 = p.get()
            operand2 = p.get()
            resta = int(operand2) - int(operand1)
            p.put(resta)
        if expresion[i] == '*':
            multiplicacion = int(p.get()) * int(p.get())
            p.put(multiplicacion)
        if expresion[i] == '/':
            operand1 = p.get()
            operand2 = p.get()
            division = int(operand2) / int(operand1)
            p.put(division)
    return p.get()
#PARTE 3: COLAS
#Ejercicio 13
def generarCola(n,x,y) -> Cola:
    c = Cola()
    listanums = generar_numeros_al_azar(n,x,y)
    for i in listanums:
        c.put(i)
    return c
#Ejercicio 14
def cantidad_elementos2(c:Cola)-> int:
    contador = 0
    temp_cola = Cola()
    while not c.empty():
        elemento = c.get()
        temp_cola.put(elemento)
        contador +=1 
    while not temp_cola.empty():
        elemento1 = temp_cola.get()
        c.put(elemento1)
    return contador
c1 = Cola()   
c1.put(2)
c1.put(3)
print(cantidad_elementos2(c1))
#Ejercicio 15
def buscar_max(c:Cola)-> int:
    lista = []
    cola_temp = Cola()
    i = 0
    while not c.empty():
     lista.append(c.get())
     cola_temp.put(lista[i])
     i += 1
    while not cola_temp.empty():
        elemento = cola_temp.get()
        c.put(elemento) 
    return max(lista)
c1 = Cola()   
c1.put(2)
c1.put(3)
print(f"el maximo es {buscar_max(c1)}")
#Ejercicio 16
def armar_secuencia_de_bingo()-> Cola:
    Bingo = Cola()
    lista = []
    i = 0
    while i != 99:
       n = random.randint(0,99)
       if not pertenece(n,lista):
        lista.append(n)
        i += 1
    for elemento in lista:
        Bingo.put(elemento)
    return Bingo
def pertenece(x,l) -> bool:
    if x in l:
        return True
    else:
        return False
#No es tipo in 
def jugar_carton_de_bingo(Carton:list,Bolillero:Cola) -> int:
    Jugadas = 0
    while not Carton == []:
      bolilla = Bolillero.pop(0)
      if bolilla in Carton:
          Carton.remove(bolilla)
      Jugadas += 1
    return Jugadas   
carton = [5,10,15,20,25,30,35,40,45,50,55,60]
bolillero = list(range(0, 99))
random.shuffle(bolillero)
print(jugar_carton_de_bingo(carton,bolillero))
#Ejercicio 17
def n_pacientes_urgentes(c:Cola)-> int:
    n = 0
    while not c.empty():
        elemento = c.get()
        urgencia = elemento[0]
        if urgencia < 4:
            n += 1
        else:
            n = n
    return n  
Cola1 = Cola()
Cola1.put((1,"L","R"))
Cola1.put((2,"M","R"))
print(n_pacientes_urgentes(Cola1))
#Ejercicio 18
def pertenece_colas(l,c:Cola) -> bool:
    lista = []
    while not c.empty():
     elemento = c.get()
     lista.append(elemento)
    if l in lista:
        return True
    else:
      return  False 
def eliminar_repetidos(c:Cola) -> Cola:
    colita = Cola()
    while not c.empty():
        elemento = c.get()
        if not pertenece_colas(elemento,colita):
            colita.put(elemento)
        else:
            colita = colita
    return colita 

def a_clientes(c:Cola)-> Cola:
    orden = Cola()
    restaura = Cola()
    cola_temp1 = Cola() 
    while not c.empty():
        info = c.get()
        prioridad = info[3]
        preferencia = info[2]
        if prioridad == True:
            orden.put(info)
            restaura.put(info)
        elif preferencia == True:
            orden.put(info)
            restaura.put(info)
        else:
            restaura.put(info)
            cola_temp1.put(info)
    while not cola_temp1.empty():
     elemento = cola_temp1.get()
     orden.put(elemento)
    c.put(eliminar_repetidos(restaura))
    return orden.queue
cola_ingreso = Cola()
cola_ingreso.put(("Juan Perez", 12345678, False, True))
cola_ingreso.put(("Maria Rodriguez", 98765432, True, False))
cola_ingreso.put(("Luis González", 55555555, True, False))
cola_ingreso.put(("Ana López", 11111111, False, False))    
print(a_clientes(cola_ingreso))

#PARTE 4: DICCIONARIOS
#Ejercicio 19
def agrupar_palabras(nombre_archivo:str) -> dict:
    with open(nombre_archivo,"r") as archivo:
        dict = {}
        for linea in archivo:
         palabras = linea.split()
         for i in range(len(palabras)):
             if len(palabras[i]) in dict:
               dict[(len(palabras[i]))] += 1
             else:
                 dict[((len(palabras[i])))] = 1
    return dict
#Ejercicio 20
notas_csv = "C:\\Users\\dinob\\OneDrive\\Escritorio\\Guia8\\notas.csv"
def promedio_de_todos()-> dict:
    dict = {}
    with open(notas_csv,"r") as archivo:
        for line in archivo:
            datos = line.split(',')
            LU, Materia, Fecha, Notas = datos
            LU = LU.strip()
            if len(LU) > 2:
             dict[LU]=promedio_de_alumno(LU)
    return dict
#Ejercicio 21
def la_palabra_mas_frecuente(nombre_archivo:str) -> str:
    with open(nombre_archivo,"r") as archivo:
        dict = Cuantas_veces_esta_cada_una(nombre_archivo)
    return max(dict,key=dict.get)

def Cuantas_veces_esta_cada_una(nombre_archivo:str)-> dict:
    with open(nombre_archivo,"r") as archivo:
        dict = {}
        for linea in archivo:
            palabras = linea.split()
            for i in range(len(palabras)):
                if palabras[i] in dict:
                    dict[palabras[i]] += 1
                else:
                    dict[palabras[i]] = 1
    return dict 
#Ejercicio 22
historiales = {}
ultimo_sitio = []
def visitar_sitio(historiales:dict,usuario:str,sitio:str):
    historial = Pila()
    if usuario not in historiales:
        p = historial
        p.put(sitio)
        historiales[usuario] = historial
    else:
      p = historial
      p.put(sitio)
      historiales[usuario] = historial
def navegar_atras(historiales,usuario:str):
    if usuario in historiales:
       historial = historiales[usuario] 
       sitio_anterior = (historial.get())
       ultimo_sitio.append(sitio_anterior)
def navegar_adelante(historiales,usuario:str):
    if usuario in historiales:
        historial = historiales[usuario]
        sitio_siguiente = ultimo_sitio.pop()
        historial.put(sitio_siguiente) 

historiales = {}
visitar_sitio(historiales, "Usuario1", "google.com")
visitar_sitio(historiales, "Usuario1", "facebook.com")
navegar_atras(historiales, "Usuario1")
visitar_sitio(historiales, "Usuario2", "youtube.com")
navegar_adelante(historiales, "Usuario1")
print(historiales)
#Ejercicio 23
inventario = {}
nombre_precio_cantidad = {}
def agregar_producto(inventario,nombre,precio,cantidad):
    if not nombre in inventario:
        inventario[nombre] = {"precio": precio,"cantidad":cantidad}
def actualizar_stock(inventario,nombre,cantidad):
    if nombre in inventario:
        inventario[nombre]["cantidad"] = cantidad
def actualizar_precios(inventario,nombre,precio):
    if nombre in inventario:
        inventario[nombre]["precio"] = precio
def calcular_valor_inventario(inventario)-> int:
    valor = 0
    for nombre in inventario:
      info = inventario[nombre]
      valor +=  info["precio"] * info["cantidad"]
    return valor 
inventario = {}
agregar_producto(inventario, "Camisa", 20.0, 50)
agregar_producto(inventario, "Pantal´on", 30.0, 30)
actualizar_stock(inventario, "Camisa", 10)
valor_total = calcular_valor_inventario(inventario) 
print(valor_total)

#Simulacro
#Ejercicio 1
def ultima_aparición(s:list,e:int) -> int:
    apariciones = []
    for i in range(len(s)):
        if s[i] == e:
            apariciones.append(i)
    return max(apariciones)
#Ejercicio 2
def elementos_exclusivos(s:list,t:list) -> list:
    exclusivo = []
    for i in range(len(s)):
     if s[i] not in t:
          if s[i] not in exclusivo:
           exclusivo.append(s[i])
    for q in range(len(t)):
        if t[q] not in s:
            if t[q] not in exclusivo:
                exclusivo.append(t[q])
    return exclusivo
#Ejercicio 3
def contar_traducciones_iguales(ingles:dict,aleman:dict) -> int:
    contador = 0
    for key,value in ingles.items():
        for key1,value1 in aleman.items():
            if key == key1 and value == value1:
                contador += 1
    return contador 
print(contar_traducciones_iguales({"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"},{"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}))
#Ejercicio 4
def convertir_a_diccionario(l:list)->dict:
    dict = {}
    for i in range(len(l)):
        if l[i] in dict:
            dict[l[i]] += 1
        else:
            dict[l[i]] = 1
    return dict 
print(convertir_a_diccionario([-1,0,4,100,100,-1,-1]))

           
        
       


        