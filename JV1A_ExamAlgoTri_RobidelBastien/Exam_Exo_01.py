def permuter(myTable, i, j):
    myTable[i], myTable[j] = myTable[j], myTable[i]
    return myTable

print(permuter([84, 12, 3, 5, 78, 35, 2], 4, 3))
