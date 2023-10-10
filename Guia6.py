from ast import Str
import math
from re import X
import re
from tokenize import String
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
       return 3*3000
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
#5.1
def devolver_el_doble_si_es_par(x:int) -> int:
    if x % 2 == 0 :
      return x * 2
    else : 
      return x 
#5.2
def devolver_valor_si_es_par_sino_el_que_sigue(numeringui) -> int:
   if numeringui % 2 == 0:
      return numeringui
   else: 
      return numeringui + 1
#5.3
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(num) -> int:
   if num % 9 == 0:
      return num * 3
   if num % 3 == 0:
      return num * 2
   else:
      return num
#5.4
def lindo_nombre(nombre) -> str:
   if len(nombre) >= 5:
      return 'tu nombre tiene muchas letras!'
   else:
      return 'Tu nombre tiene menos de 5 caracteres'
#5.5
def elRango(num) -> str:
   if num < 5:
      return 'menor a 5'
   if 10 < num < 20:
      return 'entre 10 y 20'
   if num > 20:
      return 'mayor a 20'
   else: 
      return num  
#5.6
def vacaciones_o_laburo(g,edad) -> str:
    if edad >= 65:
       return 'vacacionees'
    if g == 'm' and edad < 65:
       return 'a laburar'
    if g == 'f' and edad >= 60:
       return 'vacacionees' 
    if 18 < edad < 60:
       return 'a laburar'
    if edad <= 18:
       return 'vacacionees'       
#Ejercicio 6
#6.1
def nums_1_al_10() -> None:
   x = 1 
   while (x != 11):
    print(x) 
    x = x +1  
nums_1_al_10()
#6.2
def pares_10_al_40() -> None:
    x = 10
    while (x!=41):
     if (x % 2 == 0):
      print(x)
     x = x + 1
    else:
     x = x + 1
pares_10_al_40()
#6.3 forma 1
def eco() -> str:
   print ('eco ' * 10)
eco()
#6.4
def cuenta_regresiva(x) -> None:
    while (x!=0):
     print (x)
     x = x - 1
    if x == 0:
       return 'Despegue'
#6.5
def viaje_al_pasado(año_de_salida, año_de_llegada) -> None:
    while (año_de_salida != año_de_llegada):
      print (f"Viajo un año al pasado, estamos en el año:{año_de_salida-1}")
      año_de_salida = año_de_salida - 1
    if año_de_salida == año_de_llegada:
       print (f"Viajo un año al pasado, estamos en el año:{año_de_llegada}")
#6.6
def viaje_a_conocer_Aristoteles(año_de_salida) -> None:
    while (-364 < año_de_salida):
       print (f"Viajo un año al pasado, estamos en el año:{año_de_salida-20}")
       año_de_salida = año_de_salida - 20
   