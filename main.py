from lista import Lista

class Main:

   def ReadFile(file_EMACS):
    with open(file_EMACS)as files:
      for l in files:
       if l.startswith('p'):
          _, v1,a1 = l.split()
          vertices = (int(a1))   
          list = Lista(vertices) 
         
       if l.startswith('e'):
          descarte, origem,destino,peso = l.split()
          o = int(origem)
          d =int(destino)
          p =int(peso)
          list.adiconar_arestas(o,d,p)
          
      list.mostrar_lista()
      list.calc_grau(3)
   pass
    
         
   ReadFile("arquivo.txt")
            
       
          
