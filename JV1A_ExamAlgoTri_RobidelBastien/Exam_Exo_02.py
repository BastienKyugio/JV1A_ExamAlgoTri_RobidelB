
def tri_a_bulle_unique_iteration(myTable):
    for i in range(len(myTable)-1):
        if myTable[i] > myTable[i+1]:
            myTable[i], myTable[i+1] = myTable[i+1], myTable[i]
    return myTable

print(tri_a_bulle_unique_iteration([84, 12, 3, 5, 78, 35, 2]))