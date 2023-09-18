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
{-personaConMasAmigos :: [(String,String)] -> String
personaConMasAmigos ((x,y):xs) | -}

cuantosRepetidos :: String -> [(String,String)] -> Int
cuantosRepetidos n [] = 0
cuantosRepetidos n ((x,y):xs) | n == x || n == y = 1 + cuantosRepetidos n xs
                              | otherwise = cuantosRepetidos n xs

comparaAmigos :: [(String,String)] -> String
comparaAmigos ((x,y):xs) | cuantosRepetidos x xs > cuantosRepetidos y xs = cuantosRepetidos x tail(xs)
                         | otherwise = y