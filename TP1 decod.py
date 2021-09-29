from math import*

def Entropy(listePi) :

    somme = 0

    for i in range(0,len(listePi),1):

        somme = somme + listePi[i] * ( log(listePi[i],2)  )

    return( - somme )



def LAVG(listePi,listeLi) :

    somme = 0

    for i in range(0,len(listePi),1):

        somme = somme + listePi[i] * listeLi[i]

    return( somme )



def Efficiency(listePi,listeLi) :

    monEntropy = Entropy(listePi)
    monLavg =LAVG(listePi,listeLi)
    monEfficiency = monEntropy/monLavg *100

    print("Entropy = ",monEntropy,"bit/symbol")
    print("Lavg = ",monLavg,"bit/symbol")
    print("Efficiency = ",monEfficiency,"%")



#################################################
#                   My task
#################################################

listePi = [0.5,0.3,0.1,0.1]

### Binary Code
print("                   Binary              ")
listeLiBinary = [2,2,2,2]
Efficiency(listePi,listeLiBinary)

"""
### Shannon Mode
print("                 Shannon               ")
listeLiShannon = [1,2,3,4,4]
Efficiency(listePi,listeLiShannon)"""
