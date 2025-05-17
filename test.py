import random

posisi_kelinci = random.randint(1,4)
inputUser = input("input !...")

while int(inputUser) not in (1,2,3,4) :
    inputUser = input("input yang betul...")
print("betul")
