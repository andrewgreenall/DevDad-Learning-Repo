# if statement
dayNo = int(input("enter a day of the month: "))

if dayNo > 31 or dayNo < 1:
    print('this is not a day of a month')
else:
    print(dayNo, " is a day of the month")

# looping

# while loop

i = 1
while i <= 1_001:
    print("i is currently: ", i)
    i = i+1

# For loop

numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item)

# while alternative

i = 0
while i < len(numbers):
    print(numbers[i], end=',')
    i = i + 1
    