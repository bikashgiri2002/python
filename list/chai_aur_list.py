tea_varities = ["Black", "Green", "Oolong", "White"]
print(tea_varities)
# ['Black', 'Green', 'Oolong', 'White']
# tea_varities[5] = "Suger"

# Error
# Traceback (most recent call last):
#   File "<pyshell#2>", line 1, in <module>
#     tea_varities[5] = "Suger"
# IndexError: list assignment index out of range

tea_varities[1:2] = ["Lamon"]
print(tea_varities)
# ['Black', 'Lamon', 'Oolong', 'White']
tea_varities = ["Black", "Loman", "Green", "Oolong", "White"]
print(tea_varities)
# ['Black', 'Loman', 'Green', 'Oolong', 'White']
tea_varities[1:2] = ["Lamon"]
print(tea_varities)
# ['Black', 'Lamon', 'Green', 'Oolong', 'White']
tea_varities[1:1] = ["Test", 'test']
print(tea_varities)
# ['Black', 'Test', 'test', 'Lamon', 'Green', 'Oolong', 'White']
tea_varities[1:1] = []
print(tea_varities)
# ['Black', 'Test', 'test', 'Lamon', 'Green', 'Oolong', 'White']
tea_varities[1:3] = []
print(tea_varities)
# ['Black', 'Lamon', 'Green', 'Oolong', 'White']