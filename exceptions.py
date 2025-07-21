#Errors and Exceptions


class ValueTooHighError(Exception):
    """Raised when the input value is too high."""
    pass

class ValueTooSmallError(Exception):
    """Raised when the input value is too small."""
def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooSmallError('value is too small')

try:
    test_value(1) 
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e)