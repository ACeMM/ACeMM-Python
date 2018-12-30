from Binario import *
from Octal import *
from Hexadecimal import *

def Escolha(r):
	if r == "1":
		DecBin( )
		print(" ")
	elif r == "2":
		BinDec( )
		print(" ")
	elif r == "3":
		DecOct( )
		print(" ")
	elif r == "4":
		OctDec( )
		print(" ")
	elif r == "5":
		DecHex( )
		print(" ")
	elif r == "6":
		HexDec( )
		print(" ")
	else:
		print("Valor inválido.")
