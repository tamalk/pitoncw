tipo = str(input())
resistors = []
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
                read = float(1/val)
            resistors.insert(n, read)
        n += 1
    print(sum(resistors))
