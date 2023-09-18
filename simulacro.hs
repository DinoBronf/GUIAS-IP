--Ej 1
relacionesValidas :: [(String,String)] -> Bool
relacionesValidas [] = True
relacionesValidas ((x,y):xs) | pertenece (x,y) (xs) = False
                             | pertenece (reverso (x,y)) (xs) = False
                             |otherwise = relacionesValidas xs
reverso:: (String,String) -> (String,String)
reverso (x,y) = (y,x)
pertenece :: (String,String) -> [(String,String)] -> Bool
pertenece xs [] = False
pertenece (l,m) ((x,y):xs) | (l,m) == (x,y) = True
                           | (l,m) == reverso (x,y) = True
                           | otherwise = pertenece (l,m) (xs)
--Ej 2
personas :: [(String,String)] -> [String]
personas  [] = []
personas ((x,y):xs) |pertenece (x,y) xs = personas xs
                    | x == y = [x] ++ personas xs
                    | x /= y = [x,y] ++ personas (xs)  
--Ej 3
amigosDe :: String -> [(String,String)] -> [String]
amigosDe xs [] = []
amigosDe n ((x,y):xs) | n == x = [y] ++ (amigosDe n xs)
                      | n == y = [x] ++ (amigosDe n xs)
                      | n /= x && n /= y = amigosDe n xs
--Ej 4
personaConMasAmigos :: [(String,String)] -> String 
personaConMasAmigos [] = "ninguno"
personaConMasAmigos  ((x,y):(xs))   | (xs) == [] = personaConMasAmigosAux ((x,y):(xs)) 
                                    | personaConMasAmigosAux ((x,y):(xs)) > personaConMasAmigosAux xs = personaConMasAmigos ((x,y):tail(xs))
                                    | personaConMasAmigosAux ((x,y):(xs)) <= personaConMasAmigosAux xs = personaConMasAmigos (xs)
 
personaConMasAmigosAux :: [(String,String)] -> String
personaConMasAmigosAux [] = []
personaConMasAmigosAux ((x,y):xs) | longitud (amigosDe x ((x,y):xs)) >= longitud (amigosDe y ((x,y):xs)) = x  
                                  | longitud (amigosDe x ((x,y):xs)) < longitud (amigosDe y ((x,y):xs)) = y  

longitud :: [String] -> Integer
longitud  [] = 0
longitud (x:xs) = 1 + longitud (xs)  
 