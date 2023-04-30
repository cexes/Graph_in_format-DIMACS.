from lista import ListAdj
from matriz import MatrizAdj

class Main:

   def ReadFile(file_EMACS):
    with open(file_EMACS)as files:
      for l in files:
       if l.startswith('p'):
          _, v1,a1 = l.split()
          vertices = (int(a1))   
          list = ListAdj(vertices) 
          m = MatrizAdj(vertices)
       if l.startswith('e'):
          descarte, origem,destiny,weight = l.split()
          o = int(origem)
          d =int(destiny)
          p =int(weight)
          list.add_edges(o,d,p)
          m.add_edge(o,d,p)
          
      list.show_list()
      list.calc_grau(vertices)
      #list.bipartite_connected()
      m.show_matriz()
      m.calc_grau(vertices)
      m.bipartite_connected()
      
   pass
    
         
   ReadFile("arquivo.txt")
   

          
