def pattern1(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i,end="")
        print()


def pattern2(n):
    for i in range(1,n+1):
        for j in range(n,n-i,-1):
            print(j,end="")
        print()
print("Enter the number of rows for the patterns:")
n = int(input())

print("\nPattern 1:")
pattern1(n)

print("\nPattern 2:")
pattern2(n)
