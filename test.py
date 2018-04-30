from affine import Affine

ciper = Affine()
while True:
    text = raw_input('Text --> ')
    keys = ciper.getRandomKeys()
    crypted = ciper.crypt(text, keys)
    print 'KEY A: {}\nKEY B: {}'.format(str(keys[0]), str(keys[1]))
    print 'CRYPTED TEXT: '+ crypted
    que = raw_input ('Did you decrypted? (y/n)')
    if que == 'y':    
        decrypted = ciper.decrypt(crypted, keys)
        print decrypted
