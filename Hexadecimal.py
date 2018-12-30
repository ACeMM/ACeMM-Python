def DecHex():
	num = " "
	let = 55
	hx = [ ]
	nb = [ ]

	print("-" * 30)
	print("   DECIMAL PARA HEXADECIMAL")
	print("-" * 30)

	while (not num.isnumeric( )):
		num = input("Número decimal: ")
		print(" ")
		if (not num.isnumeric( )):
			print("Entrada inválida. Digite apenas números.")
			print(" ")

	n = int(num)

	while n % 16 >= 0:
		if n < 16:
			nb.append(n)
			break
		q = n // 16
		rd = n % 16
		n = q
		nb.append(rd)

	for x in nb:
		if x > 9:
			lt = chr(x + let)
			hx.append(lt)
		else:
			hx.append(str(x))

	print("Número hexadecimal: " + "".join(hx[::-1]))

def HexDec( ):
	n = " "
	let = 55
	nd = 0
	nb = [ ]
	td = [ ]
	tv = [ ]
	ns = [ ]

	print("-" * 30)
	print("   HEXADECIMAL PARA DECIMAL")
	print("-" * 30)

	while (not n.isalnum( )):
		n = input("Número hexadecimal: ").upper( )
		print(" ")
		if (not n.isalnum( )):
			print("Entrada inválida. Digite apenas números e apenas letras de A até F.")
			print(" ")

	for x in n:
		if x.isdigit( ):
			v = int(x)
		else:
			v = ord(x) - let
		ns.append(v)

	for x in range(3, -1, -1):
		v = 2 ** x
		tv.append(v)

	for x in ns:
		for y in range(len(tv)):
			if x >= tv[y]:
				r = x - tv[y]
				x = r
				b = 1
			else:
				b = 0
			nb.append(str(b))

	for x in range(len(nb)):
		vd = 2 ** x
		td.append(vd)

	tdi = td[::-1]

	for x in range(len(nb)):
		if nb[x] == "1":
			nd += tdi[x]

	print(f"Número decimal: {nd}")