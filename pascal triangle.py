arr=[[1]]
for i in range(1,6):
    arr.append([])
    arr[i].append(1)
    for index,value in enumerate(arr[i-1]):
        if index!=len(arr[i-1])-1:
            arr[i].append(arr[i-1][index]+arr[i-1][index+1])
    arr[i].append(1)
for val1 in arr:
    for val2 in val1:
        print(val2,end=" ")
    print()