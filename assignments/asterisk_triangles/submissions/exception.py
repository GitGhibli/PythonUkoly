def asterisk_triangles(iterations):
    # x = int(input("zadaj pocet riakov: "))
    for riadky in range (1, iterations+1):
        for stlpec in range (1, riadky+1):
            prin("*", end=" ")
        print()