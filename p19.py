days = [0, 0, 0, 0, 0, 0, 0]

d_m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 0

year = 1900
result = 0

while year < 2001:
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0 and year % 400 != 0:
            leap = False

    for i in range(12):
        temp = d_m[i]
        if i == 1 and leap:
            temp = 29

        for j in range(temp):
            if year > 1900:
                if j == 0 and day == 6:
                    result += 1
                days[day] += 1
            day += 1
            if day == 7:
                day = 0

    year += 1

print(days)
print(result)
