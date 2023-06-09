matriz = [
    ['r', 'n', 'e', 'o', 'b', 'd', 'g', 't', 'p', 'o', 'l', 'a', 'b', 'r', 'a', 's'],
    ['c', 'a', 'r', 'r', 'o', 't', 'a', 'n', 'e', 't', 'r', 'e', 't', 'e', 'r', 'r'],
    ['l', 'e', 'o', 'n', 'd', 'e', 'r', 'e', 'l', 'a', 'p', 'o', 't', 'a', 'm', 'o'],
    ['a', 'c', 'a', 'n', 't', 'i', 'l', 'a', 'd', 'o', 's', 'c', 'e', 'l', 'a', 's'],
    ['r', 't', 'p', 'e', 't', 'r', 'o', 'l', 'e', 'r', 'o', 'c', 's', 'a', 'l', 'a'],
    ['a', 's', 't', 'e', 'r', 'o', 'i', 'd', 'e', 's', 'a', 'u', 'e', 'r', 'a', 'a'],
    ['m', 'o', 'n', 'o', 's', 'a', 'l', 'a', 'b', 'o', 'a', 's', 'r', 'r', 'e', 'd'],
    ['t', 'a', 'o', 'a', 'b', 'r', 'a', 's', 'e', 's', 'o', 'c', 'u', 'l', 't', 'a'],
    ['i', 'n', 's', 't', 'r', 'u', 'm', 'e', 'n', 't', 'o', 's', 'o', 't', 'a', 's'],
    ['e', 'r', 'i', 't', 'r', 'e', 'r', 'e', 's', 'i', 'r', 'i', 's', 'a', 'r', 'a'],
    ['r', 'o', 'a', 'a', 'm', 'u', 'n', 'd', 'o', 'o', 'r', 'a', 't', 'o', 'c', 's'],
    ['r', 'r', 'r', 'n', 'l', 'e', 't', 'r', 'a', 's', 'o', 'c', 'a', 't', 'e', 's'],
    ['a', 'r', 'a', 'e', 'g', 'u', 'l', 'a', 'r', 'i', 'd', 'a', 'd', 's', 'e', 'a'],
    ['s', 'a', 'p', 'i', 'e', 'n', 't', 'e', 'r', 'e', 's', 'a', 'l', 'a', 's', 'a'],
    ['a', 'r', 'e', 'n', 'a', 'e', 'l', 'i', 'm', 'i', 'n', 'a', 'c', 'i', 'o', 'n'],
    ['p', 'a', 'l', 'a', 't', 'r', 'a', 's', 'd', 'n', 'a', 'r', 'e', 't', 'i', 'r']
]

palabras = ['bala', 'asteroide', 'soda', 'palabras','pala','tierra', 'mono', 'paraiso', "esternocleidomastoideo", "tigrillo"]

def busqueda(words, matrix):    
    palabrasEncontradas = []
    palabrasNoEncontradas = []
    for word in words: 
        longitud=len(word)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == word[0]:
                    if matrix[i][j:j+longitud] == list(word):
                        print("palabra horizontal: " + str(word))
                        palabrasEncontradas.append(word)
                        break
                    if matrix[i][j:j-longitud:-1] == list(word):
                        print("palabra horizontal invertida: " + str(word))
                        palabrasEncontradas.append(word)
                        break
                    if (i+longitud)<=len(matrix):
                        counter=1
                        for k in range(len(word)):
                            if counter < len(word):
                                if matrix[i+k][j]== word[k]:
                                    counter+=1
                            else:
                                print("Palabra vertical "+str(word))
                                palabrasEncontradas.append(word)
                    if i+1>=longitud: 
                        counter=1
                        for k in range(len(word)):
                            if counter < len(word):
                                if matrix[i-k][j]== word[k]:
                                    counter+=1
                            else:
                                print("Palabra vertical invertida "+str(word))   
                                palabrasEncontradas.append(word)
                                
    for palabra in words:
        if palabra not in palabrasEncontradas:
            palabrasNoEncontradas.append(palabra)
    print("las palabras encontradas fueron: " + str(palabrasEncontradas))
    print("las palabras no encontradas fueron: " + str(palabrasNoEncontradas))
    
busqueda(palabras,matriz)
