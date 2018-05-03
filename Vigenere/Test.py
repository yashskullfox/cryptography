from CypherTable import CypherTable
from time import sleep

keyWord = ""
table = CypherTable()
while(True):
    print("This program developed by Yashskullfox for Prof. Quang Wang OSS")
    print("First, You have to choose keyword by presssing 'c' ")
    que = raw_input ('Do you want to ENCRYPT than press E and DECRYPT than press D. (c/e/d)')
    sleep(0.2)	# output time control
    if que == 'c':  # 1 - Set Key
        keyWord = raw_input("Choose a keyword: ").replace(" ","").lower()	# forcing key for encryption lowercase
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

            

