din = float(input())
quin = int(din / 500)
quinr = din % 500
dosc = int(quinr / 200)
doscr = quinr % 200
cien = int(doscr / 100)
cienr = doscr % 100
cinc = int(cienr / 50)
cincr = cienr % 50
vein = int(cincr / 20)
veinr = cincr % 20
diez = int(veinr / 10)
diezr = veinr % 10
five = int(diezr / 5)
fiver = diezr % 5
dos = int(fiver / 2)
dosr = fiver % 2
uno = int(dosr)
unor = dosr - uno
medio = int(unor / 0.5)
medior = unor % 0.5
quinto = int(medior / 0.2)
quintor = medior % 0.2
decimo = int(quintor / 0.1)
decimor = quintor % 0.1
vavo = int(decimor / 0.05)
vavor = decimor % 0.05
cavo = int(vavor / 0.02)
cavor = vavor % 0.02
cent = int(cavor)
print("Billetes de quinientos euros: " + str(quin))
print("Billetes de doscientos euros: "+ str(dosc))
print("Billetes de cien euros: " + str(cien))
print("Billetes de cincuenta euros: " + str(cinc))
print("Billetes de veinte euros: " + str(vein))
print("Billetes de diez euros: " + str(diez))
print("Billetes de cinco euros: " + str(five))
print("Monedas de dos euros: " + str(dos))
print("Moneadas de un euros: " + str(uno))
print("Monedas de cincuenta céntimos: " + str(medio))
print("Monedas de veinte céntimos: " + str(quinto))
print("Monedas de diez céntimos: " + str(decimo))
print("Monedas de cinco céntimos: " + str(vavo))
print("Monedas de dos céntimos: " + str(cavo))
print("Monedas de un céntimo: " + str(cent))
