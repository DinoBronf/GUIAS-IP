--Ej 1
--1.1
longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud (xs)
--1.2
ultimo :: [t] -> t
ultimo (x:[]) = x
ultimo (x:xs) = ultimo (xs)
--1.3
principio :: [t] -> [t]
principio (x:xs) | longitud (x:xs) == 1 = [] 
                 |  otherwise = x : principio(xs) 
--1.4
reverso :: (Eq t) => [t] -> [t]
reverso (x:xs) | xs == [] = [x]
               | otherwise = reverso xs ++ [x]         
--Ej 2
--2.1
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece e l | longitud l == 0 = False
              | e == head l = True
              | otherwise = pertenece e (tail l)         
--2.2
todosIguales :: (Eq t) => [t] -> Bool
todosIguales (x:xs) | longitud xs == 0 = True
                    | x /= head (xs) = False
                    | otherwise = todosIguales (xs)
--2.3
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos (x:xs) | xs == [] = True
                      | pertenece x xs = False
                      | otherwise = todosDistintos (xs) 
--2.4
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos x | todosDistintos x == True = False
               | otherwise = True 