from CypherTable import CypherTable
from time import sleep

keyWord = ""
table = CypherTable()
while(True):
    que = raw_input ('Did you want to ENCRYPTED than press E and DECRYPTED than press D. (e/d)')
    sleep(0.2)	# output time control
    if que == 'c':  # 1 - Set Key
        keyWord = raw_input("Choose a keyword: ").replace(" ","").lower()	# forcing key for encryption lowercase
        #elif (que != 1 or que != 0) and keyWord == "" :	# If user wants to encrypt/decrypt but no key was set
        #print("You have to set a keyword first")
    elif que == 'e':		# 2 - Encrypt
        encryptedMessage = ""
        phrase = raw_input("Insert a message to encrypt: ").lower()	# forcing word to decryptn lowercase
        for word in phrase.split():
            encryptedMessage += table.encrypt(word, keyWord) + " "
            print("Encrypting message...")
            sleep(1)	# output time control
            print encryptedMessage
    elif que == 'd':	# 3 - Decryp
        decryptedMessage = ""
        phrase = raw_input("Insert a message to decrypt: ").lower()	# forcing word to decryptn lowercase
        for word in phrase.split():
            decryptedMessage += table.decrypt(word, keyWord) + " "
            print("Decrypting message...")
            sleep(1)	# output time control
            print decryptedMessage[: len(decryptedMessage) - 1]	#cutting space in last word

            

