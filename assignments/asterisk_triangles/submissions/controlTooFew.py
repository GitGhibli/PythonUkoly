def asterisk_triangles(iterations):
    file = open("vysledok.txt", "w")
    for riadky in range (1, iterations):
        for stlpec in range (1, riadky+1):
            file.write("*")
        file.write('\n')
    
    file.flush()
    file.close()