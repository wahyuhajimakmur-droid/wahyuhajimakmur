#program untuk menghitung jumlah huruf vokal pada sebuah kalimat
#string of vowels

import pandas as pd

vowels = 'aeiou'


ip_str = str(input("Masukkan sebuah kalimat: "))


#memodifikasi kalimat agar memiliki format yang sama setiap karakter
ip_str = ip_str.casefold()


# membuat sebuah dictionary dengan setiap huruf vokal menjadi key dan value awal adalah 0
count = {}.fromkeys(vowels,0)


# menghitung jumlah huruf vokal
for char in ip_str:
   if char in count:
       count[char] += 1


count_table = pd.DataFrame(count, index=['Jumlah'])
print(count_table)