from general import delta_x, delta_y, slope

point1 = {'x': 1, 'y': 1}
point2 = {'x': 3, 'y': 7}

delta_x = delta_x(point1, point2)
x = point1['x']
y = point1['y']

max_slope = slope(point1, point2) * 2

x_increment = 0.0001
increment_count = delta_x / x_increment

slope_increment = max_slope / increment_count

curr_slope = slope_increment

while curr_slope <= max_slope:
    x += x_increment
    y += curr_slope * x_increment

    curr_slope += slope_increment

print y
