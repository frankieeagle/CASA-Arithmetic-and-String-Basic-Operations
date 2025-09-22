# Do not forget to change values for the variables fruit and s
# Do not forget to comment out the lines of code that will trigger Type and Index errors.

# Chapter 6.1 "A string is a sequence" code
foods = 'banana'
letter = foods[1]
print(letter)

letter = foods[0]
print(letter)

#letter = foods[1.5]


# Chapter 6.2 "Getting the length of a string using len" code
foods = 'banana'
print(len(foods))

length = len(foods)
# last = foods[length]

last = foods[length-1]
print(last)


# Chapter 6.3 "Traverse through a string with a loop" code
index = 0
while index < len(foods):
    letter = foods[index]
    print(letter)
    index = index + 1


# Chapter 6.4 "String Slices" code
for char in foods:
    print(char)

g = 'Monty Python'
print(g[0:5])

print(g[6:12])

foods = 'banana'
print(foods[:3])
print(foods[3:])

foods = 'banana'
print(foods[3:3])

print(foods[:]) #prints from beginning to end


