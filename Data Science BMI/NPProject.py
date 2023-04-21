import numpy as np

def defar1():
    R,C = map(int, input("Enter no of rows and columns: ").split())
    listA = [list(map(int,input("Enter elements for row: ").split())) for i in range(R)]
    arr1 = np.array(listA)
    print ("Array #1 is ",arr1)

def defar2():
    R,C = map(int, input("Enter no of rows and columns: ").split())
    listA = [list(map(int,input("Enter elements for row: ").split())) for i in range(R)]
    arr2 = np.array(listA)
    print ("Array #2 is ",arr2)

while True:
    print ("""
    1. Add the arrays
    2. Subtract the arrays
    3. Multiply the arrays
    4. Divide the arrays
    5. Exit
    """)
    user = int(input("Enter number of choice: "))
    if user == 1:
        ar1 = defar1()
        ar2 = defar2()
        r1,c1 = ar1.shape
        r2,c2 = ar2.shape
        if r1 == r2 and c1 == c2:
            ar3 = ar1 + ar2
            print ("Sum of array 1 and array 2: \n",ar3)
        else:
            print ("Addition is not possible")
    elif user == 2:
        ar1 = defar1()
        ar2 = defar2()
        r1,c1 = ar1.shape
        r2,c2 = ar2.shape
        if r1 == r2 and c1 == c2:
            ar3 = ar1 - ar2
            print ("Difference of array 1 and array 2: \n",ar3)
        else:
            print ("Subtraction is not possible")
    elif user == 3:
        ar1 = defar1()
        ar2 = defar2()
        r1,c1 = ar1.shape
        r2,c2 = ar2.shape
        if r1 == r2 and c1 == c2:
            ar3 = ar1 * ar2
            print ("Product of array 1 and array 2: \n",ar3)
        else:
            print ("Multiplication is not possible")
    elif user == 4:
        ar1 = defar1()
        ar2 = defar2()
        r1,c1 = ar1.shape
        r2,c2 = ar2.shape
        if r1 == r2 and c1 == c2:
            ar3 = ar1/ar2
            print ("Quotient of array 1 and array 2: \n",ar3)
        else:
            print ("Division is not possible")
    elif user == 5:
        break