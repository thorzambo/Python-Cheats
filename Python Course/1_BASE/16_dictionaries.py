# dictionaries are key-value pairs

x = {'key': 'value', 'key2': 'value'} # keys MUST be always different

print(x)
print(x['key'])
x['key3'] = 5
print(x)
x['key2'] = 'valueChanged'
print(x)

# speed is constant time, hash collisions

#check if 
print('key' in x)
print(x.values())
print(x.keys())

#delete values and keys
del x['key']

# loop over

for key, value in x.items():
      print(key, value)
      

