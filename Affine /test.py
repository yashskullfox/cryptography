from affine import Affine

ciper = Affine()
while True:
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
