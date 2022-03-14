input = input("kata : ")

def isKata(input):
	return input == input[::-1]

tes = isKata(input)

if tes:
	print ("True")
else:
	print ("False")
