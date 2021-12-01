Dbestand = open("Diepte.txt")
Dieptelijst = Dbestand.readlines()
Dbestand.close()

DL2 = []
for i in range(0,len(Dieptelijst)):
    Placeholder = Dieptelijst[i].strip("\n")
    DL2.append(int(Placeholder))

print(DL2)

# Puzel 1
# L = 0
# i = 1
# while i != 2000:
#     if int(Dieptelijst2[i]) > int(Dieptelijst2[i-1]):
#         L = L + 1
#     i = i + 1
#
# print(L)

# Puzel 2
L = 0
for i in range(len(DL2)-3):
    A = DL2[i] + DL2[i+1] + DL2[i+2]
    B = DL2[i+1] + DL2[i+2] + DL2[i+3]
    if B > A:
        L = L + 1
    i = i + 1

print(L)

