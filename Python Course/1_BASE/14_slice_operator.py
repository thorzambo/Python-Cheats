x = [0,1,2,3,4,5,6,7,8,9,10]
y = ['hhi', 'hello', 'ciao', 'cime', 'thor', 'Thor', 'Leo']
s = "Leo"

# slice also work with touples

#sliced = x[start:stop:step]
sliced = x[0:8:2] # 8 is excluded, step means jump
sliced_stop = x[:4] # stop at pos 4
sliced_start = x[4:] # start at 4
sliced_reversed = x[::-1] # step 1 reverse
sliced_diff = x[::2] # step all by 2

# printing
print('sliced:', end = ' ')
print(sliced)
print('\nsliced_stop:', end = ' ')
print(sliced_stop)
print('\nsliced_start:', end = ' ')
print(sliced_start)
print('\nsliced_reversed:', end = ' ')
print(sliced_reversed)
print('\nsliced_diff:', end = ' ')
print(sliced_diff)
