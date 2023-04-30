from bip import Bip
class ListAdj:
 
  def __init__(self,vertices):
     self.vertices = vertices
     self.grafo = [[] for i in range(self.vertices)]
     

  def add_edges(self, origem,destiny,weight):
     self.grafo[origem-1].append([destiny,weight])

  def show_list(self):
     print('A LISTA de adja:')
     for i in range(self.vertices):
        print(f'{i+1}:',end= ' ')
        for j in self.grafo[i]:
           print(f'{j}: ->',end=' ')
        print("\n")
         
  def calc_grau(self,v):
     v-=1
     grau = len(self.grafo[v])
     print("LISTA O grau do vértice:",v+1, "é",grau,"\n")
     
  def bipartite_connected(self):
    print("LISTA É BIPARTIDO: ",Bip.is_bipartite(self.grafo),"\n")   
    print("LISTA É CONEXO :", Bip.is_connected(self.grafo),"\n")   
    
g  = ListAdj(3)

g.add_edges(1,1,1)
g.bipartite_connected()