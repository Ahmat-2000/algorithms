def transf_en_fct(ch):
    if ch == "+1":
        return lambda x : x + 1
    elif ch == "+2":
        return lambda x : x + 2
    else:
        return lambda x : 2*x

def score_rec(g,d):
    global dico
    if (g,d) not in dico:
        if g == 0 and d ==0:
            res = 0
        elif g == 0:
            res = ope_d[d-1](score_rec(0,d-1))
        elif d == 0:
            res = ope_g[g-1](score_rec(g-1,0))
        else:
            res = max (   ope_d[d-1](score_rec(g,d-1))   ,  ope_g[g-1](score_rec(g-1,d))   )
        dico[(g,d)] = res
    return dico[(g,d)]

nb_tests = int(input())
for _ in range(nb_tests):
    N = int(input())
    entree = input().split(" ")
    p = entree.index("O")
    ope_g=[ transf_en_fct(entree[i]) for i in range(p-1,-1,-1)]
    ope_d=[ transf_en_fct(entree[i]) for i in range(p+1,N)]
    len_g = p
    len_d = N-p-1
    score = [[0 for d in range(len_d+1)] for g in range(len_g+1)]
    dico = {}
    #Remplir la première ligne et la première colonne
    for d in range(len_d):
        score[0][d+1] = ope_d[d](score[0][d])
    for g in range(len_g):
        score[g+1][0] = ope_g[g](score[g][0])
    #Remplir le reste
    for d in range(len_d):
        for g in range(len_g):
            score[g+1][d+1] = max(ope_g[g](score[g][d+1]), ope_d[d](score[g+1][d]))
    #Retrouver le chemin
    g = len_g
    d = len_d
    res = []
    while(g > 0 or d > 0):
        if score[g][d] == ope_g[g-1](score[g-1][d]):
            res.append("G")
            g = g - 1 
        else:
            res.append("D")
            d = d - 1
    res = ''.join(reversed(res))
    print(res)



                
                
            