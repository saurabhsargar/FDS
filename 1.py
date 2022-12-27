"""In second year computer engineering class, group A student’s play cricket, group B
students play badminton and group C students play football.
Write a Python program using functions to compute following: -
a) List of students who play both cricket and badminton
b) List of students who play either cricket or badminton but not both
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton."""

A = []
x = int(input("Enter number of students who play Cricket : "))
for i in range(0 , x):
    A.append(input("Name of students who play cricket : "))
print(A)

B = []
y = int(input("Enter the number of students who play badminton : "))
for j in range(0 , y):
    B.append(input("Name of students who play badminton : "))
print(B)

C = []
z = int(input("Enter the number of students who play football : "))
for k in range(0 , z):
    C.append(input("Name of students who play football : "))
print(C)

def AandB():
    AandB = []
    if(len(A) > len(B)):
        for i in range(x):
            for j in range(y):
                if(A[i] == B[j]):
                    AandB.append(A[i])
        print("Students who play cricket and badminton both : " , AandB)
    else:
        for j in range(y):
            for i in range(x):
                if(B[j] == A[i]):
                    AandB.append(B[j])
        print("Students who play cricket and badminton both : " , AandB)
    return AandB

def AorB():
    AorB = []
    for i in A:
        if i not in B:
            AorB.append(i)
    for j in B:
        if j not in A:
            AorB.append(j)
    print("Students who play either cricket or badminton but not both : " , AorB)

def onlyFB():
    onlyC = []
    for k in C:
        if(k not in A) and (k not in B):
            onlyC.append(k)
    if len(onlyC)>0:
        print(len(onlyC) , "Students play neither cricket nor badminton : ")
        print("list : " , onlyC)
    elif len(onlyC) == 0:
        print("Students who play only football , i.e-Neither cricket nor badminton")

def AandCnotB():
    AandCnotB = []
    AandCnotB = A+C
    AandCnotB = list(dict.fromkeys(AandCnotB))
    for j in B:
        if j in AandCnotB:
            AandCnotB.remove(j)
    print(len(AandCnotB) , "Students play cricket and football but not badminton")
    print("list : ", AandCnotB)

AandB()
AorB()
onlyFB()
AandCnotB()