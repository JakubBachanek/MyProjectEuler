MAX = 13*26

data = ""

with open("p042_words.txt", "r") as file:
    data = file.read()
    data = data.replace("\"", "")
    data = data.split(",")


t_nums = [1]
n = 2

while t_nums[-1] < MAX:
    t_nums.append((n*(n+1))//2)
    n += 1


result = 0

for word in data:
    value = 0
    for letter in word:
        value += ord(letter)-64

    for val in t_nums:
        if value == val:
            result += 1
            break


print(result)
