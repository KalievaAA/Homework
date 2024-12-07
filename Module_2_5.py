def code_1 ():
    code = int(input())
    return code

n = code_1()
list_1 = list(range(1, n))
list_2 = list(range(1, n))
pairs = []
result = ''

for i in list_1:
    for j in list_2:
        if i >= j:
            continue
        else:
            code_2 = n % (i + j)
            if code_2 == 0:
                pairs.append([i, j])
                result = result + str(i) + str(j)

print(result)

