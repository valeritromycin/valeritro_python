peshka = (1, 4)

pherz = (3, 2)

diff_x = peshka[0] - pherz[0]
diff_y = peshka[1] - pherz[1]

if diff_x == 0 or diff_y == 0 or abs(diff_x) == abs(diff_y):
    ruin = True
else:
    ruin = False

print(ruin)