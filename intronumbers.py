num1 = 3
num2 = 1.23


print(num1)
print(type(num1))
print(type(num2))


#arithmetic Operators:
#   Addition        3 + 2
#   subtraction     3 - 2
#   multiplcation   3 * 2
#   division        3 / 2
#   floor dvision   3 // 2      antallet af gange divisionen går helt op
#   exponent        3 ** 2
#   modulus         3 % 2       antallet tilbage efter mulige hele divisioner

print(num1**num1)

#Order of operations can be used with parentheses

print(3 * 2 + 1)
print(3 * (2 + 1))


# increment values can be done by += 1

print(num1)
num1 += 1
print(num1)

num1 *= 10
print(num1)


#absolute value function

print(abs(-10))

print(round(num2))

# anden parameter bestemmer antal decimal der skal afrundes med
print(round(num2, 1))


# double equal sign is comparison
print(num1 == num2)

print(num1 != num2)

print(num1 < num2)

print(num1 > num2)


s_num_1 = '100'
s_num_2 = '200'

print(s_num_1 + s_num_2)
#casting can be done

s_num_1 = int(s_num_1)
s_num_2 = int(s_num_2)

print(s_num_1 + s_num_2)
