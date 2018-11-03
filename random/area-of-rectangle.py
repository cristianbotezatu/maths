# inputs from the user
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# the semi-perimeter
sum = (a + b + c) / 2

# the area
area = (sum*(sum-a)*(sum-b)*(sum-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)
