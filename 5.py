"""Write a python program to store second year percentage of students in array. Write
function for sorting array of floating point numbers in ascending order using
a) Insertion sort
b) Shell Sort and display top five scores"""

def insertsort(arr, n):
    i = 1
    for i in range(n):
        temp = arr[i]
        j = i - 1
        while((j >= 0) and (arr[j] > temp)):
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = temp
    print(arr)
    print("Top five Scores are: ")
    for i in range(len(arr)-1, 1, -1):
        print(arr[i])

def shellsort(arr, n):
    d = n // 2
    while(d > 0):
        for i in range(d, n):
            temp = arr[i]
            j = 1
            while(j>= d and arr[i-d] > temp):
                arr[j] = arr[j-d]
                j -= d
            arr[j] = temp
        d = d // 2
    print(arr)
    print("Top five scores are: ")
    for i in range(len(arr)-1, 1, -1):
        print(arr[i])

# Driver Code
n = int(input("How many student are there: "))
arr = []
i = 0
for i in range(n):
    item = float(input("Enter percentage marks: "))
    arr.append(item)

print("You have entered percentage are: ", arr)
while(True):
    print("*********** Menu ***********")
    print("1. Insertion Sort.")
    print("2. Shell Sort.")
    print("3. Exit.")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("The sorted scores using insertion sort are: ")
        insertsort(arr, n)
    
    elif choice == 2:
        print("The sorted scores using shell sort are: ")
        shellsort(arr, n)
    
    else:
        print("Exit.")
        exit()