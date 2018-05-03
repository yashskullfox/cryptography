import string
import random

__author__ = 'easyly'
__version__ = 2.0


#SYMBOLS = "@#$%&,*-+()!:.'\";/?~`|{}^_=[]\<>" + '\n\t'
WORDS = list(string.ascii_lowercase) # + ' ' + SYMBOLS + string.digits)

def gcd(a, b):
    """
    OBEB gcd
    URL: http://bilgisayarkavramlari.sadievrenseker.com/2009/10/26/obeb-gcd/
    """
    while a != 0: 
        a, b = b % a, a 
    return b    

def modInverse(a, m): 
    """
    MODULER TERSLIK
    URL: https://tr.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/modular-inverses
    """ 
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
#            keya = random.randint(2, len(WORDS))
#            keyb = random.randint(2, len(WORDS))
#            if gcd(keya, len(WORDS)) == 1:
                # PARSE KEYS
#                key = keya * len(WORDS) + keyb
#                keyA = key // len(WORDS)
#                keyB = key % len(WORDS)
                keyA = input( 'enter a value for a key: ')
                keyB = input( 'enter a value for b key: ')
                return (keyA,keyB)
            
    def crypt(self, text, keys):
        """
        @param text: text to be encrypted
        @param keys: key tuple type
        """
        text = text.lower()
        keyA, keyB = keys
        cipertext = ""
        for i in text:
            cipertext +=  WORDS[(keyA*WORDS.index(i) + keyB)%len(WORDS)]
        return cipertext
    
    def decrypt(self, text1, keys1):
        """
        @param text: text to be decrypted
        @param keys: key tuple type
        """
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
