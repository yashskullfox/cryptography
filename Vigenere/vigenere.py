""" Cypher matrix handler """

from string import ascii_lowercase as l

class CypherTable:
        
	def __init__(self):
		self.matrix = [l[i:]+l[:i] for i in range(len(l))]

	def cross(self, b, a):
   		val1 = self.matrix[0].index(a)	
		new_letter = [i for i in self.matrix if i[0] == b][0][val1]	
   		return new_letter

	def decross(self, b, a):
   		val1 = self.matrix[0].index(a)	
   		val2 = self.matrix[0].index(b)	
   		new_letter = [i for i in self.matrix if i[val1] == b][0][0]	
   		return new_letter

	def __str__(self):
		return "\n".join('|'.join(row) for row in self.matrix)		
	def encrypt(self, string, key):
		encryptedString = ""
		keyRange = len(string) - len(key)
		for i in range(keyRange):	
			key += key[i]
		
		for i in range(len(string)):
			encryptedString += self.cross(string[i], key[i])
		return encryptedString

	def decrypt(self, string, key):
		decryptedString = ""
		keyRange = len(string) - len(key)
		for i in range(keyRange):	
			key += key[i]	
		for i in range(len(string)):
			decryptedString += self.decross(string[i], key[i])
		return decryptedString
