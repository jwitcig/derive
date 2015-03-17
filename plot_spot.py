from general import slope
from models import Point

def calc_point(target, point1=None, point2=None):
    """
    Generates smooth curve of constant second derivative between two points.
    The point for the desired x value is returned.
    """
    delta_x = point2.x - point1.x
    target_delta_x = target - point1.x

    max_slope = slope(point1, point2) * 2

    target_slope = ((target_delta_x / delta_x) * max_slope)
    avg_slope = target_slope / 2

    x = target
    y = (target_delta_x * avg_slope) + point1.y
    return Point(x, y)
