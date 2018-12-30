from Opcoes import *

def Main( ):
   r = " "
   print("-" * 30)
   print(" " * 16 + "OPÇÕES")
   print("-" * 30)

   while (r == "") or (len(r) > 1) or (ord(r) < 49) or (ord(r) > 54):
      r = input("1 - Decimal para binário \n2 - Binário para decimal \n3 -" +
                  " Decimal para octal \n4 - Octal para decimal \n5 - Decimal para" +
                  " hexadecimal \n6 - Hexadecimal para decimal \n")
      print(" ")

      if (r == "") or (len(r) > 1) or (ord(r) < 49) or (ord(r) > 54):
         print("Entrada inválida. Digite apenas números de 1 a 6.")
         print(" ")

   Escolha(r)

e = "S"
while e == "S":
   Main( )

   e = input("Deseja continuar? S/N \n").upper( )
   print(" ")

   while (e != "S") and (e != "N"):
      e = input("Deseja continuar? S/N \n").upper( )
      print(" ")
      if (e != "S") and (e != "N"):
         print("Entrada inválida.")
         print(" ")

   if e == "N":
      print("-" * 30)
      print(" " * 20 + "FIM")
      print("-" * 30)

if __name__ == "__Main__":
   Main( )
