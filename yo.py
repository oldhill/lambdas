# Some basic lambda exploration

def add_two(x):
  return x + 2

add_two_lambda = lambda x: x + 2

print add_two(1)
print add_two_lambda(1)
print (lambda x: x + 2)(1)
print (lambda: 3)()
