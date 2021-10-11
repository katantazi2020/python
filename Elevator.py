import math
n = 4
p = 5
num_courses = n / p
if n % p != 0 :
 rounded_val = math.ceil(num_courses )
 print(rounded_val)
elif n % p == 0:
    print(num_courses)
