import math

def babyStep_giantStep(g, x, p):
    d = p-1 
    m = int(math.ceil(math.sqrt(d))) 
    print("m =", m)
    
    babysteps = {}
    giantsteps = {}

    # Baby steps
    for i in range(m):
        babysteps[i] = (x * pow(g,i,p)) % p
        print("BabyStep nro",i, "xg^(k) =", babysteps[i])

    # Giant steps
    for j in range(m):
        giantsteps[j] = (pow(g,j*m,p)) % p
        print("GiantStep nro",j, "g^(km) =", giantsteps[j]) 
        
    for i in range(m):
        for j in range(m):
            if (giantsteps[i] == babysteps[j]):
                print("En paso nro", i, " de GiantSteps hay colision tal que xg^(k) == g^(km)")
                print("Donde: xg^(j)=",giantsteps[j],"=g^(im) con i =",i, "j =",j, "m =",m)
                logdiscreto = (i*m - j) % d
                break

    print("El logaritmo discreto de x =",x, "es", logdiscreto)

    print("Verificacion: g^(logdiscreto) =", pow(g,logdiscreto,p), "= x")

    return logdiscreto

#g=2
#p=(10**6)+3
#x=28287

babyStep_giantStep(2, 28287, (10**6)+3)
