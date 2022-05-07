# for larger operations:

x = 8
y = 9
z = 10

r1 = x == y
r2 = y > x
r3 = z < x < y

final_result = r1 or not r2 and r3

print(final_result)

print(not(final_result))

print(not (False and True))

print(False and True)

# first get valuated and then or

print(True and False or False)
