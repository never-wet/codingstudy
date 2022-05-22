prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
         31, 37, 41, 43, 47, 53, 59, 61, 67,
         71, 73, 79, 83, 89, 97, 101, 103, 107,
         109, 113, 127, 131, 137, 139, 149, 151,
         157, 163, 167, 173, 179, 181, 191, 193,
         197, 199, 211, 223, 227, 229, 233, 239,
         241, 251, 257, 263, 269, 271, 277, 281,
         283, 293]


number = input()
workingNumber = int(number)
rest = 0
foundFactor = False
factor = []

while (True):
    foundFactor = False

    for i in prime:
        if (workingNumber % i == 0):
            factor.append(i)
            workingNumber = workingNumber / i

            foundFactor = True
            break

    if foundFactor == False or workingNumber == 1:
        factor.append(workingNumber)
        break

for i in factor:
    if ( i != 1):
        print(i)


