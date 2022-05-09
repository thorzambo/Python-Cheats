# Unordered or ordered group of elements
caio = "ciao"
x = [4, True,'Ciao', "Ciao", caio, 4.3]
y = "hellooo"
# can store a bunch of diff elements
# [] list, ordered collection, order gets maintained

print(x)

print(len(x)) # length of str, elements inside it
print(len(y))

x.append(False)
print(x)
x.append(y)

x.extend([4,3,5,43,3,'fdsd'])
print(x)

x.remove(4)
print(x)

x.pop()
print(x)

x.pop(1) #gets index
print(x)

print(x[3]) # access by index

print(x.index('hellooo')) # gets index

x[0] = 'CHANGED'

print(x)


# TOUPLES
x = (0,9, "Ciao")
#touble is IMMUTABLE, list is MUTABLE
print(x[0])

'''x.append or pop or remove or stuff wont work'''
