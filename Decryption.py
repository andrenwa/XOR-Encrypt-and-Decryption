import sys

def str_xor(s1, s2):
	return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(s1,s2)])

if len(sys.argv) < 3:
	print("\n\nModo de uso:\n./XorDecrypt key.txt message.txt// file for decrypt the XOR HASH ! and message\n:)\n\n")
else:
	file_key = open(sys.argv[1], 'r')
	file_message = open(sys.argv[2], 'r')
	message = file_message.read().strip('\n')
	key = file_key.read().strip('\n')
	decrypted_xor = str_xor(message, key)
	print('Message decripted: \n\n%s\n'%decrypted_xor)