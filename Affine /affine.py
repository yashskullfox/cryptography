import string
import random
WORDS = list(string.ascii_lowercase)

def gcd(a, b):
    while a != 0: 
        a, b = b % a, a 
    return b    

def modInverse(a, m): 
    if gcd(a, m) != 1: 
        return None 
    u1, u2, u3 = 1, 0, a 
    v1, v2, v3 = 0, 1, m 
    while v3 != 0: 
        q = u3 // v3 
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3 
        
    return u1 % m



class Affine(object):        
    def getRandomKeys(self):
        while True:
            keyA = input( 'enter value for a key: ')
            keyB = input( 'enter value for b key: ')
            return (keyA,keyB)
            
    def crypt(self, text, keys):
        text = text.lower()
        keyA, keyB = keys
        cipertext = ""
        for i in text:
            cipertext +=  WORDS[(keyA*WORDS.index(i) + keyB)%len(WORDS)]
        return cipertext
    
    def decrypt(self, text1, keys1):
        text1 = text1.lower()
        keysA, keysB = keys1
        plaintext = ""
        inverseA = modInverse(keysA, len(WORDS))
        for char in text1:
            if char in WORDS:
                plaintext  += WORDS[(WORDS.index(char) - keysB) * inverseA % len(WORDS)]           
            else:
                plaintext += char        
        return plaintext
