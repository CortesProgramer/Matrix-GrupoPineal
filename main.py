from fastapi import FastAPI

app = FastAPI()

@app.post("/")
def busqueda(words: list[str], matrix: list[list[str]]):
    palabrasEncontradas = []
    palabrasNoEncontradas = []
    for word in words:
        longitud = len(word)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == word[0]:
                    if matrix[i][j:j+longitud] == list(word):
                        palabrasEncontradas.append(word)
                        break
                    if matrix[i][j:j-longitud:-1] == list(word):
                        palabrasEncontradas.append(word)
                        break
                    if (i+longitud) <= len(matrix):
                        counter = 1
                        for k in range(len(word)):
                            if counter < len(word):
                                if matrix[i+k][j] == word[k]:
                                    counter += 1
                            else:
                                palabrasEncontradas.append(word)
                    if i+1 >= longitud:
                        counter = 1
                        for k in range(len(word)):
                            if counter < len(word):
                                if matrix[i-k][j] == word[k]:
                                    counter += 1
                            else:
                                palabrasEncontradas.append(word)

    for palabra in words:
        if palabra not in palabrasEncontradas:
            palabrasNoEncontradas.append(palabra)
    
    return {"encontradas": palabrasEncontradas, "no_encontradas": palabrasNoEncontradas}
