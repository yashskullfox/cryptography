""" Vigenere Cipher """
from CypherTable import CypherTable
from time import sleep

def main():
	keyWord = ""
	table = CypherTable()
	while(True):
		sleep(0.2)	# output time control
		choice = menuChoice()	# menu printing and menu voice selecting
		
		if choice == 0:	# 0 - Quit
			exit()
		elif choice == 1:	# 1 - Set Key
			keyWord = changeKeyWord()
		elif (choice != 1 or choice != 0) and keyWord == "" :	# If user wants to encrypt/decrypt but no key was set
			print("You have to set a keyword first")
		else:
			if choice == 2:		# 2 - Encrypt
				word = raw_input("Insert the word to enrypt: ").lower()		# forcing word to encryptn lowercase
				encryptedString = table.encrypt(word, keyWord)
				print("Encrypting word...")
				sleep(1)	# output time control
				print("Original word: " + word)
				print("Encrypted word: " + encryptedString)
			elif choice == 3:	# 3 - Decrypt
				word = raw_input("Insert the word to decrypt: ").lower()	# forcing word to decryptn lowercase
				decryptedString = table.decrypt(word, keyWord)
				print("Decrypting word...")
				sleep(1)	# output time control
				print("Encrypted word: " + encryptedString)
				print("Decrypted word: " + decryptedString)
			elif choice == 4:	# 4 - Encrypt phrase
				encryptedMessage = ""
				phrase = raw_input("Insert a message to encrypt: ").lower()	# forcing word to decryptn lowercase
				for word in phrase.split():
					encryptedMessage += table.encrypt(word, keyWord) + " "
				print("Encrypting message...")
				sleep(1)	# output time control
				print encryptedMessage

			elif choice == 5:	# 5 - Decrypt phrase
				decryptedMessage = ""
				phrase = raw_input("Insert a message to decrypt: ").lower()	# forcing word to decryptn lowercase
				for word in phrase.split():
					decryptedMessage += table.decrypt(word, keyWord) + " "
				print("Decrypting message...")
				sleep(1)	# output time control
				print decryptedMessage[: len(decryptedMessage) - 1]	#cutting space in last word

				
				

def menuChoice():
	while(True):
		""" Menu printing """
		print("  \n*** Vigenere Cipher ***")
		print("Select a voice from the menu")
		print("	1 - Insert/change key word")
		print("	2 - Encrypt a word")
		print("	3 - Decrypt a word")
		print("	4 - Encrypt a message")
		print("	5 - Decrypt a message")
		print("	0 - Quit")

		""" User input """
		try:
			choice = int(raw_input())	# converting input to integer
		except(ValueError):				
			choice = -1					# catching = -1 if not integer

		""" Selecting return value """
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
	elif value == 3:
		return 3
	elif value == 4:
		return 4
	elif value == 5:
		return 5
	elif value == 0:
		return 0
	else:
		return -1

def changeKeyWord():
	keyWord = raw_input("Choose a keyword: ").replace(" ","").lower()	# forcing key for encryption lowercase
	return keyWord


if __name__ == "__main__": main()
