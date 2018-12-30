def DecOct( ):
	num = " "
	no = [ ]

	print("-" * 30)
	print("     DECIMAL PARA OCTAL")
	print("-" * 30)

	while not num.isnumeric( ):
		num = input("Número decimal: ")
		print(" ")
		if not num.isnumeric( ):
			print("Entrada inválida. Digite apenas números.")
			print(" ")

	n = int(num)

	while n % 8 >= 0:
		if n < 8:
			no.append(str(n))
			break
		q = n // 8
		rd = n % 8
		n = q
		no.append(str(rd))

	print("Número octal : " + "".join(no[::-1]))

def OctDec( ):
	num = " "
	nb = [ ]
	tv = [ ]
	td = [ ]
	ns = [ ]
	nd = 0

	print("-" * 30)
	print("     OCTAL PARA DECIMAL")
	print("-" * 30)

	while (not num.isnumeric( )) or ("8" in num) or ("9" in num):
		num = input("Número octal: ")
		print(" ")
		if (not num.isnumeric( )) or ("8" in num) or ("9" in num):
			print("Entrada inválida. Digite apenas números com digitos de 0 a 7.")
			print(" ")

	n = int(num)

	while n >= 10:
		q = n // 10
		rd = n % 10
		n = q
		ns.append(rd)
		if n < 10:
			ns.append(n)
	a = ns[::-1]

	for x in range(2, -1, -1):
		v = 2 ** x
		tv.append(v)

	for x in a:
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