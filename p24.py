d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

perms = []

def generate_p(p, digs):
    if digs == []:
        perms.append(p)
        return

    for i in digs:
        temp_p = p + str(i)
        temp_d = [j for j in digs if i != j]
        generate_p(temp_p, temp_d)


for i in d:
    temp_p = str(i)
    temp = [j for j in d if i != j]
    generate_p(temp_p, temp)

print(perms[999999])
