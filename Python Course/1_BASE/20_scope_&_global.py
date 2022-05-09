# Bad to use, but this exhists

x = 'Leo'

def func(name):
      global x
      x = name


print(x)

func('Changed')

print(x)
