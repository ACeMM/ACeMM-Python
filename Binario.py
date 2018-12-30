def DecBin( ):
	num = " "
	nb = [ ]

	print("-" * 30)
	print("     DECIMAL PARA BINÁRIO")
	print("-" * 30)

	while not num.isnumeric( ):
		num = input("Número decimal: ")
		print(" ")
		if not num.isnumeric( ):
			print("Entrada inválida. Digite apenas números.")
			print(" ")

	n = int(num)

	while n % 2 >= 0:
		if n < 2:
			nb.append(str(n))
			break
		q = n // 2
		rd = n % 2
		n = q
		nb.append(str(rd))

	print("Número binário: " + "".join(nb[::-1]))

def BinDec( ):
	nb = " "
	cbn = [ ]
	nd = 0

	print("-" * 30)
	print("     BINÁRIO PARA DECIMAL")
	print("-" * 30)

	while (not "1" in nb) and (not "0" in nb):
		nb = input("Número binário: ")
		print(" ")
		if (not "1" in nb) and (not "0" in nb):
			print("Entrada inválida. Números binários só aceitam valores de 1 ou 0.")
			print(" ")
	lb = list(nb[::-1])

	for x in range(len(lb)):
		cb = 2 ** x
		cbn.append(cb)

	for x in range(len(lb)):
		if lb[x] == "1":
			nd += cbn[x]
	print(f"Número decimal: {nd}")