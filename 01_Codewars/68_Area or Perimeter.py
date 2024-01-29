# You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
# If it is a square, return its area. If it is a rectangle, return its perimeter.


def area_or_perimeter(l , w):
    if l == w:
        return l**2
    return (l+w)*2