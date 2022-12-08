#Soal 1
n = input("Masukkan Kata atau Angka :" )
def reserve (n):
    str = ""
    for i in n :
        str = i + str
    return str
print (reserve(n))
