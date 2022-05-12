import random
import numpy as np
from math import floor, log
from random import randrange




print("----------------------------------------- Parite 1  ------------------------------------------")


#Calcul du le Plus Grand Diviseur Commun' entre les 2 nombres entiers a et b
def pgcd(a, b): 
    if(b == 0): 
        return a 
    else: 
        return pgcd(b, a % b) 
         
#print("le plus grand diviseur en commun est :", pgcd(60,48)) 




#Test de primalité
def primalite(n):
    """ retourne True si n est premier, False dans le cas contraire """

    if n == 1 or n == 2:
        return True

    if n % 2 == 0:
        return False

    x = n ** 0.5

    if x == int(x):
        return False

    for y in range(3, int(x), 2):

        if n % y == 0:
            return False

    return True


#Generation des nombres premiers aleatoires
def generationNumAlea():
    k = int(input("merci de bien saisir le K: ")) 
    """Retourne p et q deux nombres premiers """
    p = 0
    q = 0
   

    x = k//2
    y = 2**x

    while primalite(p) is False:
        p = int(random.randrange(1,y))
        
    while primalite(q) is False:
        q = int(random.randrange(1,y))
        
   

    print("p est :",p)
    print("q est ",q)
    return p , q


#L'algorithme d'euclide étendu
def euclide(a,b):
   
    r = a
    u = 1
    v = 0
    rp = b
    up = 0
    vp = 1

    while rp != 0:
        q = r // rp
        rs = r
        us = u
        vs = v

        r = rp
        u = up
        v = vp
        
        rp = rs - q * rp
        up = us - q * up 
        vp = vs - q * vp

    return u % b


#L'exponentiation modulaire
def modulo(x, y, n):
    """Retourne (x**y) % m"""
    r = 1
    while y > 0:
        if y & 1 == 1: 
            r = (r * x) % n
        y = y >> 1  
        x = (x * x) % n
    return r



#Génération de la clé publique et privée
def cles():

     
    p,q=generationNumAlea()

    #calcul de n
    n = p * q

    #calcul phi
    phi=(p-1)*(q-1)

    e=0
    #generer un nombre e (clé publique) tels que pgcd(e,phi) = 1
    while pgcd(e,phi)!=1 :
        e = randrange(phi)

    #calcul d la clé privée
    d=euclide(e,phi)

    publicKey = (e,n)
    privateKey = (d,n)

    print("La clé publique: (",e,n,")")
    print()
   
    print("La clé privée est : (",d, n,")")
    return publicKey, privateKey
    print()





#Chiffrement
def encrypt(m,e,n):
    c = modulo(m, e, n)
    return c


#Déchiffrement
def decrypt(c,d,n):
    m = modulo(c, d, n)
    return m
    c = encrypt(message, e, n)





   
def testEncryptDecrypt():
    
    #generation des clés
    public, private = cles()
    message = int(input("Veillez entrer un message(Nombre) à chiffrer : "))
    print()
    e = public[0]
    n = public[1]
    d = private[0]

    
    while message >= n:
        message = int(input("Le message ne doit pas être suppérieur à n : "))
        print("n est :", n)
    print()

    #chiffrement
    print("----------------------------------------- chiffrement ------------------------------------------")
    c = encrypt(message, e, n)
    print("Le message chiffré est : ",c)
    print()
    print("----------------------------------------- Déchiffrement ------------------------------------------")
    #déchiffrement
    message = decrypt(c,d,n)
    print("Le message dechiffrer est : ",message)
    print()






    print("########################################## Partie 2 ###########################################")



def factoring(n):
    """factoring(n): décomposition d'un nombre entier n en facteurs premiers"""
    F = []
    if n == 1:
        return F
    # recherche de tous les facteurs 2 s'il y en a
    while n >= 2:
        x, r = divmod(n, 2)
        if r != 0:
            break
        F.append(2)
        n = x
    # recherche des facteurs 1er >2
    i = 3
    rn = np.sqrt(n) + 1
    while i <= n:
        if i > rn:
            F.append(n)
            break
        x, r = divmod(n, i)
        if r == 0:
            F.append(i)
            n = x
            rn = np.sqrt(n) + 1
        else:
            i += 2
    return F



