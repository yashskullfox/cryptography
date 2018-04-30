from affine import Affine

ciper = Affine()
while True:
    que = raw_input('did you want to encryot or decrypt ? (e/d)')
    if que == 'e':
    text = raw_input('Text --> ')
    keys = ciper.getRandomKeys()
    crypted = ciper.crypt(text, keys)
    print 'KEY A: {}\nKEY B: {}'.format(str(keys[0]), str(keys[1]))
    print 'CRYPTED TEXT: '+ crypted
    que = raw_input ('Did you decrypted? (y/n)')
    elif que == 'd':    
        text1 = raw_input('text--')
        keys1 = cipher.getRandomKeys()
        decrypted = ciper.decrypt(crypted, keys)
        print decrypted
    else:
        return
