# * 
# * * 
# * * * 
# * * * * 
# * * * * *

for i in range(1, 6) :
    print("* " * i)

# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(5, 0, -1):
    print("* " * i)



#     *
#    ***
#   *****
#  *******
# *********

# Number of rows
rows = 5

# Loop to print the pattern
for i in range(rows):
    # Printing spaces
    print(' ' * (rows - i - 1), end='')
    # Printing asterisks
    print('*' * (2 * i + 1))
