def diagonal (mat, n):
	satu = 0
	dua = 0

	# for i in range (0, n):
		for j in range (0,n):
			if (i == j):
				satu += mat[i][j]
			if ((i + j) == (n -1)):
				dua += mat [i][j]

	print ("diagonal satu ", satu)
	print ("diagonal dua ", dua) 
	print ("total", satu+dua)

x = [
	[11,2,4,3],
	[4,5,6,3],
	[10,8,12,3],
	[3,3,3,3]
]

diagonal(x, 4)
