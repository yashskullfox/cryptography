from affine import Affine
def main():
    ciper = Affine()
    choice = menuChoice()
while True:
    
        if choice == 0:	# 0 - Quit
            exit()
        elif choice == 1:	# 1 - Set Key
			keyWord = changeKeyWord()
	elif (choice != 1 or choice != 0) and keyWord == "" :	# If user wants to encrypt/decrypt but no key was set
			print("You have to set a keyword first")
        else:
		if choice == 1:
            text1 = raw_input('Text --> ')
            keys1 = ciper.getKeys()
            decrypted = ciper.decrypt(crypted, keys1)
            print 'DECRYPTED TEXT: '+ decrypted
            print decrypted
        elif choice == 2:
            text = raw_input('Text --> ')
            keys = ciper.getRandomKeys()
            crypted = ciper.crypt(text, keys)
            print 'KEY A: {}\nKEY B: {}'.format(str(keys[0]), str(keys[1]))
            print 'CRYPTED TEXT: '+ crypted
def menuChoice():
	while(True):
            """ Menu printing """
		print("  \n*** Affine Cipher ***")
		print("Select a voice from the menu")
		print("	1 - Encrypt text")
		print("	2 - deEncrypt a word")
		try:
			choice = int(raw_input())	# converting input to integer
		except(ValueError):				
			choice = -1
			if(switch(choice) == -1):
			print("*** ERROR ***")
			print("You didn't insert a correct value")
			print("Please insert it again\n")
		else:
			return switch(choice)
def switch(value):
	""" Switch value handler """
	if value == 1:
		return 1
	elif value == 2:
		return 2
	    elif value == 0:
		return 0
	else:
		return -1

		    
            
