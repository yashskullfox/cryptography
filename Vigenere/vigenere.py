def main(args):
    if len(args) != 4:
        printUsage()
    elif args[1] == '-e':
        print(encrypt(args[2], args[3]))
    elif args[1] == '-d':
        print(decrypt(args[2], args[3]))
    else:
        printUsage()
def printUsage():
    print("""
    Usage: main -e <srouce string> <cipher> //Encrypt source string with the cipher by vigenere algorithm;
           main -d <encrypted string> <cipher> //Decrypt encrypted string with the cipher by vigenere algorithm;
    """)
def encrypt(srcStr, cipher):
    result = ''
    j = 0
    for i in range(len(srcStr)):
        c = srcStr.upper()[i]
        if isUpperLetter(c):
            result += encryptChar(c, cipher.upper()[j])
            j = (j + 1) % len(cipher)
        else:
            result += ' '
    return result

def decrypt(encStr, cipher):
    result = ''
    j = 0
    for i in range(len(encStr)):
        c = encStr.upper()[i]
        if isUpperLetter(c):
            result += decryptChar(c, cipher.upper()[j])
            j = (j + 1) % len(cipher)
        else:
            result += ' '
    return result

if __name__ == "__main__":
    import sys
    main(sys.argv)
