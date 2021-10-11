lst = []
num = int(input("Number of inputs:"))
for n in range (num):
    Ascii_val = ord(input())
    lst.append(Ascii_val)
print("The sum is :" ,sum(lst))