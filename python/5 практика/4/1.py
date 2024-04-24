from deal import pre, post, ensure, raises

@pre(lambda x1, y1, x2, y2: isinstance(x1, (int, float)) and isinstance(y1, (int, float)) and isinstance(x2, (int, float)) and isinstance(y2, (int, float)))
@post(lambda result: isinstance(result, (int, float)))
@ensure(lambda x1, y1, x2, y2, result: result >= 0)
@raises(ValueError)
def distance(x1, y1, x2, y2):
    if not isinstance(x1, (int, float)) or not isinstance(y1, (int, float)) or not isinstance(x2, (int, float)) or not isinstance(y2, (int, float)):
        raise ValueError("Coordinates must be numeric")
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
