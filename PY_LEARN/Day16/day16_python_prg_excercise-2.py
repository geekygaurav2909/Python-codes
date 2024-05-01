from prettytable import *

table = PrettyTable()
# Surprisignly, we are doing it in three ways
# Way - 1  

# table.field_names = ["Pokemon Name", "Type"]
# table.add_rows(
#     [
#         ["Pikachu","Electric"],
#         ["Squirtle","Water"],
#         ["Charmander", "Fire"]
#     ]
# )

#Way 2
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

table.align = "l"

#Way 3
# table.add_row(["Gaurav","Anjula"])
print(table)