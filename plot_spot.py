from general import slope
from models import Point

def calc_point(target, point1=None, point2=None):
    """
    Generates  smooth curve of constant second derivative between two points.
    The point for the desired x value is returned.
    """
    dx = 1.0

    delta_x = point2.x - point1.x
    increment_count = delta_x / dx
    target_delta_x = target - point1.x

    max_slope = slope(point1, point2) * 2
    dm = max_slope / increment_count

    init_slope = 0

    avg_slope = (init_slope + dm*(target_delta_x/dx)) / 2

    x = target
    y = (target_delta_x * avg_slope) + point1.y
    result = Point(x, y)
    return (result.x, result.y)
