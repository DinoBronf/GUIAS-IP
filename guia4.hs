todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor v w = fst (v) < fst (w) && snd (v) < snd (w)

todoMenor2 :: (Float,Float) -> (Float, Float) -> Bool
todoMenor2 (v1,v2) (w1,w2) = v1 < w1 && v2 < w2 

posPrimerPar :: (Int, Int, Int) -> Int
posPrimerPar (x,y,z)| mod x 2 == 0 = 1
                    | mod y 2 == 0 = 2
                    | mod z 2 == 0 = 3
                    | otherwise = 4
sumarSoloMutliplos :: (Integer,Integer,Integer) -> Integer -> Integer
sumarSoloMutliplos (a,b,c) n = esMultiplo a n + esMultiplo b n + esMultiplo c n
    where
esMultiplo a n|  mod a n == 0 = a
              | otherwise = 0  
--Guia 4

--Ej 1
fibonacci2:: Integer ->Integer
fibonacci2 x | x == 0 = 0
             | x == 1 = 1
             | x > 1 = (fibonacci2 (x-1) + fibonacci2 (x-2))
fibo :: Integer -> Integer
fibo 0 = 0
fibo 1=1
fibo x = fibo (x-1) + fibo (x-2)             
--Ej 2
parteEntera :: Float ->Integer
parteEntera x | x < 0 && x > (-1) = 0
              | x >= 0 && x < 1 = 0
              | x >= 1 = 1 + parteEntera (x-1)
              | otherwise = (-1) + parteEntera (x+1)
--Ej 3
esDivisible :: Integer ->Integer ->Bool
esDivisible  x y| x == 0 = True
                | x < y = False
                | otherwise = esDivisible (x-y) y  
--Ej 4
sumaImpares :: Integer -> Integer
sumaImpares x| x == 0 = 0
             | x == 1 = 1
             | otherwise = sumaImpares (x-1) + 2*x-1          
--Ej 5
medioFact :: Integer -> Integer
medioFact x| x == 0 = 1
           | x == 1 = 1           
--Ej6
sumaDigitos :: Integer -> Integer
sumaDigitos x| x == 0 = 0
             | otherwise = sumaDigitos (div x 10) + mod x 10
--Ej 7
todosDigitosIguales :: Integer ->Bool 
todosDigitosIguales x| x < 10 = True
                     | otherwise = (ultimoDigito x == ultimoDigito (sacarUltimoDigito x)) && todosDigitosIguales (sacarUltimoDigito x)
ultimoDigito :: Integer -> Integer
ultimoDigito x = mod x 10
sacarUltimoDigito :: Integer -> Integer
sacarUltimoDigito x = div x 10  
--Ej 7 manera 2
todosDigitosIguales2 :: Integer -> Bool
todosDigitosIguales2 x | x < 10 = True
                      | mod x 10 == mod ( div x 10) 10 = todosDigitosIguales2 (div x 10)
                      | otherwise = False  
--Ej 8
cantidadDigitos :: Integer -> Integer 
cantidadDigitos x | x < 10 = 1
                  | otherwise = 1 + cantidadDigitos (div x 10)
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito x i |  i == cantidadDigitos x = mod x 10
                 | otherwise = iesimoDigito (div x 10) i 
--Ej 9
invertir :: Integer -> Integer
invertir x | x < 10 = x
           | otherwise = mod x 10 * 10^((cantidadDigitos x)-1) + invertir (div x 10)
esCapicua :: Integer ->Bool
esCapicua x = x == invertir x 
--Ej 10
f1 :: Integer -> Integer
f1 n | n <= 0 = 1
     | otherwise = 2^n + f1 (n-1)
f2 :: Integer -> Integer -> Integer
f2 n q | n <= 1 = q^n
       | otherwise = q^n + f2 (n-1) q
f3 :: Integer -> Integer -> Integer
f3 n q | n <= 1 = q^(2*n)
       | otherwise = q^(2*n) + f3 (n-1) q        
f4 :: Integer -> Float -> Float
f4 n q = f4aux (2*n) n q
f4aux :: Integer -> Integer -> Float -> Float
f4aux n i q | i == n = q^n
            | otherwise = q^(n) + f4aux (n-1) i q        
--Ej 11
eAprox :: Integer -> Float
eAprox n | n == 0 = 1.0
         | otherwise = (1.0 / fromIntegral (factorial n)) + eAprox (n-1)
