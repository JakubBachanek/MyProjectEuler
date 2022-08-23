import math

p_nums = [(n*(3*n-1))//2 for n in range(1, 5000)]

def check_num_p(n):
    temp = (1+math.sqrt(1+24*n))/6
#    print(temp)

    t = int(temp)

    if temp - t > 0:
#        print(n, False)
        return False

#    print(n, True)
    return True

def check_num(v, s, e):
    for i in range(s, e):
        if v == p_nums[i]:
            return True

    return False


result = p_nums[-1]



for i in range(1, len(p_nums)):
    for j in range(i, -1, -1):
        test = True
        val_1 = p_nums[i] - p_nums[j]
        test = check_num_p(val_1)

        if not test:
            continue

        val_2 = p_nums[i] + p_nums[j]
        test = check_num_p(val_2)

        if test:
            print("*** ------", i, j, p_nums[i], p_nums[j]) 
            if val_1 < result:
                result = val_1

print(result)
