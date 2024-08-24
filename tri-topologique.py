"""
# Type

type graphe = {
    sommets : liste de sommets
    arcs : dictionnaire où la clé est un sommet et la valeur
           est une liste de sommets
}
"""
class TriTopologique :
  def __init__(self,graphe):
    self.sommets, self.voisins = graphe["sommets"], graphe["arcs"]
    self.couleur = {}
    self.fin = {}
    self.initialisation()

  def initialisation(self):
    self.temps = 0
    for s in self.sommets:
      self.couleur[s] = "blanc"
      self.fin[s] = 0
  # version 1 naive utilisation du trie  
  def naiveRecDfs(self, s):
    self.couleur[s] = "gris"
    for v in self.voisins[s]:
      if self.couleur[v] == "blanc" :
        self.naiveRecDfs(v)
    self.couleur[s] = "noir"
    self.temps += 1 
    self.fin[s] = self.temps

  def naiveTriTopologique(self):
    for s in self.sommets :
      if self.couleur[s] == "blanc":
        self.naiveRecDfs(s)

    res = sorted(self.fin.items(), key=lambda item : item[1] , reverse=True)
    return [el[0] for el in res]

  # version 2 améliorée avec pile
  def v2TriTopologique(self):
    pile = []
    def v2RecDfs(s):
      self.couleur[s] = "gris"
      for v in self.voisins[s]:
        if self.couleur[v] == "blanc" :
          v2RecDfs(v)
      self.couleur[s] = "noir"
      pile.append(s)

    self.initialisation()
    for s in self.sommets :
      if self.couleur[s] == "blanc":
        v2RecDfs(s)

    return [ pile[i] for i in range(len(pile) -1 , -1 , -1)]

  # version 3 améliorée avec degré entrant d'un sommet
  """
  Tri topologique, basé cette fois-ci sur le fait qu’un sommet de 
  degré entrant nul peut être placé en tête d’un tri topologique.
  """
  def degreEntrant(self,s):
    d = 0
    for k, v in self.voisins.items() :
      if k != s and s in v :
        d += 1
    return d

  def v3TriTopologique(self):
    file = []
    resultat = []
    degre = {}

    self.initialisation()

    for s in self.sommets :
      degre[s] = self.degreEntrant(s)
      if degre[s] == 0 :
        file.append(s)

    while file : # not empty
      u = file.pop(0)
      resultat.append(u)

      for v in self.voisins[u]:
        degre[v] -= 1
        if degre[v] == 0 :
          file.append(v)
    return resultat



if __name__ == "__main__" :

  graphe = {
    "sommets" : [1,2,3,4,5,6,7,8,9],
    "arcs" : {
      1 : [2,8], # arc (1,2) et (1,8)
      2 : [3,8],
      3 : [6],
      4 : [3,5],
      5 : [6],
      6 : [],
      7 : [],
      8 : [],
      9 : [8]
    }
  }

  triTopologique = TriTopologique(graphe)

  print("# affiche de la version naive ")
  print(triTopologique.naiveTriTopologique())

  print("\n# affiche de la version 2 ")
  print(triTopologique.v2TriTopologique())

  print("\n# affiche de la version 3 ")
  print(triTopologique.v3TriTopologique())
