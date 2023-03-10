def linearSearch(var, n, elemen):

    for i in range(0, n):
        if (var[i] == elemen):
            print(elemen, "berada di index ke", i)
            return i
    for kolom in range(len(var[i])):
        if (var[i][kolom] == elemen):
            print(elemen, "berada di index ke", i, "pada kolom", kolom) 
            return i   
    else:
        print("Elemen tidak ditemukan")

var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
elemen = str(input("Apa yang ingin Anda cari: "))
n = len(var)
result = linearSearch(var, n, elemen)