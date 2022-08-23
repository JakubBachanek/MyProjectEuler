MAX = 50

def check_palindrome(n):
    return str(n) == str(n)[::-1]

result = 0

for i in range(1, 10000):
    s = str(i)
    counter = 0
    palindrome = False

    while counter < MAX:
        temp = int(s) + int(s[::-1])

        if check_palindrome(temp):
            palindrome = True
            break

        s = str(temp)
        counter += 1

    if not palindrome:
        result += 1


print(result)
