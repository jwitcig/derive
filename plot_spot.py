from general import calc_slope
from models import Point

def calc_value(target, point1, point2, init_slope=0):
    """
    Generates smooth curve of constant second derivative between two points.
    The point for the desired x value is returned.
    """
    delta_x = point2.x - point1.x
    target_delta_x = target - point1.x

    avg_slope = calc_slope(point1, point2)
    slope_diff = 2*avg_slope - init_slope

    target_slope = slope_diff * (target_delta_x / delta_x) + init_slope

    avg_slope_target = target_slope / 2

    x = target
    y = (target_delta_x * avg_slope_target) + point1.y
    return Point(x, y)

def final_slope(point1, point2, init_slope=0):
    avg_slope = calc_slope(point1, point2)
    return (2 * avg_slope) - init_slope

def calc_point(target, points):
    points = sort_points(points)

    init_slope = 0
    for i, point in points:
        if i == len(points)-1: continue
        left_point = point
        right_point = points[i+1]

        if left_point.x < target < right_+point.x:
            calc_value(target, left_point, right_point, init_slope)




def sort_points(points):
    return sorted(points, key=lambda x: x.x)
