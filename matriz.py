from bip import Bip
class MatrizAdj:
  
  def __init__(self,vertices):
     self.vertices = vertices
     self.grafo = [[0]*self.vertices for i in range(self.vertices)]
     
  def add_edge(self,origiem, destino,peso):
     self.grafo[origiem-1][destino -1] = peso
     
     
  def show_matriz(self):
      print('A MATRIZ de adja:')
      for i in range(self.vertices):
        
        print(i +1,self.grafo[i],"\n")      
        
  def calc_grau(self,v):
     v-=1
     grau = len(self.grafo[v])
     print("MATRIZ O grau do vértice:",v+1, "é",grau,"\n")
     
  def bipartite_connected(self):
    print("MATRIZ É BIPARTIDO: ",Bip.is_bipartite(self.grafo),"\n")   
    print("MATRIZ É CONEXO :", Bip.is_connected(self.grafo),"\n") 
     

            

