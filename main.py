from lista import Lista

class Main:
  origemdestinopeso = []
  with open('arquivo.txt')as files:
    for l in files:
       if l.startswith('p'):
          _, v1,a1 = l.split()
          arestas = (int(v1))
          vertices = (int(a1))        
       if l.startswith('e'):
          descarte, origem,destino,peso = l.split()
          o = int(origem)
          d =int(destino)
          p =int(peso)
          lista = Lista(2)
          lista.adiconar_arestas(1,2,3)
          lista.mostrar_lista()