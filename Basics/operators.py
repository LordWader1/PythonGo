
# ==================================================
# 1. ARITHMETIC OPERATIONS IN PYTHON
# ==================================================

print("\n========== INTEGER OPERATIONS ==========")

# Addition
print("Addition:", 1 + 2)

# Subtraction
print("Subtraction:", 2 - 1)

# Multiplication
print("Multiplication:", 2 * 3)

# Division (always returns a float)
print("Division:", 4 / 2)
print("Division:", 6 / 2)
print("Division:", 7 / 2)

# Floor division (removes the decimal part)
print("Floor Division:", 7 // 2)
print("Floor Division:", 7 // 3)

# Modulus (returns the remainder)
print("Modulus:", 3 % 2)

# Exponentiation (power)
print("Exponentiation:", 3 ** 2)


# ==================================================
# 2. FLOATING-POINT NUMBERS
# ==================================================

print("\n========== FLOATING-POINT NUMBERS ==========")

pi = 3.14
gravity = 9.81

print("Value of PI:", pi)
print("Value of Gravity:", gravity)


# ==================================================
# 3. COMPLEX NUMBERS
# ==================================================

print("\n========== COMPLEX NUMBERS ==========")

complex_number = 1 + 1j
multiplication = (1 + 1j) * (1 - 1j)

print("Complex Number:", complex_number)
print("Complex Multiplication:", multiplication)


# ==================================================
# 4. USING VARIABLES IN ARITHMETIC OPERATIONS
# ==================================================

print("\n========== VARIABLE OPERATIONS ==========")

a = 3
b = 2

total = a + b
difference = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

print("a =", a)
print("b =", b)

print("Addition (a + b):", total)
print("Subtraction (a - b):", difference)
print("Multiplication (a * b):", product)
print("Division (a / b):", division)
print("Modulus (a % b):", remainder)
print("Floor Division (a // b):", floor_division)
print("Exponentiation (a ** b):", exponential)


# ==================================================
# 5. OPERATIONS USING num_one AND num_two
# ==================================================

print("\n========== NUMBER OPERATIONS ==========")

num_one = 3
num_two = 4

total = num_one + num_two
difference = num_two - num_one
product = num_one * num_two
division = num_two / num_one
remainder = num_two % num_one

print("Total:", total)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)


# ==================================================
# 6. AREA OF A CIRCLE
# ==================================================

print("\n========== AREA OF CIRCLE ==========")

radius = 10
pi = 3.14

area_of_circle = pi * radius ** 2

print("Radius:", radius)
print("Area of Circle:", area_of_circle)


# ==================================================
# 7. AREA OF A RECTANGLE
# ==================================================

print("\n========== AREA OF RECTANGLE ==========")

length = 10
width = 20

area_of_rectangle = length * width

print("Length:", length)
print("Width:", width)
print("Area of Rectangle:", area_of_rectangle)


# ==================================================
# 8. WEIGHT OF AN OBJECT
# ==================================================

print("\n========== WEIGHT CALCULATION ==========")

mass = 75
gravity = 9.81

weight = mass * gravity

print("Mass:", mass, "kg")
print("Gravity:", gravity, "m/s²")
print("Weight:", weight, "N")


# ==================================================
# 9. COMPARISON OPERATORS
# ==================================================

print("\n========== COMPARISON OPERATORS ==========")

print("3 > 2:", 3 > 2)
print("3 >= 2:", 3 >= 2)
print("3 < 2:", 3 < 2)
print("2 < 3:", 2 < 3)
print("2 <= 3:", 2 <= 3)
print("3 == 2:", 3 == 2)
print("3 != 2:", 3 != 2)


# ==================================================
# 10. STRING COMPARISONS USING len()
# ==================================================

print("\n========== STRING LENGTH COMPARISONS ==========")

print("mango == avocado:", len("mango") == len("avocado"))
print("mango != avocado:", len("mango") != len("avocado"))
print("mango < avocado:", len("mango") < len("avocado"))

print("milk != meat:", len("milk") != len("meat"))
print("milk == meat:", len("milk") == len("meat"))

print("tomato == potato:", len("tomato") == len("potato"))
print("python > dragon:", len("python") > len("dragon"))


# ==================================================
# 11. BOOLEAN OPERATIONS
# ==================================================

print("\n========== BOOLEAN OPERATIONS ==========")

print("True == True:", True == True)
print("True == False:", True == False)
print("False == False:", False == False)

print("True and True:", True and True)
print("True or False:", True or False)


# ==================================================
# 12. IDENTITY OPERATORS
# ==================================================

print("\n========== IDENTITY OPERATORS ==========")

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a is b:", a is b)
print("a is c:", a is c)
print("a is not c:", a is not c)

# is checks whether two variables refer to the same object.


# ==================================================
# 13. MEMBERSHIP OPERATORS
# ==================================================

print("\n========== MEMBERSHIP OPERATORS ==========")

print("'A' in 'Asabeneh':", 'A' in 'Asabeneh')
print("'B' in 'Asabeneh':", 'B' in 'Asabeneh')

print("'coding' in 'coding for all':",
      'coding' in 'coding for all')

print("'a' in 'an':", 'a' in 'an')


# ==================================================
# 14. LOGICAL OPERATORS
# ==================================================

print("\n========== LOGICAL OPERATORS ==========")

# AND: True only when both conditions are True.

print("3 > 2 and 4 > 3:", 3 > 2 and 4 > 3)
print("3 > 2 and 4 < 3:", 3 > 2 and 4 < 3)
print("3 < 2 and 4 < 3:", 3 < 2 and 4 < 3)

# OR: True when at least one condition is True.

print("3 > 2 or 4 > 3:", 3 > 2 or 4 > 3)
print("3 > 2 or 4 < 3:", 3 > 2 or 4 < 3)
print("3 < 2 or 4 < 3:", 3 < 2 or 4 < 3)

# NOT: Reverses the Boolean result.

print("not (3 > 2):", not (3 > 2))
print("not True:", not True)
print("not False:", not False)
print("not not True:", not not True)
print("not not False:", not not False)
