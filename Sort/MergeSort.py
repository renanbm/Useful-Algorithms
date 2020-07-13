def MergeSort(list):
    n = len(list)
    if n < 2:
        return
    mid = n//2
    lefthalf = list[:mid]
    righthalf = list[mid:]
    MergeSort(lefthalf)
    MergeSort(righthalf)

    nL = len(lefthalf)
    nR = len(righthalf)

    i = 0
    j = 0
    k = 0

    while i < nL and j < nR:
        if lefthalf[i] <= righthalf[j]:
            list[k] = lefthalf[i]
            i += 1
        else:
            list[k] = righthalf[j]
            j += 1
        k += 1

    while i < nL:
        list[k] = lefthalf[i]
        k += 1
        i += 1

    while j < nR:
        list[k] = righthalf[j]
        k += 1
        j += 1

Numbers = [5, 4, 6, 7, 10, 2, 9, 3, 8, 1, 0]
MergeSort(Numbers)
print(Numbers)