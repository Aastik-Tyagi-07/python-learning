# Take a number from the user and print its digits one by one

n = int(input("Enter number:"))

while n >0:
    print(n%10)
    n = n // 10
    