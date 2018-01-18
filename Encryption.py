# Desenvolvido por Adriel Freud!
# Contato: businessc0rp2k17@gmail.com
# FB: http://www.facebook.com/xrn401
#   =>DebutySecTeamSecurity<=
#conding: utf-8

import string
import random
import sys

key = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(1024))
print(key)

print('\n'+'Key length = '+str(len(key)))
message = raw_input("Menssage: ")
print("Msg is "+message+'\n')

def str_xor(s1, s2):
	return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(s1,s2)])
enc = str_xor(message, key)

print('Encrypted messge is: '+'\n'+enc+'\n')

dec = str_xor(enc, key)
print('Decrypted messge is: '+'\n'+dec)

with open('key.txt', 'w') as w:
	w.write(key)
	w.close()
	m = open('message.txt', 'w')
	m.write(enc)
	m.close()


