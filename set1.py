import codecs

def convert_hex_to_base64(hex_string):
	decoded_string = codecs.decode(hex_string, 'hex')
	base64_string = codecs.encode(decoded_string, 'base64')
	return base64_string





# challenge 1
hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
base64_string = convert_hex_to_base64(hex_string)
print(base64_string)