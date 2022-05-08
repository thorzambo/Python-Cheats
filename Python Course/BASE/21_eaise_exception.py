#raise Exception('Bad') # Java is throw exception -> uncomment to test

# to raise exception
# for handling that, we will need to catch the exception, in Python is Try, Except, Finally. In Java is Try catch


try: 
      x = 7 / 0
except Exception as e:
      print(e)
finally:
      print('finally')

# test without it:
x = 7 / 0

