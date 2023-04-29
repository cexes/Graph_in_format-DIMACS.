from lista import Lista
from matriz import Matriz
class Main:
  

  origemdestinopeso = []
  with open('arquivo.txt')as files:
    for l in files:
       if l.startswith('p'):
          _, v1,a1 = l.split()
          arestas = (int(v1))
          vertices = (int(a1))
          Lista(vertices)
          Matriz.matriz_adjacencias(vertices,arestas)
       if l.startswith('e'):
          descarte, origem,destino,peso = l.split()
          int(origem)
          int(destino)
          int(peso)
          #print(origem,destino,peso)

