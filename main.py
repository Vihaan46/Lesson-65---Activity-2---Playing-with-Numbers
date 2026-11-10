num1 = int(input("Enter your largest number : "))
num2 = int(input("Enter Smallest number : "))

while (num2):
    numberstore = num2
    num2 = num1 % num2
    num1 = numberstore

print("HCF is :", num1)