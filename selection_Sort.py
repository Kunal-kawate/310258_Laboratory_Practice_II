'''
Implement Greedy search algorithm for any of the following application:
- Selection Sort
'''


array=[6,3,1,4,2,9,7,8,0,5]

print(array)

for i in range(len(array)):
    min_index=i
    for j in range(i+1,len(array)):
        if array[j]<array[i]:
            min_index=j
            temp= array[j]
            array[j]=array[i]
            array[i]=temp

print(array)