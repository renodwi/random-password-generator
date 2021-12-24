import random
import os
from os import system

os.system("clear")
print("----------------------------------------");
print("> PASSWORD GENERATOR <")
print("INFO : Maksimal panjang password cuma 70 karakter");
print("Creator: rndwst\n");

hurufkecil = "abcdefghijklmnopqrstuvwxyz"
hurufbesar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
angka = "1234567890"
simbol = "+-@$()*/'":#,=!?€¥£¢"

length = int(input("PANJANG PASSWORD : "))
all = hurufkecil + hurufbesar + angka + simbol

password = "".join(random.sample(all, length))
print(f'Password : {password}')
print("----------------------------------------");
