class Lista:
 
  def __init__(self,vertices):
     self.vertices = vertices
     self.grafo = [[] for i in range(self.vertices)]
     

  def adiconar_arestas(self, u,destino,peso):
     self.grafo[u-1].append([destino,peso])

  def mostrar_lista(self):
     for i in range(self.vertices):
        print(f'{i+1}:',end= ' ')
        for j in self.grafo[i]:
           print(f'{j}: ->',end=' ')
        print("")
         
  def calc_grau(self,v):
     v-=1
     grau = len(self.grafo[v])
     print("O grau do vértice:",v+1, "é",grau)