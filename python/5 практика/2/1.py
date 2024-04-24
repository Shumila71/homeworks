def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

import pytest

@pytest.mark.parametrize("x1, y1, x2, y2, expected", [
    (0, 0, 3, 4, 5.0),
    (0, 0, 0, 0, 0.0),
    (1, 1, 1, 1, 0.0)
])
def test_distance( x1, y1, x2, y2, expected):
    assert distance(x1, y1, x2, y2) == expected