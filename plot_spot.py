from general import calc_slope
from models import Point

def calc_point(target, point1=None, point2=None, init_slope=0):
    """
    Generates smooth curve of constant second derivative between two points.
    The point for the desired x value is returned.
    """
    delta_x = point2.x - point1.x
    target_delta_x = target - point1.x

    slope_diff = max_slope - init_slope

    target_slope = slope_diff * (target_delta_x / delta_x) + init_slope

    avg_slope = target_slope / 2

    x = target
    y = (target_delta_x * avg_slope) + point1.y
    return Point(x, y)
