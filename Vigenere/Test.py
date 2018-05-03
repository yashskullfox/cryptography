from CypherTable import CypherTable
from time import sleep

keyWord = ""
table = CypherTable()
print("This program developed by Yashskullfox for Prof. Qian Wang OSS")
print("First, You have to choose keyword by presssing 'c' ")
while(True):
    que = raw_input ('Do you want to ENCRYPT than press E and DECRYPT than press D. (c/e/d)')
    sleep(0.2)	
    if que == 'c':  
        keyWord = raw_input("Choose a keyword: ").replace(" ","").lower()	
    elif que == 'e':		
        encryptedMessage = ""
        phrase = raw_input("Insert a message to encrypt: ").lower()	
        for word in phrase.split():
            encryptedMessage += table.encrypt(word, keyWord) + " "
            print("Encrypting message...")
            sleep(1)
            print encryptedMessage
    elif que == 'd':	
        decryptedMessage = ""
        phrase = raw_input("Insert a message to decrypt: ").lower()	
        for word in phrase.split():
            decryptedMessage += table.decrypt(word, keyWord) + " "
            print("Decrypting message...")
            sleep(1)	
            print decryptedMessage[: len(decryptedMessage) - 1]	
            

