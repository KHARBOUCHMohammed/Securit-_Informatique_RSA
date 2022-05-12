import random
import math
import random
from random import randrange

#From internet
def Premier(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                #print("It is not a prime number")
                return False
                break
        else:
            #print("It is a prime number")
            return True
    else:
        #print("It is not a prime number")
        return False
                
def generationKeys(k):
    p=0
    q=0
    x=k/2
    while (Premier(p)==False ):
        p=random.randrange(1, int(2**x-1))
    while (Premier(q)==False ) and (p!=q):
        q=random.randrange(1, int(2**x-1))
    return p,q

def PGCD(a,b):    
    if (b==0):
        return a
    else:
        return PGCD(b,a%b)

def euclide(a,b):
    r, u, v = a, 1, 0 
    rp, up, vp = b, 0, 1
    while rp != 0:
        q = r // rp
        rs, us, vs = r, u, v
        r, u, v = rp, up, vp
        rp, up, vp = (rs - q * rp), (us - q * up), (vs - q * vp)
    return u % b

def encryption(n, e,msg):
    c=pow(msg,e,n)
    return c
    
def decryption(n,d,msg):
    m=pow(msg,d,n)
    return m



print(" EXO1")
print("********************************************")
k = int(input("Insérer la taille de k : "))
p,q=generationKeys(k)

n=p*q
phi=(p-1)*(q-1)
e=0
while PGCD(e, phi) != 1:
    e = randrange(int(phi / 10), phi)

print("p = ",p)
print("q = ",q)
print ("Phi = ",phi)
print("e= ",e)
d=euclide(e,phi)
kp=(e,n)
kpr=(d,n)
print("La clé public est :",kp)
print("La clé privé est :",kpr)


message = int(input("INSERER LE CHIFFRE :"))
c=encryption(n, e, message)
print('CHIFFREMENT:', c)
m=decryption(n,d,c)
print('DECHIFFREMENT:', m)




print(" EXO2")
print("********************************************")

#From internet
def factors(n):
    F=[]
    i=2
    while n > 1:
        while n % i == 0:
            F.append(i)
            n=n/i
        i = i + 1
    return F[0],F[1]


def decryptionQuestion2():
    n=13289
    p,q=factors(n)
    e=12413
    phi=(p-1)*(q-1)
    d=euclide(e,phi)
    print("Kp(12413,13289)")
    print("Kpr(",d,",",n,")",)
    ListMsg=[9197, 6284, 12836, 8709, 4584, 10239, 11553, 4584, 7008, 12523,
9862, 356, 5356, 1159, 10280, 12523, 7506, 6311]
    print (ListMsg)
    messageDechiffrer=[]
    for i in ListMsg:
        message1=decryption(n,d,i)
        messageDechiffrer.append(message1)
    print("The decrypted key is :",messageDechiffrer)
    
    
def decryptionQuestion2LongNumber():
    n=755918011
    p,q=factors(n)
    e=163119273
    phi=(p-1)*(q-1)
    d=euclide(e,phi)
    print("Kp(12413,13289)")
    print("Kpr",d,",",n,")",)
    ListMsg2=[671828605, 407505023, 288441355, 679172842, 180261802]
    print (ListMsg2)
    messageDechiffrer=[]
    for i in ListMsg2:
        message1=decryption(n,d,i)
        messageDechiffrer.append(message1)
    print("The decrypted key is :",messageDechiffrer)


decryptionQuestion2()
decryptionQuestion2LongNumber()





print(" EXO3")
print("********************************************")



#CHIFFREMENT DU TEXTE
def encryptionOfText(texte,n,e):
    print("******************* Encryption: *************************")
    k=int(math.log(int(n), 40))
    Tab={}
    for i in range (0,k):
        for j in range (0,k):
            Tab[i,j]='a'
    Chiff=[]
    Chiff2=[]
    blockCutting(k,texte,Tab)
    #print("k=",k)
    StrMsg=""
    inst=len(texte)/k
    #print("inst= ",inst)
    if len(texte)%k!=0:
        inst=(len(texte)//k)+1
        #print("inst2= ",inst)

    for i in range(0,int(inst)):
        #print("i=",i)
       # print("ta1=",Tab[0,0])
        x=compteurBlock(Tab,i,k)
        Chiff.append(x)
    #print(Chiff)
    #print("Chiffrement avec la clé pub:")
    var=""
    for i in range(0,len(Chiff)):
        arg=encryption(n,e,Chiff[i])
        #print("message Chiff:",i,"*",arg)
        var=chiffrementToLetter(arg,k,Chiff2,StrMsg)
    #print(var)
    return var
    

def compteurBlock(Tab,ind,k):
    sum=0
    for i in range(0,k):
        sum+=Liste[Tab[ind,i]]*(40**(k-(i+1)))
        print("Tab[ind,i]=",Tab[ind,i],"   POW=",k-(i+1))
    #print ("Somme finale = ",sum)
    return sum

#découpe le texte en bloc
def blockCutting(k,texte,Tab):
    compteur=0
    cp=0
    for i in range(0,len(texte)):
        Tab[cp,compteur]=str(texte[i])
        if compteur>=k-1:
            cp+=1
            compteur=0
        else:
            compteur+=1

def searchForIndex(n):
    for cle,valeur in Liste.items():
        if valeur==n:
            return cle

#permet de passer de chiffre au nombre
def chiffrementToLetter(n,k,T,StrMsg):
    for i in range(k,-1,-1):
        if ((n/pow(40,i)>0) and (n/pow(40,i))<=40):
            num=int(n/pow(40,i))
            Caract=searchForIndex(num)
            n=n-(num*pow(40,i))
            T.append(Caract)

    StrMsg=StrMsg+AffichageMsgChiff(T,StrMsg)
    return StrMsg

def AffichageMsgChiff(T,StrMsg):
    for i in range(len(T)):
        StrMsg=StrMsg+T[i]
    return StrMsg


#DECHIFFREMENT du texte
def decryptionOfText(texte,n,d):
    print("******************* Déchiffrement: *************************")
    k=int(math.log(int(n), 40))+1
    Tab={}
    Chiff=[]
    Chiff2=[]
    blockCutting(k,texte,Tab)
    print("k=",k)
    StrMsg=""
    inst=len(texte)/k
    if len(texte)%k!=0:
        inst=(len(texte)//k)+1
    for i in range(0,int(inst)):
        x=compteurBlock(Tab,i,k)
        Chiff.append(x)
    #print(Chiff)
    print("DéChiffrement avec la clé pub:")
    var=""
    for i in range(0,len(Chiff)):
        arg=decryption(n,d,Chiff[i])
        #print("message Décrypted:",i,"-",arg)
        var=chiffrementToLetter(arg,k-2,Chiff2,StrMsg)
    print("Your decrypted text :",var)

Liste = {'a' : 0, 'b' :1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8,'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20,
        'v': 21,'w': 22, 'x': 23, 'y': 24, 'z': 25, ',' :26, '.': 27 , '?' : 28, '$' : 29, '0' :30 ,'1' :31, '2' :32 , '3': 33, '4': 34, '5': 35, '6': 36,
        '7': 37,'8': 38 ,'9': 39 }


message = input("INSERER LE TEXTE:")
cryptedMsg=encryptionOfText(message,n,e)
print("Your crypted text is :",cryptedMsg)
decryptionOfText(cryptedMsg,n,d)


