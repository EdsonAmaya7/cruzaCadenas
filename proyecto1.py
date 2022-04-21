

from random import Random, sample### devuelve una lista de elementos random##

## variables para la matrices ##

max=0
tamaño = 0

# matrices ##
matriz=[]
matrizpadre= []
matrizmadre = []
randompardre= []
randommadre= []
MatrizHijo=[]

lines = 0
size = 1024 * 1024

with open(r"cadenas.txt", "r+") as myfile:
    read_file = myfile.read
    buffer = read_file(size)
    while buffer:
        lines += buffer.count('\n')
        buffer = read_file(size)

if (lines != 0):
    lines += 1

f = open("Alpha.txt", "r")
lineas = f.readlines()
f.close()

def extractDigits(lst):
    return [[el] for el in lst]

lst = lineas
# print(extractDigits(lst))
matriz = extractDigits(lst)
# print(matriz)
# print('lineeeeees',lines)


print("Ingrese el numero de palabras que conformara la matriz :")
colum=int(lines) ## numero de palabras para la matriz

# for a in range(colum):
#     print("Ingrese la cadena de caracteres : ")
#     texto = input("")
#     matriz.append(list(texto)) 
#     print(matriz)

f = open("Alpha.txt", "r")
lineas = f.readlines()
# print('lineas',lineas);
f.close()



## obteniendo la cadena con mas elementos ##
for f in range(colum):
    print(f)
    tamaño = len(matriz[f])
    # tamaño = 40
    min=len(matriz[0])
    # min=45

    if max<=tamaño:
        max= tamaño
    if tamaño<=min:
        min=tamaño

gaps=int(max/2)    

max = max + gaps

#rellena las palabras con gaps
for f in range(colum): 
    matrizpadre.append([]) 
    matrizmadre.append([])
    for g in range(max): 
        if (g<len(matriz[f])):
            matrizpadre[f].append(matriz[f][g])
            matrizmadre[f].append(matriz[f][g])
        else:
            matrizpadre[f].append("-")
            matrizmadre[f].append("-")

#generando posiciones random para los gaps
for f in range(colum):
    randompardre.append([])
    randommadre.append([])
    lista1=sorted(sample(range(0,max-gaps),gaps))
    lista2=sorted(sample(range(0,max-gaps),gaps))
    for g in range(gaps):
        randompardre[f].append(lista1[g])
        randommadre[f].append(lista2[g])
        

## transforma la matriz de random(lista) a matriz de random(int)
for f in range(colum):
    for g in range(gaps):
        randompardre[f][g]=int(randompardre[f][g]) 
        randommadre[f][g]=int(randommadre[f][g])

##insertando gaps aleatorio
for f in range(colum):
    j=len(randompardre[f])-1
    while (j>=0):
        #matriz padre
        k1=len(matrizpadre[f])-1 
        pos1=randompardre[f][j] 
        while (pos1<k1):
            matrizpadre[f][k1]=matrizpadre[f][k1-1]
            k1=k1-1
        matrizpadre[f][k1]="-"
        #matriz madre
        k2=len(matrizmadre[f])-1
        pos2=randommadre[f][j]
        while (pos2<k2): 
            matrizmadre[f][k2]=matrizmadre[f][k2-1]
            k2=k2-1
        matrizmadre[f][k2]="-"
        j=j-1## decrementado la j

##Obteniendo el numero de gaps sobrantes Matriz 1

EGaps = len(matrizpadre[0])-1
for f in range(colum):
    cont = 0
    g =len(matrizpadre[f])-1
    while(g>0):
        if(matrizpadre[f][g]=="-"):
            cont=cont +1
            g=g-1
        else:
            g=0
    if(cont<=EGaps):
        EGaps = cont

##Eliminando los gaps sobrantes Matriz padre
for f in range(colum):
    g = len(matrizpadre[f])-1
    for h in range(EGaps):
        matrizpadre[f].pop(g)
        g = g-1

##Obteniendo el numero de gaps sobrantes Matriz madre

EGaps = len(matrizmadre[0])-1 
for f in range(colum): 
    cont = 0 
    g =len(matrizmadre[f])-1 
    while(g>0): 
        if(matrizmadre[f][g]=="-"): 
            cont=cont +1
            g=g-1 
        else:
            g=0 
    if(cont<=EGaps): 
        EGaps = cont 

