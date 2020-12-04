f = open('input', 'r+')
input_data = f.read().splitlines()
f.close


def countTree(right, down):
    tree_count = 0
    x = 0
    y = 0
    for index, line in enumerate(input_data):

        if (index == y):

            if (line[x % 31] == "#"):
                tree_count += 1
            
            x += right
            y += down

    return tree_count


product = 1

count = countTree(1, 1)
product *= countTree(1, 1)
print ("R1, D1 Tree Count : ", count) 

count = countTree(3, 1)
product *= countTree(3, 1)
print ("R3, D1 Tree Count : ", count) # Should return 252, Part 1

count = countTree(5, 1)
product *= countTree(5, 1)
print ("R5, D1 Tree Count : ", count) 

count = countTree(7, 1)
product *= countTree(7, 1)
print ("R7, D1 Tree Count : ", count)

count = countTree(1, 2)
product *= countTree(1, 2)
print ("R1, D2 Tree Count : ", count) 


print ("Product of each slope: ", product)

