sayi1 = 30
sayi2 = 20
sayi3 = 10

if sayi1 > sayi2 > sayi3:
  print("Sayi 1 En Buyuk Degerdir")
  print(sayi1)

elif sayi2 > sayi1 and sayi2 > sayi3:
  print("ikinci sayi hem 3.den ve hem de birinciden daha buyuktur")
  print(sayi2)

else:
  print("Ucuncu Sayi En Buyuktur")
  print(sayi3)

if sayi1 < sayi2 and sayi1 < sayi3:
  print("Birinici Sayi En Buyuktur")
  print(sayi3)

elif sayi2 < sayi1 and sayi2 < sayi3:
  print("Ikinci Sayi En Kucuktur")
  print(sayi2)

else:
  print("Ucuncu Sayi En Kucuktur")
  print(sayi3)
