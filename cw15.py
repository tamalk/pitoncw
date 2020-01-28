sano = input()
coronavirus = input()
inf = []
pos = []
nindex = 0
nospace = sano[: : 2]
nospacecorona = coronavirus[: : 2]
if sano != coronavirus and len(nospace) == 8 and len(nospacecorona) == 8:
    print("El ADN saludable es: { " + sano + " }")
    print("El ADN infectado por el virus es: { " + coronavirus + " }")
    for i in range(len(nospace) - 1):
        if nospace[i] != nospacecorona[i]:
            infected = nospacecorona[i]
            inf.insert(nindex, infected)
            pos.insert(nindex, i)
            nindex += 1
    if len(pos) > 1:
        print("El fragmento del ADN infectado por el virus va de la base " + str(pos[1]) + " a la base " + str(pos[len(pos) - 1] + 1) + ": { ", end="")
    else:
        print("La base del ADN infectada por el virus es la base " + str(pos[0] + 1) + ": { ", end="")
    for x in range(len(inf)):
        print(inf[x] + " ", end="")
    print("}")
    print("Ahora, el ADN infectado por la gripe está curado: { " + sano + " }")
else:
    print("Error. Vuelva a introducir las secuencias de ADN, por favor. Recuerde que debe haber espacios entre las bases.")    
