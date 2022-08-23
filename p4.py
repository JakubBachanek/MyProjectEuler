
def check_palindrome(num):
    return str(num) == str(num)[::-1]

result = 0


for i in range(100, 1000):
    for j in range(100, 1000):
        temp = i * j

        if check_palindrome(temp):
            if temp > result:
                result = temp

print(result)
