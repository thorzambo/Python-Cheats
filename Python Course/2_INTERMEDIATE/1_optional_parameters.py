# Optional Parameners

def func(x=1):          # parameter = x, optional parameter =, in case you are missing the parameter once calling the function, it
      return x **2      # takes the preset one after =
      

call = func(5)
print(call)


# ----------------

def func1(word, freq=1):
      print(word*freq)

func1('Leo', )

# ----------------

def func1(word, add=5, freq=1):
      print(word*(freq + add))

func1('Leo', 5, 6)

# -----------------

class car(object):
      def __init__(self, make, model, year, condition='New', kms=0):
            self.make = make
            self.model = model
            self.year = year
            self.condition = condition
            self.kms = kms
      
      def display(self, showAll=True):
            if showAll:
                  print("this car is %s %s from %s, it %s and has %s kms" % (self.make, self.model, self.year, self.condition, self.kms))
            else:
                  print("this car is a %s %s from %s." % (self.make, self.model, self.year))
            
whip = car('Ford', 'Fusion', 2012)
whip.display()

