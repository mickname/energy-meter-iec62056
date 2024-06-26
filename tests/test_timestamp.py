from datetime import datetime

from iec62056.objects import timestamp

def test_normal_time() -> None:
    """Assert that timestamp parsing retuns a naive datetime ignoring the S/W flag."""
    assert timestamp('240330180410W') == datetime(2024, 3, 30, 18, 4, 10)

def test_summer_time() -> None:
    """Assert that timestamp parsing retuns a naive datetime ignoring the S/W flag."""
    assert timestamp('240625173400S') == datetime(2024, 6, 25, 17, 34, 00)
