# x=10            # integer
# y=10.2          # float
# z=("Hello")     # string

    # Implicit type conversion

# x=x*y
# x=x+y

# print(x)

# print(x, "Type of x is:", type(x))

    # Explicit type conversion
# age=input("What is your age? ")
# print(type(age))  # class--'str'

    # Name
name=input("What is your name? ")
print(name, type(str(name)))

age=input("What is your age? ")
# # age=int(age)   # "OR"
# # print(type(age))   # "OR"
# # print(type(int(age)))
#         # To Print AGE
# # print(age, type(int(age)))
# # print(age, type(str(age)))
print(age, type(float(age)))
