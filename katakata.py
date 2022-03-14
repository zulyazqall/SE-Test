inp = input("kata : ")


def reverse(inp):
	str= ""

	for i in inp:
		str = i + str
	return str

tes = reverse(inp) == inp

if tes:
        print("true")
else:
        print("false")
