Movement = open("Movement.txt")
i = 1
raw = []
while i < 1001:
    PL = Movement.readline()
    PL = PL.strip("\n")
    raw.append(PL)
    i += 1
Movement.close()

NotRaw = []
i = 0
while i != 1000:
    pl = raw[i]
    pl = pl.split()
    NotRaw.append(pl)
    i += 1

print(NotRaw)

# Opdracht 1
# i = 0
# d = 0
# f = 0
# while i != 1000:
#     Mo = NotRaw[i][0]
#     Nu = int(NotRaw[i][1])
#     if Mo == "forward":
#         f += Nu
#     if Mo == "down":
#         d += Nu
#     if Mo == "up":
#         d -= Nu
#     i += 1
#
# print(d)
# print(f)
# print(f*d)

i = 0
A = 0
F = 0
D = 0
while i != 1000:
    Mo = NotRaw[i][0]
    Nu = int(NotRaw[i][1])
    if Mo == "forward":
        F += Nu
        D += A * Nu
    if Mo == "down":
        A += Nu
    if Mo == "up":
        A -= Nu
    i += 1

print(D)
print(F)
print(D*F)