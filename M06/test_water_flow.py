from water_flow import water_column_height
from pytest import approx
import pytest

def test_water_column_height(water_column_height):
    assert water_column_height(0,0) == approx(0)
    assert water_column_height(0,10) == approx(7.5)
    assert water_column_height(25,0) == approx(25)
    assert water_column_height(48.3, 12.8) == approx(57.9)
pytest.main(["-v", "--tb=line", "-rN", __file__])