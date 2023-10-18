
def tri_a_bulle(myTable):
    for j in range(len(myTable)):
        for i in range(len(myTable)-1):
            if myTable[i] > myTable[i+1]:
                myTable[i], myTable[i+1] = myTable[i+1], myTable[i]
    return myTable

print(tri_a_bulle([84, 12, 3, 5, 78, 35, 2]))

