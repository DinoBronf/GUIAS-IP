import math
#Ejercicio 1
#1.1
def imprimir_hola_mundo() -> None:
    print ('Hola Mundo') 
imprimir_hola_mundo ()
imprimir_hola_mundo ()
imprimir_hola_mundo ()

def perimetro() -> float: 
    return 2 * math.pi 

a = perimetro
print (a)
print(perimetro())

def es_multiplo_de(x: int, y: int) -> bool:
    return x % y == 0 
         
def devolver_el_doble_si_es_par(x:int) -> int:
    if x % 2 == 0 :
      return x * 2
    else : 
      return x 

def pares_10_40() -> None:
    x == 10
    while (x != 41):
       if (x % 2 == 0):
         print (x)
         x = x + 1 
       else:
         x = x + 1
#1.2
def imprimir_un_verso() -> None:
   print ('el se canso de hacer canciones de protesta y se vendio a fiorucci')
imprimir_un_verso ()      
#1.3
def raizDe2() -> float:
   return round(math.sqrt (2),4)
#1.4
def factorial_de_dos() -> int:
   return 1*2
#1.5
def perimetro() -> int:
   return math.pi*2
#Ejercicio 2
#2.1
def imprimir_saludo(x) -> None:
    print ('hola ' + x) 
imprimir_saludo ('dino')
#2.2
def raiz_cuadrada_de(x) -> int:
    return math.sqrt(x)
#2.3
def fahrenheit_a_celsius(x:float) -> float:
    return ((x-32)*5/9) 
#2.4
def imprimir_dos_veces(estribillo: str)-> str:
   print (estribillo* 2)
#2.5
def es_multiplo_de2(x:int,y:int) -> bool:
   if x % y == 0:
      return True
   else:
      return False 
#2.6
def es_par(x:int) -> bool:
   if es_multiplo_de2(x,2) == True:
      return True
   else:
      return False
def es_par2(x:int) -> bool:
   return es_multiplo_de2(x,2)
#2.7
def cantidad_de_pizzas(panas,porcionesporpana) -> int:
    if panas*porcionesporpana % 8 == 0:
        return panas*porcionesporpana / 8
    else:
     return cantidad_de_pizzas(panas,(porcionesporpana+1))
#Ejercicio 3
#3.1
def alguno_es_0(x,y) -> bool:
    return x == 0 or y == 0
#3.2
def ambos_son_0(x,y) -> bool:
    return x == 0 and y == 0
#3.3
def es_nombre_largo(nombre:str) -> bool:
    return 3 <= len(nombre) <= 8    
#3.4
def es_bisiesto(año) -> bool:
    return es_multiplo_de(año,400) or es_multiplo_de(año,4) and not es_multiplo_de(año,100)  
#Ejercicio 4
def peso_pino1(alturaencm) -> int:
    if alturaencm <= 3000:
       return 3*sumatoria(3000)
    else:
       return 3*3000 + 2*(alturaencm-3000)   
def peso_pino(altura) -> int:
    peso_primeros_3m = min (altura,3) * 300 
    peso_metros_adicionales = max (altura-3,0) * 200 
    return peso_primeros_3m + peso_metros_adicionales 

def sirve_pino(pinito) -> bool:
    return max (peso_pino(pinito),1000) == 1000 and min(peso_pino(pinito),400) == 400

def es_peso_util(pinito) -> bool:
    return max (pinito,1000) == 1000 and min(pinito,400) == 400
#Ejercicio 5