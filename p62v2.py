def cubic_permutations(n):
    cubes = {}
    cands = []
    i = 1
    digits = 0

    while True:
        c = i**3
        s = ''.join(sorted(str(c)))

        if cands != [] and len(s) > digits:
            cands = [x for x in cands if len(x) == n]

            if cands != []:
                return min(map(min, cands))

        l = cubes.setdefault(s, [])
        l.append(c)

        if len(l) == n:
            cands.append(l)
            digits = len(s)


        i += 1

print(cubic_permutations(5))
