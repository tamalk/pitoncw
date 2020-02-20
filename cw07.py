tipo = str(input())
resistors = []
respar = 0
val = 0
n = 0
if (tipo != "s" and tipo != "p"):
    print("Entrada no válida.")
else:
    while (val != "f"):
        val = input()
        if (val != "f"):
            if (tipo == "s"):
                read = float(val)
            if (tipo == "p"):
                read = float(1/float(val))
            resistors.insert(n, read)
        n += 1
    if (tipo == "s"):
        print(sum(resistors))
    else:
        for i in resistors:
            resa = resistors[i]
            resb = float(1/resa)
            respar += resb
        print(1/respar)
