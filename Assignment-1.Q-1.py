#Write a Python program to get the Fibonacci series between 0 to 50

num = 9
n1, n2 = 1, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")
