class Lista:
  def __init__(self,vertices):
     self.vertices = vertices
     self.grafo = [[] for i in range(self.vertices)]
     
    
  def adiconar_aresta(self, u,v,peso):
     self.grafo[u-1].append([v,peso])

  def mostra_lista(self):
     for i in range(self.vertices):
        print(f'{i+1}:',end= ' ')
        for j in self.grafo[i]:
           print(f'{j} ->',end=' ')
        print("")

g = Lista(4)
g.adiconar_aresta(1,2,0)
g.adiconar_aresta(1,4,2)
g.adiconar_aresta(4,1,1)
g.adiconar_aresta(3,2,1)
g.adiconar_aresta(3,2,2)
g.mostra_lista()