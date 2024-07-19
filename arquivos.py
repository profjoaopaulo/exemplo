import random

#Cria matriz aleatória
def retornaMatriz(l=2, c=2):
    m = []
    for i in range(l):
        linha = []
        for j in range(c):
            if j == c-1:
                linha.append(str(random.randint(0, 9))+"\n")
            else:
                linha.append(str(random.randint(0, 9))+"\t")
        m.append(linha)

    x = ""
    for i in m:
        x += "".join(i)
    return x

#Main
arquivo = open("sabado.txt", "w")
arquivo.write( retornaMatriz(9, 5) )
arquivo.close()
print("Matriz no arquivo!")
