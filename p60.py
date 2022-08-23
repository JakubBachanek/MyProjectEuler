from itertools import combinations
LIMIT = 600000

primes = [True for _ in range(LIMIT+1)]
p = 2

for i in range(p*p, LIMIT+1, p):
    primes[i] = False

p = 3

while p*p <= LIMIT:
    if primes[p] == True:
        for i in range(p*p, LIMIT+1, p):
            primes[i] = False

    p += 2

primes[0] = False
primes[1] = False


def check_prime(n):
    if n%2 == 0:
        return False

    prime = True
    p = 3

    while p*p < n+1:
        if n % p == 0:
            prime = False
            break

        p += 2

    return prime

testowe = [3, 7, 13, 19, 31, 37, 43, 61, 67, 73, 79, 97, 103, 109, 127, 139, 151, 157, 163, 181, 193, 199, 211, 223, 229, 241, 271, 277, 283, 307, 313, 331, 337, 349, 367, 373, 379, 397, 409, 421, 433, 439, 457, 463, 487, 499, 523, 541, 547, 571, 577, 601, 607, 613, 619, 631, 643, 661, 673, 691, 709, 727, 733, 739, 751, 757, 769, 787, 811, 823, 829, 853, 859, 877, 883, 907, 919, 937, 967, 991, 997, 1009, 1033, 1039, 1051, 1063, 1069, 1087, 1093, 1117, 1129, 1153, 1171, 1213, 1231, 1237, 1249, 1279, 1291, 1297, 1303, 1321, 1381, 1399, 1447, 1453, 1459, 1471, 1483, 1489, 1531, 1543, 1549, 1567, 1579, 1597, 1609, 1621, 1627, 1657, 1663, 1669, 1693, 1699, 1723, 1741, 1759, 1777, 1783, 1801, 1831, 1861, 1867, 1873, 1933, 1951, 1993, 1999, 2011, 2017, 2029, 2053, 2089, 2113, 2131, 2137, 2161, 2179, 2203, 2221, 2239, 2251, 2269, 2281, 2287, 2293, 2311, 2341, 2347, 2371, 2377, 2383, 2389, 2437, 2467, 2473, 2503, 2539, 2551, 2557, 2593, 2617, 2647, 2659, 2671, 2683, 2689, 2707, 2719, 2731, 2749, 2791, 2797, 2803, 2833, 2851, 2887, 2917, 2953, 3001, 3037, 3049, 3061, 3067, 3109, 3121, 3163, 3181, 3187, 3217, 3229, 3253, 3259, 3301, 3307, 3313, 3331, 3343, 3361, 3391, 3433, 3457, 3463, 3469, 3499, 3511, 3517, 3529, 3541, 3547, 3559, 3571, 3583, 3613, 3637, 3697, 3709, 3727, 3733, 3769, 3823, 3847, 3853, 3919, 3931, 3943, 4021, 4027, 4057, 4111, 4129, 4159, 4177, 4219, 4231, 4243, 4261, 4327, 4339, 4357, 4363, 4423, 4441, 4447, 4483, 4507, 4513, 4519, 4549, 4561, 4567, 4591, 4597, 4603, 4657, 4663, 4723, 4729, 4759, 4789, 4801, 4813, 4903, 4909, 4951, 4957, 4987, 4993, 5011, 5059, 5077, 5101, 5107, 5113, 5119, 5179, 5197, 5281, 5323, 5407, 5413, 5431, 5437, 5449, 5503, 5521, 5527, 5557, 5563, 5569, 5581, 5623, 5647, 5653, 5659, 5683, 5701, 5737, 5743, 5749, 5779, 5791, 5821, 5827, 5839, 5851, 5857, 5869, 5881, 5923, 6007, 6037, 6043, 6073, 6079, 6091, 6121, 6133, 6163, 6199, 6229, 6247, 6271, 6301, 6337, 6343, 6361, 6367, 6373, 6379, 6397, 6421, 6427, 6451, 6481, 6529, 6553, 6607, 6637, 6661, 6673, 6679, 6691, 6709, 6733, 6763, 6781, 6793, 6823, 6829, 6841, 6871, 6949, 6967, 6991, 6997, 7039, 7057, 7069, 7159, 7177, 7207, 7213, 7237, 7297, 7309, 7351, 7369, 7393, 7417, 7459, 7489, 7507, 7537, 7549, 7561, 7573, 7591, 7639, 7669, 7681, 7687, 7699, 7723, 7741, 7753, 7759, 7873, 7927, 7933, 7993, 8011, 8017, 8089, 8101, 8161, 8179, 8191, 8221, 8233, 8269, 8287, 8311, 8317, 8329, 8353, 8377, 8389, 8431, 8461, 8539, 8581, 8599, 8623, 8629, 8641, 8647, 8689, 8707, 8713, 8719, 8731, 8737, 8779, 8803, 8821, 8839, 8887, 8893, 8923, 8929, 8941, 8971, 9001, 9007, 9043, 9049, 9067, 9091, 9133, 9157, 9187, 9199, 9283, 9319, 9337, 9343, 9349, 9397, 9403, 9421, 9433, 9439, 9463, 9511, 9547, 9601, 9613, 9631, 9649, 9661, 9679, 9697, 9721, 9733, 9769, 9787, 9811, 9817, 9829, 9859, 9871, 9883, 9901, 9907, 9931, 9967, 20023, 36097, 63493, 93187]
l = len(testowe)
print(l)


# bruteforce strong :)

for i in range(l):
    print(i)
    for j in range(i+1, l):
        if check_prime(int(str(testowe[i])+str(testowe[j]))) and check_prime(int(str(testowe[j])+str(testowe[i]))):
            for k in range(j+1, l):
                if (check_prime(int(str(testowe[i])+str(testowe[k]))) and check_prime(int(str(testowe[k])+str(testowe[i])))
                    and check_prime(int(str(testowe[j])+str(testowe[k]))) and check_prime(int(str(testowe[k])+str(testowe[j])))):
                        for kk in range(k+1, l):
                            if (check_prime(int(str(testowe[i])+str(testowe[kk]))) and check_prime(int(str(testowe[kk])+str(testowe[i])))
                                and check_prime(int(str(testowe[j])+str(testowe[kk]))) and check_prime(int(str(testowe[kk])+str(testowe[j])))
                                and check_prime(int(str(testowe[k])+str(testowe[kk]))) and check_prime(int(str(testowe[kk])+str(testowe[k])))):
                                    print("FOUND 4", i, j, k, kk)
                                    print("FOUND 4 val", testowe[i], testowe[j], testowe[k], testowe[kk])
                                    for kkk in range(kk+1, l):
                                        if (check_prime(int(str(testowe[i])+str(testowe[kkk]))) and check_prime(int(str(testowe[kkk])+str(testowe[i])))
                                and check_prime(int(str(testowe[j])+str(testowe[kkk]))) and check_prime(int(str(testowe[kkk])+str(testowe[j])))
                                and check_prime(int(str(testowe[k])+str(testowe[kkk]))) and check_prime(int(str(testowe[kkk])+str(testowe[k])))
                                and check_prime(int(str(testowe[kk])+str(testowe[kkk]))) and check_prime(int(str(testowe[kkk])+str(testowe[kk])))):
                                            print("FOUND ", i, j, k, kk, kkk)
                                            print("FOUND 5", testowe[i], testowe[j], testowe[k], testowe[kk], testowe[kkk])
