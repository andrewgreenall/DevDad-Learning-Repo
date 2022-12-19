"""Array file"""

names = ['Andrew', 'Dad', 'John', 'Jack']
# display orginal list
print(names)

# alter John to Jon
names[2] = 'Jon'
print(names)

# show first
print(names[1])

# show last
print(names[-1])

# show first and second
print(names[0:2])

# add Sue to the end
names.append('Sue')

# insert Katie at the beginning
names.insert(0, 'Katie')
print(names)

# is Dad in the list
print('is Dad in the list? ', 'Dad' in names)

# how many are in the list
print(len(names))
