n1 = list(input('Insert the string: '))
n2 = list(input('Insert the  2nd string: '))
for j in range(len(n1)):

    n3 = []

    k = -j
    for _ in range(len(n2)):
        n3.append(n2[k])
        k += 1
    if n3 == n1:
        print('The first string is equal to the second string with', j, 'movements')
        break
if n3 != n1:
    print('The first string is not equal to the second string')
