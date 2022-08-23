n = 200
p = [200, 100, 50, 20, 10, 5, 2, 1]

def gen(w, m):
    temp = 0

    if m == 7:
        return 1

    for i in range(m, 8):
        if w-p[i] == 0:
            temp += 1
        elif w-p[i] > 0:
            temp += gen(w-p[i], i)

    return temp


print(gen(n, 0))
