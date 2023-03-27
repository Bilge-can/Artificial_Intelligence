#For döngüsü ile program:
sayısalDeğerler = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

# for döngüsü ile 5'e bölünen sayıları bulma
print("For döngüsü ile çözüm:")
for sayi in sayısalDeğerler:
    if sayi % 5 == 0 and sayi < 150:
        print(sayi)

#*********************************************************************************************************

#While döngüsü ile program:
sayısalDeğerler = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

# while döngüsü ile 5'e bölünen sayıları bulma
print("While döngüsü ile çözüm:")
index = 0
while index < len(sayısalDeğerler):
    if sayısalDeğerler[index] % 5 == 0 and sayısalDeğerler[index] < 150:
        print(sayısalDeğerler[index])
    index += 1