NUM = 1000

w_1 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
w_2 = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
w_3 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
w_4 = ["hundred", "thousand"]
result = 0


for i in range(1, NUM+1):
    print(i)
    temp = []
    a = i % 100
    if a > 9 and a < 20:
        temp.append(w_2[a-10])
    elif a >= 20:
        b = a % 10
        if b > 0:
            temp.append(w_1[b-1])

        b = a // 10
        temp.append(w_3[b-2])
    elif a > 0:
        temp.append(w_1[a-1])

    a = i // 100

    if a < 10 and a > 0:
        if temp != []:
            temp.append("and")
        temp.append(w_1[a-1] + " " + w_4[0])
    a = a // 10

    if a == 1:
        temp.append(w_1[a-1] + " " + w_4[1])

    print(temp[::-1])
    print()

    for j in temp:
        result += len(j.replace(" ", ""))

print()
print(result)
