class Matriz:
  
  def __init__(self,vertices):
     self.vertices = vertices
     self.grafo = [[0]*self.vertices for i in range(self.vertices)]
     
  def adiciar_arestas(self,origiem, destino,peso):
     self.grafo[origiem-1][destino -1] = peso
     
     
  def mostrar_matriz(self):
      print('A MATRIZ de adja é')
      for i in range(self.vertices):
        print(i +1,self.grafo[i])      
        
  def calc_grau(self,v):
     v-=1
     grau = len(self.grafo[v])
     print("MATRIZ O grau do vértice:",v+1, "é",grau)
        
