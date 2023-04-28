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
          int(origem)
          int(destino)
          int(peso)

          print(origem,destino,peso)

