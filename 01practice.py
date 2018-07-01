#
# Example of the Built-in Functions
#

# Prints from 0 to 100 and its binary form.
for i in range(0, 101):
    x = str(bin(i))
    print(i,x[2:])
