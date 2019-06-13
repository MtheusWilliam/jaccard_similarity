import pandas as pd 
import numpy as np
import csv
import math

df = pd.read_csv("dataset_mod2.csv", sep=';')
#print(df)

instances = df.shape[0]
columns = df.shape[1]
#print(instances, columns)

lines = []

#pegando o conjunto de keywords como uma só string de cada artigo e armazenando na lista lines
for i in range(0, instances):
    lines.append(df.loc[i]['author_keywords'])

#pegando o conjunto de keywords em forma de lista de cada artigo e armazenando na lista lines
for i in range(0,instances):
    lines[i] = lines[i].split(',')

#colocando o id de todos os artigos em um vetor
papers_id = []
for i in range(0,instances):
    papers_id.append(df['paper_id'].loc[i])

def compara_strings():
    mat = []
    mat.append('')

    for i in range(0, instances):
        mat.append(papers_id[i]) 

    for w in range(0, instances):
        mat.append(papers_id[w])
        for k in range(0, instances):
            aux = 0
            if lines[w] == lines[k]:#verifica se está comparando um artigo com ele mesmo, caso sim, a célula recebe -1 como valor
                mat.append(-1)
            else:
                for i in range(0, len(lines[w])):
                    for j in range(0, len(lines[k])):
                        if lines[w][i].lower() == lines[k][j].lower():
                            aux = aux + 1 #iteração para representar todas as palavras chaves em comum entre dois artigos, ou seja, a interseção

                #calculando o coeficiente de jaccard fazendo a divisão entre a interseção(aux) 
                # pela soma do tamanho do vetor de palavras chaves dos dois artigos
                #menos a interseção entre eles
                cof_jac = float(aux/( len(lines[w]) + len(lines[k]) - aux))
                #inserindo o coeficiente no vetor mat
                mat.append(cof_jac)

    #transformando o vetor mat em uma matriz n x n onde n é o numero total de artigos do dataset
    mat = np.reshape(mat,(instances+1, instances+1))

    return mat

def write_csv(mat):
    with open('matriz_similaridade_final.csv', 'w', newline='\n') as fp:
        a = csv.writer(fp, delimiter=';')
        a.writerows(mat)

write_csv(compara_strings())