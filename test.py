from affine import Affine

ciper = Affine()
while True:
<<<<<<< HEAD
    que = raw_input ('Did you want to ENCRYPTED than press E and DECRYPTED than press D. (e/d)')
    if que == 'e':
        text = raw_input('Text --> ')
        keys = ciper.getRandomKeys()
        crypted = ciper.crypt(text, keys)
        print 'KEY A: {}\nKEY B: {}'.format(str(keys[0]), str(keys[1]))
        print 'CRYPTED TEXT: '+ crypted
    elif que == 'd':
        text1 = raw_input('Text --> ')
        keys1 = ciper.getRandomKeys()
        decrypted = ciper.decrypt(text1, keys1)
        print 'KEY A: {}\nKEY B: {}'.format(str(keys1[0]), str(keys1[1]))
        print 'DECRYPTED TEXT: '+ decrypted
=======
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
>>>>>>> 8fa09d644b79f2aa108156f5f631b8039c4df750
