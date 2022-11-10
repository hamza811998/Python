# while and for loops
# while loops



# while loops


# x=0
# while (x<5):
#     print(x)
#     x=x+1

# x=0
# while (x<=5):
#     print(x)
#     x=x+1


# for loops

# for y in range(4,11):
#     print(y)

# array
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# for d in days:
#     print(d)

for d in days:
    # if (d=="Fri"):break # Loop stops
    if (d=="Fri"): continue # Skips d
    print(d)
