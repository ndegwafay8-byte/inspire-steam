#Name : Faith
# Date : 

# program to perform arithmetic operation

f_number = 12 # first nymber
s_number = 34
sum_number = f_number + s_number
diff_number = f_number - s_number
product_number =  f_number * s_number
quotient_number = f_number / s_number

print("the sum of the number%d "%sum_number)
print("tthe quotient of the numbers %0.2f")

#modulas - remaider
print(7%3)

# even and odd numbers
for x in range(0,21):
    if( x%2 ==1 ):
        print(f"{x} is odd number")
    elif (x%2 == 0) :
        print(f"{x} is even number")
