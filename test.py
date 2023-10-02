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
def imprimir_saludo(x:string) -> None:
    print ()