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
   
def es_nombre_largo(nombre:str) -> bool:
    return 3 <= len(nombre) <= 8     
    
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
def cantidad_de_pizzas(x:int,y:int) -> int:
   