data = []

with open("p022_names.txt", "r") as file:
    data = file.read()

data = data.replace("\"", "")
data = data.split(",")
data = sorted(data)

result = 0

for i in range(len(data)):
    value = 0

    for char in data[i]:
        value += ord(char) - 64

    score = (i+1) * value
    result += score

print(result)
