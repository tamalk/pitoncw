pos = int(input())
planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]
if pos < 1 or pos > 8:
	print ("Error. No hay ningún planeta en dicha posición.")
else:
	print("La posición " + str(pos) + " corresponde al planeta " + planetas[pos - 1] + ".")
