--Ej 1
--1.1
longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud (xs)  
--1.2
ultimo :: [t] -> t
ultimo (x:[]) = x
ultimo (x:xs) = ultimo xs  
--1.3
principio :: [t] -> [t] 
principio (x:xs) | longitud (x:xs) == 1 = []
                 | otherwise = x : principio xs
--1.4
reverso :: [t] -> [t] 
reverso (x:xs) | longitud (x:xs) == 1 = (x:xs)
               | otherwise = reverso xs ++ [x]
--Ej 2
--2.1
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece e (x:xs) | e == head (x:xs) = True
                   | longitud (x:xs) == 1 = False 
                   | e /= head (x:xs) = pertenece e (xs)
--2.2
todosIguales :: (Eq t) => [t] -> Bool
todosIguales (x:xs) | (x:xs) == [] = False
                    | longitud (x:xs) == 1 = True
                    | head (x:xs) == head (xs) = todosIguales (xs)
                    | otherwise = False
--2.3
todosDistintos :: (Eq t) => [t] -> Bool 
todosDistintos (x:xs) | longitud (x:xs) == 1 = True
                      | pertenece (head (x:xs)) (xs) = False
                      | otherwise = todosDistintos (xs)
--2.4
hayRepetidos :: (Eq t) => [t] -> Bool 
hayRepetidos (x:xs) | longitud (x:xs) == 1 = False
                    | pertenece (head (x:xs)) (xs) = True
                    | otherwise = hayRepetidos xs
--2.5
quitar :: (Eq t) => t -> [t] -> [t]
quitar e (x:xs) | e == head (x:xs) = xs 
                | e /= head (x:xs) = x : quitar e (xs)   
--2.6 
quitarTodos :: (Eq t ) => t -> [t] -> [t]
quitarTodos x [] = []
quitarTodos e (x:xs) | e == head (x:xs) = quitarTodos e xs 
                     | otherwise = head (x:xs) : quitarTodos e xs 
--2.7
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos (x:xs) | xs == [] = [] 
                         | pertenece x xs = [x] ++ quitarTodos x (eliminarRepetidos xs)
                         | otherwise = [x] ++ eliminarRepetidos xs 
--2.8
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos (x:xs) (y:ys) | xs == [] = True
                              | noPertenece x (y:ys) = False 
                              | otherwise = mismosElementos xs (y:ys)  
noPertenece :: (Eq t) => t -> [t] -> Bool
noPertenece x [] = True
noPertenece e (x:xs) | e == x = False 
                     | e /= x = noPertenece e xs 
--2.9
capicua :: (Eq t) => [t] -> Bool 
capicua (x:xs) | xs == [] = True
               | reverso (x:xs) == (x:xs) = True 
               | otherwise = False
--Ej 3
--3.1
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs
--3.2
productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = x * productoria xs
--3.3
maximo :: [Integer] -> Integer
maximo (x:xs) | longitud (x:xs) == 1 = x
              | x >= head (xs) = maximo (x:tail(xs))
              | x <= head (xs) = maximo xs 
--3.4
sumarN :: Integer -> [Integer] -> [Integer]
sumarN n (x:xs) | longitud (x:xs)== 1 = [x + n] ++ xs  
                | otherwise = [x + n] ++ sumarN n xs
--3.5 si el primero no se sumaba a si mismo
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (x:xs) | longitud (x:xs) == 1 = (x:xs)
                      | otherwise = [x] ++ sumarN x xs
--3.5 el primero sumandose a si mismo
sumarElPrimero2 :: [Integer] -> [Integer]
sumarElPrimero2 (x:xs) = sumarN x (x:xs)
--3.6
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo (x:xs) | longitud (x:xs) == 1 = (x:xs)
                     | otherwise = sumarN (head (reverso (x:xs))) (x:xs)  
--3.7
pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | even x = [x] ++ pares xs
             | otherwise = pares xs 