##Eliminando los gaps sobrantes Matriz madre
for f in range(colum):
    g = len(matrizmadre[f])-1
    for h in range(EGaps):
        matrizmadre[f].pop(g)
        g = g-1

## pedir numero de cortes
cortes = 0
# while(cortes<2 or cortes>min):
while(cortes<5 ):
    print("\nIngrese el numero de cortes: [2,",min,"]")
    cortes=int(input())
    if(cortes>1 and cortes<=min):
        print("Cortes dentro de rango!!")
    else:
        print("Cortes fuera de rango!!")
        print("Intente de nuevo.")

##Matriz de cortes
numlet = []
resultado = 0
modulo = 0
for i in range(len(matriz)):
    numlet.append([])
    resultado =int(len(matriz[i]) / cortes)
    modulo = len(matriz[i]) % cortes
    numlet[i].append(resultado)
    numlet[i].append(modulo)

##Declarando variables necesarias para matriz hijo
indicador1 = 0
indicador2 = 0
letrasM1 = 0
letrasM2 = 0
turno = False
posicion = 0
j = 0
##Creando la matriz hijo
for i in range(colum):
    print()
    MatrizHijo.append([])
    j = 0
    turno = not turno
    while((j+1)<cortes):
        for k in range(cortes):
            if(k+1<cortes):
                letrasM2 =int(numlet[i][0])
            else:
                letrasM2 = int(numlet[i][0]) + int(numlet[i][1])
            if(turno):
                while(letrasM1<letrasM2):
                    posicion = int(indicador1)
                    MatrizHijo[i].append( matrizpadre[i][posicion])
                    j=j+1
                    if(matrizpadre[i][posicion]!="-"):
                        letrasM1 = letrasM1 + 1
                    indicador1 = indicador1 +1
                letrasM1 = 0
                while(letrasM1<letrasM2):
                    posicion = int(indicador2)
                    if(matrizmadre[i][posicion]!="-"):
                        letrasM1 = letrasM1 + 1
                    indicador2 = indicador2 + 1

                letrasM1 = 0
                MatrizHijo[i].append("|")
                turno = not turno
            else:
                while(letrasM1<letrasM2):
                    posicion = int(indicador2)
                    MatrizHijo[i].append(matrizmadre[i][posicion])
                    j = j + 1
                    if(matrizmadre[i][posicion]!="-"):
                        letrasM1 = letrasM1 +1
                    indicador2 = indicador2 + 1

                letrasM1 = 0
                while(letrasM1<letrasM2):
                    posicion = int(indicador1)
                    if(matrizpadre[i][posicion]!="-"):
                        letrasM1 = letrasM1 + 1
                    indicador1 = indicador1 + 1
                letrasM1 = 0
                MatrizHijo[i].append("|")
                turno = not turno

        indicador1 = 0
        indicador2 = 0

    
#Imprimiendo las matrices
print("Matriz:")
for f in range(colum):### primer forrr cuantas palabras tiene
    print("[",end=' ')
    for c in matriz[f]:## me imprime el numero de letras que tiene la cadena 
        print( c ,end=' ')## y con este imprime lo c y da el espacio
    print("]")


print("Matriz padre :")
for f in range(colum):
    print("[",end=' ')
    for c in matrizpadre[f]:
        print( c ,end=' ')
    print("]")

print("Matriz madre:")
for f in range(colum):
    print("[",end=' ')
    for c in matrizmadre[f]:
        print( c ,end=' ')
    print("]")
    
maximo = 0
for i in range(colum):
        tamaño = len(MatrizHijo[i])
        if(maximo<=tamaño):
            maximo = tamaño

for i in range(colum):
    for j in range(maximo):
        if(j>=len(MatrizHijo[i])):
            MatrizHijo[i].append("-")

##Imprimiendo matriz hijo
print("\nMatriz hijo:")
for i in range(colum):
    print("[", end=" ")
    for j in range(len(MatrizHijo[i])):
        print(MatrizHijo[i][j], end=" ")
    print("]")