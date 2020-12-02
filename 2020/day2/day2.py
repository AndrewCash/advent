f = open('input', 'r+')
input_data = f.read().splitlines()
f.close


def checkPassword(password, part):
    
    split = password.partition(": ")
    constraint = split[0]
    passwd = split[2]

    splitConstraint = constraint.partition(" ")

    letterTarget = splitConstraint[2]
    lower = int(splitConstraint[0].partition("-")[0])
    upper = int(splitConstraint[0].partition("-")[2])

    # Part 1
    if (part == 1):
        if (lower <= passwd.count(letterTarget) <= upper):
            # print("Password is good")
            return True
        else: 
            # print("Password is no good.")
            return False

    # Part 2
    if (part == 2):
        if ((passwd[lower - 1] == letterTarget) ^ (passwd[upper - 1] == letterTarget)):
            #print("Password is good")
            return True
        else: 
            #print("Password is no good.")
            return False


validPasswords = 0
for psswd in input_data:
    if checkPassword(psswd, 1):
        validPasswords += 1
print ("Part 1: " + str(validPasswords))

validPasswords = 0
for psswd in input_data:
    if checkPassword(psswd, 2):
        validPasswords += 1
print("Part 2: " + str(validPasswords))
