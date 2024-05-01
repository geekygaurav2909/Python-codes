# from turtle import *

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# forward(100)
# left(120)
# forward(100)
# left(120)
# forward(100)

# timmy.color("red","blue")

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import *

table = PrettyTable()

table.field_names = ["City Name", "Area", "Population", "Annual Rainfall"]
table.add_rows(
    [
        ['New York', 1295, 653257,660.50],
        ['Japan',1244,215400,412.5],
        ['Mumbai',400001,1441175,895.2],
        ['Varanasi',221103,778433,565.7]
    ]
)

# table.del_row(2) # deletes row starts from index 0
# table.del_column("Population") # deletes the particular column
# table.align["City Name"] = "l"
# table.align["Annual Rainfall"] = "r"

# print(table.get_string(sortby="Population"))

table.sortby="Annual Rainfall"


print(table)