def decryptMsg1():
    print("----------------------------------------- Déchiffrement du message 1 ------------------------------------------")
    print("La clé publique : (12413 ; 13289)")
    n=13289
    e=12413

    
    p,q=factoring(n)
  
    phi=(p-1)*(q-1)
   
    d=euclide(e,phi)

    print("La clé privée : (",d," ; ",n,")",)

    msg=[9197, 6284, 12836, 8709, 4584, 10239, 11553, 4584, 7008, 12523, 9862, 356,5356, 1159, 10280, 12523, 7506, 6311]
    print("Le message à déchiffrer:", msg)
    messageDecrypt=[]
    #parcourir le tab de message
    for element in msg:
        #dechiffrer chaque élément
        message1=decrypt(element,d,n)
        #ajout de message déchiffré au tab messageDechiffrer
        messageDecrypt.append(message1)

    print("Le message déchiffré :",messageDecrypt)
    print()





def decryptMsg2():
    print("------------------------------- Déchiffrement du message 2 ----------------------------------------------")
    print("La clé publique : (163119273;755918011)")
    n=755918011
    e=163119273
   
    p,q=factoring(n)
    phi=(p-1)*(q-1)


    d=euclide(e,phi)

    print("La clé privée : (", d, " ; ", n, ")", )

    msg2=[671828605, 407505023, 288441355, 679172842, 180261802]
    print("Le message à déchiffrer:", msg2)
    messageDecrypt=[]
    # parcourir le tab de message
    for element in msg2:
        # dechiffrer chaque élément
        messgae1=decrypt(element,d,n)
        # ajout de message déchiffré au tab messageDechiffrer
        messageDecrypt.append(messgae1)

    print("Le message déchiffré :", messageDecrypt)
    print()






#print("########################################## Partie 3 ###########################################")

def chiffrer_texte(msg): #msg a chiffrer en paramatre


    N = 40
    #public, private = cles()

    print()
    #e = public[0]
    #n = public[1]
    #d = private[0]

    n = 2074
    k = int(floor(log(n, N)))  # la taille de bloc
    Liste = {

        'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8,
        'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20,
        'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, ',': 26, '.': 27, '?': 28, '$': 29, '0': 30, '1': 31, '2': 32,
        '3': 33, '4': 34, '5': 35, '6': 36,
        '7': 37, '8': 38, '9': 39
    }

    c = 0
    j = 0
    # print("k= ",k)
    T = {}
    for i in range(0, len(msg)): # decoupage de bloc
        T[c, j] = str(msg[i])
        code = T[c, j]
        # print(T[c,j], Liste[code])
        j = j + 1
        # print(T)
        if (j >= k):
            c = c + 1
            j = 0
    print(T)
    a = 0
    x = k - 1
    Tabe = []
    for i in range(0, len(T) // k):
        for j in range(0, k):
            a = a + Liste[T[i, j]] * pow(40, x - j)
        # print("a=",a)
        Tabe.append(a)
        # print("TAB ",Tabe)
        # print(Liste[T[i, j]])
        # print(a)
    print(Tabe)
                            #Tabe c'est le msg decoupé en des bloc
    pubclef, privaclef = cles()
    e = pubclef[0]
    msg_Chiffre = []
    for element in Tabe:            #chiffrement de bloc
        element = int(element)
        c = encrypt(element, e, n)
        msg_Chiffre.append(c)
    print("chiffrement de chaque bloc : ", msg_Chiffre) #msg_chiffre retourne le tableau en bloc chiffrée

    texte = []
    for jk in range(0, len(msg_Chiffre)) :
        #print("debug jk", jk)
        for i in range(k+1, -1, -1):
            #print("debug k" , k)
            #print("debug i", i)
            #print("msg_Chiffre[jk]", msg_Chiffre[jk])
            if (msg_Chiffre[jk] / pow(40, i) > 1) :
                chiffre = int(msg_Chiffre[jk] / pow(40, i))
                #print("debug", chiffre)
                alphabet = indiceofalphabet(chiffre)
                msg_Chiffre[jk] = msg_Chiffre[jk] - (chiffre * pow(40, i))
                texte.append(alphabet)
    print(texte)
    resultatfinat = ""
    for x in texte :
        resultatfinat =  resultatfinat + x
    print( resultatfinat)





def indiceofalphabet(c):
    for indice, v in Liste.items():
        if v == c:
            return indice




Liste = {

        'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8,
        'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20,
        'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25, ',': 26, '.': 27, '?': 28, '$': 29, '0': 30, '1': 31, '2': 32,
        '3': 33, '4': 34, '5': 35, '6': 36,
        '7': 37, '8': 38, '9': 39, '_':40
    }




message = input("ecrire le messager à chiffrer : ")


#generationNumAlea()
#testEncryptDecrypt()
#decryptMsg2()

"""
decryptMsg1()
decryptMsg2()
"""
#encryptTxt()
#lettrage([0,39,15])

#indice()
chiffrer_texte(message)