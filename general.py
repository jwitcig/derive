def slope(point1, point2):
    delta_x = point2.x - point1.x
    delta_y = point2.y - point1.y
    return float(delta_y) / float(delta_x)