factorial :: Integer -> Integer
factorial n = product [1,2..n] 
e :: Float
e = eAprox 10
--Ej 12
raizDe2Aproxaux :: Integer -> Float
raizDe2Aproxaux n | n <= 1 = 2
               | otherwise = 2 +  1 / raizDe2Aproxaux (n - 1) 
raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = raizDe2Aproxaux n -1
--Ej 13
sumatoriaM :: Integer -> Integer -> Integer
sumatoriaM m i | m == 1 = i
               | otherwise = i^m + sumatoriaM (m-1) i
sumatoriaN :: Integer -> Integer -> Integer
sumatoriaN j n | n == 0 = 0
               | otherwise = sumatoriaM (j) n + sumatoriaN j (n-1)  
--Ej 14
sumaAux :: Integer -> Integer -> Integer -> Integer
sumaAux x y z | y == 0 && x == 0 = 1
              | x == 0 = z^y + sumaAux x (y-1) z 
              | y == 0 = z^x + sumaAux (x-1) y z 
              | otherwise = z^(x+y) + sumaAux (x-1) y z 
--Ej 15
{-sumaRacionales :: Integer -> Integer -> Float
sumaRacionales x y | x == 0 = 0
                   | y /= 1 = fromIntegral (x) / fromIntegral (y) + sumaRacionales x (y-1)
                   | y == 1 = fromIntegral (x) / fromIntegral (y) + sumaRacionales (x-1) y
                   -}
sumaRacionales2 :: Integer -> Integer -> Float
sumaRacionales2 x y | y == 0 = 0
                    | otherwise = funcionAux2 x y + sumaRacionales2 x (y -1)
funcionAux2 :: Integer -> Integer -> Float
funcionAux2 x y | x== 1 = fromIntegral(x)/fromIntegral(y)
                | otherwise = fromIntegral(x)/ fromIntegral(y) + funcionAux2 (x-1) y                                       
--Ej 16
--a 
menorDivisor :: Int -> Int
menorDivisor x | x == 1 = 1
               | otherwise = encontrarDivisor x 2 
encontrarDivisor :: Int -> Int -> Int
encontrarDivisor x k | mod x k == 0 = k
                     | otherwise = encontrarDivisor x (k + 1)
--b                    
esPrimo :: Int -> Bool
esPrimo x | x == 1 = False
           | menorDivisor x == x = True
           | otherwise = False
--c
sonCoprimos :: Integer ->Integer ->Bool
sonCoprimos m n | m == 1 && n == 1 = False
                | gcd m n == 1 = True 
                | otherwise = False
--d
 {-nEsimoPrimo :: Integer ->Integer
 nEsimoPrimo x | 
 listaDePrimos :: Integer -> [Integer]
 listaDePrimos -}
               
--Ej 17
esFibonacci2 :: Integer -> Bool
esFibonacci2 n = esFibo n 0
esFibo :: Integer -> Integer -> Bool
esFibo x y | x == fibonacci2 y = True
           | fibonacci2 y > x = False
           | otherwise = esFibo x (y+1) 
--Ej 18
mayorDigitoPar :: Integer -> Integer
mayorDigitoPar x | x == 0 = -1
                 | x < 10 && even x = x
                 | parSi (mod x 10) == 8 = mod x 10
                 | otherwise = mayorDigitoPar (div x 10)
parSi:: Integer -> Integer
parSi x | even x = mod x 10  
        | otherwise = parSi (div x 10)
recuentodedigitos :: Integer -> Integer
recuentodedigitos x | x <= 9 = 1 
                    | otherwise = recuentodedigitos (div x 10) + 1 
--Ej 19
esSumaInicialDePrimos :: Int -> Bool
esSumaInicialDePrimos x = sumaDeTantosPrimos1 x 2 
                         
otraMas :: Int -> Int -> Int-> Bool
otraMas m n | m == sumaDeTantosPrimos1 m n = True 
            | otherwise = sumaDeTantosPrimos1 m (n + 1)
            | m /= sumaDeTantosPrimos1 m (n+1) = False

sumaDeTantosPrimos1 :: Int -> Int -> Bool
sumaDeTantosPrimos1 x y | x == sumaDePrimos (y) = True
                        | x /= sumaDePrimos (y) = False

sumaDePrimos :: Int -> Int
sumaDePrimos y | y <= 1 = 0
               | esPrimo y = y + sumaDePrimos (y - 1) 
               | otherwise = sumaDePrimos (y - 1)
