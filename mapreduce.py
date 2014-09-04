# Looking at basic usage of python map() and reduce(), and alternative comprehensions

my_list = [1, 2, 3, 4, 5]

# map

print map(lambda x: x + 1, my_list)
print map(lambda x: 'hello', my_list)

print [x + 1 for x in my_list]
print ['hello' for x in my_list]

# reduce

print reduce(lambda x, y: x + y, my_list)

# whoa, filter?

print filter(lambda x: x > 2, my_list)
print [x for x in my_list if x > 2]