--3.8
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN n [] = []
multiplosDeN n (x:xs) | esMultiplo x n  = [x] ++ multiplosDeN n xs 
                      | otherwise = multiplosDeN n xs
    where
esMultiplo a n |  mod a n == 0 = True
               | otherwise = False 
--3.9 en orden decreciente
ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar (x:xs) | maximo (x:xs) == x = [x] ++ ordenar xs
               | otherwise = ordenar (xs ++ [x])
--3.9 en orden creciente
ordenar2 :: [Integer] -> [Integer]
ordenar2 [] = []
ordenar2 (x:xs) | maximo (x:xs) == x = ordenar2 xs ++ [x]
                | otherwise = ordenar2 (xs ++ [x])     
--Ej 4
--4.1
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos (x:xs) | longitud (x:xs) == 1 = (x:xs)
                             | x == ' ' && head (tail (x:xs)) == ' ' = [head(xs)] ++ sacarBlancosRepetidos xs
                             | otherwise = [x] ++ sacarBlancosRepetidos xs
--4.2
contarPalabras :: [Char] -> Integer
contarPalabras [] = 0
contarPalabras (x:xs) | longitud (x:xs) == 0 = 0
                      | longitud (x:xs) == 1 && x /= ' ' = 1
                      | longitud (x:xs) == 1 && x == ' ' = 0
                      | x /= ' ' && head xs /= ' ' = contarPalabras xs 
                      | x /= ' ' && head xs == ' ' = contarPalabras xs
                      | x == ' ' = 1 + contarPalabras xs 
--4.3
palabras :: [Char] -> [[Char]]
palabras x = extraerPalabras x []

extraerPalabras :: [Char] -> [Char] -> [[Char]]
extraerPalabras [] [] = []
extraerPalabras [] l = [l]
extraerPalabras (x:xs) [] | x == ' ' = extraerPalabras xs []
extraerPalabras (x:xs) l  | x == ' ' = l : extraerPalabras xs []
                          | otherwise = extraerPalabras xs (l ++ [x])  
--4.4
{-palabraMasLarga :: [Char] -> [Char]
palabraMasLarga [] = []
palabraMasLarga (x:xs) | head(xs) == ' ' = longitud (palabras x) >= longitud (palabras head(tail(xs))) == palabras x
                       | otherwise = longitud (palabras xs) -}
--4.5
aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (x:xs) = x ++ aplanar xs     
--4.6
aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [] = []
aplanarConBlancos (x:xs) = x ++ [' '] ++ aplanar xs
--4.7
aplanarConNBlancos :: [[Char]] -> Integer -> [Char]
aplanarConNBlancos [] n = []
aplanarConNBlancos (x:xs) n = x ++ nBlancos n ++ aplanarConNBlancos xs n
nBlancos :: Integer -> [Char]
nBlancos 0 = []
nBlancos n = ' ' : nBlancos (n-1)
--Ej 5
--5.1 
{-
sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada  [] = []
sumaAcumulada (x:xs) = x : sumaAcumulada (sumatoria2 x head(xs))

sumatoria2 :: t -> t -> t
sumatoria2 x y = x + y
-}
--5.2
descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) | esPrimo x = [x] : descomponerEnPrimos xs
                           | otherwise = completa x 2 : descomponerEnPrimos xs 
                          
completa :: Integer -> Integer  -> [(Integer)]
completa x y | (menorDivisor x) * y == x = [(menorDivisor x), (y)]
             | otherwise = completa x (y + 1) 
                         
esPrimo :: Integer -> Bool
esPrimo x | x == 1 = False
          | menorDivisor x == x = True
          | otherwise = False
menorDivisor :: Integer -> Integer
menorDivisor x | x == 1 = 1
               | mod x 2 == 0 = 2
               | otherwise = encontrarDivisor x 2
encontrarDivisor :: Integer -> Integer -> Integer
encontrarDivisor x k | mod x k == 0 = k
                     | otherwise = encontrarDivisor x (k+1)

 