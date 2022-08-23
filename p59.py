
data = ""

with open("p059_cipher.txt", "r") as file:
    data = file.read()
    data = data.split(",")


# 97 122
alpha = [chr(i) for i in range(97, 123)]
alpha_2 = [chr(i) for i in range(65, 91)]


# 101 120 112


print("SEARCHING...")
for i in range(97, 103):
    for j in range(97, 123):
        for k in range(97, 123):
            c = 0
            c_a = 0
            c_e = 0
            c_o = 0
            a = [i, j, k]

            for ii in data:
                if c == 3:
                    c = 0

                temp = chr(int(ii) ^ a[c])

                if temp == 'a':
                    c_a += 1
                elif temp == 'e':
                    c_e += 1
                elif temp == 'o':
                    c_o += 1
                c += 1
        
            l = len(data)
            c_a /= l
            c_e /= l
            c_o /= l

            if c_a < 0.1 and c_a > 0.03 and c_e < 0.16 and c_e > 0.09 and c_o < 0.12 and c_o > 0.04:
                print("FOUND ", i, j, k, c_a, c_e, c_o)


print("SEARCHING DONE")
c = 0
a = [101, 120, 112]
sum = 0

for i in data:
    if c == 3:
        c = 0

    print(chr(int(i) ^ a[c]), end="")
    sum += ord(chr(int(i) ^ a[c]))
    c += 1

print()
print(sum)
