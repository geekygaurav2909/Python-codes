import colorgram

colors = colorgram.extract('images.jpg',2 ** 32)
color_code = []

for index_pos in range(len(colors)):
    first_color = colors[index_pos]
    rgb = first_color.rgb
    r =rgb[0]
    g= rgb[1]
    b = rgb[2]
    final_code = (r,g,b)
    color_code.append(final_code)

print(color_code)