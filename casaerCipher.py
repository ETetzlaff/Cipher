def baseexp(n,b):
    q = n
    k = 0
    a = []
    while q != 0:
        a.append(q % b)
        q = q // b
        k += 1
    return a
def modularexp(b, a, m):
    l1 = baseexp(a, 2)
    y = 1
    power = b % m
    for i in range(0, len(l1)):
        if l1[i] == 1:
            y = (y*power) % m
        power = (power*power) % m
    return y
def converttext(text):                 #converting string into list of integers
    key = "abcdefghijklmnopqrstuvwxyz" 
    coded = []
    for i in text:
        for a in range(00, len(key)):
            if i == key[a]:
                coded.append(a)
    print coded
    return coded
def convertints(int):                  #converting list of ints to string
    key = "abcdefghijklmnopqrstuvwxyz"
    string2 = ''
    for i in int:
        for a in range(0, len(key)):
            if i == a:
                string2 += key[a]
    print string2
    return string2

def caesarCipher(ints, n):                #Encryptoion
    a = []                            #declaring temp list for shifted integer list
    for i in range(0, len(ints)):     #Execute cipher equation on each index
        a.append((3*ints[i]+n)%26)
    print a
    newString = convertints(a)
    print newString
    return newString
    
def decaesarCipher(ints, n):          #Excute cipher of equation for decryption
      a = []                            #declaring temp list for shifted integer list
      for i in range(0, len(ints)):     #Execute cipher equation on each index
        a.append((3*ints[i]-n)%26)
      print a
      newString = convertints(a)
      print newString
      return newString


temp = 'need help'
b = converttext(temp)
z = ''
z = caesarCipher(b, 7)

y = converttext(z)
c = decaesarCipher(y, 7)



