G = { 'depart' : {'A'},
      'A' : {'B'},
      'B' : {'C','D'},
      'C' : {'arrivee','A','D'},
      'D' : {'depart','A'},
      'arrivee' : {} }


def en_matrice_adjacence(G):
    M = {}
    for depart in G:
        M[depart] = {}
        for arrivee in G:
            if arrivee in G[depart]:
                M[depart][arrivee] = 1
            else:
                M[depart][arrivee] = 0
    return M

A = en_matrice_adjacence(G)

def multiplication_matricielle(M,N):
    res = {}
    for i in M:
        res[i] = {}
        for j in M:
            res[i][j] = 0
            for k in M:
                res[i][j] = (res[i][j] + M[i][k]*N[k][j])
    return res


def nombre_chemins(n,A=A,depart='depart',arrivee='arrivee'):
    An = A
    for _ in range(n-1):
        An = multiplication_matricielle(A,An)
    return An[depart][arrivee]

def nombre_chemins2(n,A=A,depart='depart',arrivee='arrivee'):
    An = expo_rapide(A,n,multiplication_matricielle)
    return An[depart][arrivee]



def debile(n):
    res = 1
    for _ in range(n):
        res = (res*13) % 10000
    return res

def expo_recursif(n):
    if n == 0:
        return 1
    if n == 1:
        return 13
    x = expo_recursif(n//2)
    x = (x*x) % 10000
    if n % 2 != 0:
        x = (x*13) % 10000
    return x


def expo_rapide(x,n,multiplication = lambda s,t : s*t % 10000):
    b = bin(n)
    res = x
    for i in range(3,len(b)):
        if b[i] == '0':
            res = multiplication(res,res)
        else:
            res = multiplication(multiplication(res,x),res)
    return res
        


def vaches(n):
    G = {'s':{'s','u'},'t':{'s'},'u':{'t'}}
    A = en_matrice_adjacence(G)
    return expo_rapide(A,n,multiplication_matricielle)['s']['s']


def vaches_molles(n):
    vn,vnm1,vnm2 = 1,1,1
    for i in range(2,n):
        vn,vnm1,vnm2 = vn+vnm2,vn,vnm1
    return vn




































import time
import matplotlib.pyplot as plt
def test(liste_fonctions,inst):
    temps_execution = []
    for fct in liste_fonctions:
        t = time.time()
        fct(inst)
        temps_execution.append(time.time()-t)
    return temps_execution

def trace_courbes(liste_fonctions,debut,fin):
    X = []
    Y = [ [] for j in range(len(liste_fonctions)) ]
    for i in range(debut,fin,max((fin-debut)//100,1)):
        plt.clf()
        X.append(i)
        instance = i #ligne à changer ici
        TE = test(liste_fonctions,instance)
        for j in range(len(TE)):
            Y[j].append(TE[j])
            plt.plot(X,Y[j])

        plt.draw()
        plt.pause(0.001)

