print("\nFirmanın İlk 4 Ay Satış Adedi")

liste=[0,"Ocak 12.000", "Şubat 13.500", "Mart 11.000", "Nisan 9.500"]

a=int(input("\nYıl başından itibaren hangi ayların satış adetini görmek istiyorsunuz?"))

print(liste[1:a+1:1])
