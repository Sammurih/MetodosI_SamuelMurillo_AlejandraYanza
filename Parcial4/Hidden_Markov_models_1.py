import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

Prior=np.array([0.2,0.8])

T = np.array([[0.8,0.2],
              [0.2,0.8]])
E = np.array([[0.5,0.9],
              [0.5,0.1]])
DictHiddenS = {0:'Justa (J)',1:'Sesgada (B)'}
DictObs = {0:'Cara (C)',1:'Sello (S)'}
#States: [J, B]
States = np.array([0,1])
#Obs: [S, C, C, C, S, C, S, C]
Obs=np.array([1,0,0,0,1,0,1,0])

def GetStates(States,N):
    
    CStates = list( combinations_with_replacement(States,N) )
    
    #print(CStates)
    
    Permu = []
    
    for it in CStates:
        p = list(permutations(it,N))
       # print(p)
        
        for i in p:
            if i not in Permu:
                Permu.append(i)
                
    return np.array(Permu)

HiddenStates = GetStates(States,8)
#print(HiddenStates,len(HiddenStates))

def GetProb(T,E,Obs,State,Prior):
    
    n = len(Obs)
    p = 1.
    
    p *= Prior[State[0]]
    
    # Matriz de transicion
    for i in range(n-1):
        p *= T[ State[i+1], State[i]  ]
        
    for i in range(n):
        p *= E[ Obs[i], State[i] ]
        
    return p
P = np.zeros(HiddenStates.shape[0], dtype=np.float64)
for i in range(P.shape[0]):
    P[i] = GetProb(T,E,Obs,HiddenStates[i],Prior)
    
#print(P)

plt.plot(P,label="Probabilidad por secuencia")
plt.legend()
plt.show()

ii = np.where( P == np.amax(P))
print(HiddenStates[ii]) #Stado Oculto más probable
print(np.round((P[ii]),4)) #Probabilidad correspondiente

print(np.sum(P)) #Probabilidad Total del estado observado [S, C, C, C, S, C, S, C]

ObsStates = GetStates([0,1],8)

Nobs = ObsStates.shape[0]

PObs = np.zeros(Nobs)

for j in range(Nobs):
    
    dim = HiddenStates.shape[0]
    P = np.zeros(dim)
    
    for i in range(dim):
        P[i] = GetProb(T,E,ObsStates[j],HiddenStates[i],Prior)
        
    PObs[j] = np.sum(P)

plt.plot(PObs,label="Probabilidad por estado observado")
plt.legend()
plt.show()

ii = np.where( PObs == np.amax(PObs))
print(ObsStates[ii]) #Estado Observado más probable
print(PObs[ii]) #Probabilidad Total del Estado Observado Más Probable
print(np.round(np.sum(PObs),4)) #En efecto la suma de todos los estados es 1.0