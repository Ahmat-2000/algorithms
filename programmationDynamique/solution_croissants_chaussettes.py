T = int(input())

for k in range(T):

    entree = input()

    X,Y,ch = entree.split(" ")
    X = int(X)
    Y = int(Y)


    """c_n désigne le coût minimal du préfixe de ch qui a n lettres
    et tel que ch[n-1] = 'C'. Si c'est impossible que ch[n-1] = 'C' (car c'est égal à 'J')
    alors c_n = +oo
    j_n est défini similairement

    on a la récurrence c_n = min(c_(n-1),j_(n-1) + Y)
    et similairement pour j_n
    """

    cn = 0
    jn = 0

    
    if ch[0] == 'J':
        cn = float("inf")
    if ch[0] == 'C':
        jn = float("inf")

    for i in range(1,len(ch)):

        cn,jn = min(jn+Y,cn),min(cn+X,jn)
        if ch[i] == 'J':
            cn = float("inf")
        if ch[i] == 'C':
            jn = float("inf")


    print(f"{min(cn,jn)}")

