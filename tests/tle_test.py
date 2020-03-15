from perylune.tle import tle
import pytest

def test_tle_bad_init():

    with pytest.raises(TypeError):
        # without any strings
        tle()

    with pytest.raises(TypeError):
        # with just one line
        tle("1 25338U 98030A   19351.71640046 +.00000015 +00000-0 +24973-4 0  9993")

    with pytest.raises(TypeError):
        tle("NOAA-15",
            "1 25338U 98030A   19351.71640046 +.00000015 +00000-0 +24973-4 0  9993",
            "2 25338 098.7340 012.5392 0011411 075.8229 284.4218 14.25943731122932",
            "unsubstantiated nonsense")

def test_tle2lines():

    x = tle("1 25338U 98030A   19351.71640046 +.00000015 +00000-0 +24973-4 0  9993",
            "2 25338 098.7340 012.5392 0011411 075.8229 284.4218 14.25943731122932")
    assert x.name == ""
    assert x.line1 == "1 25338U 98030A   19351.71640046 +.00000015 +00000-0 +24973-4 0  9993"
    assert x.line2 == "2 25338 098.7340 012.5392 0011411 075.8229 284.4218 14.25943731122932"

def test_tle3lines():

    x = tle("1 25338U 98030A   19351.71640046 +.00000015 +00000-0 +24973-4 0  9993",
            "2 25338 098.7340 012.5392 0011411 075.8229 284.4218 14.25943731122932",
            "NOAA-15")
    assert x.name == "NOAA-15"
    assert x.line1 == "1 25338U 98030A   19351.71640046 +.00000015 +00000-0 +24973-4 0  9993"
    assert x.line2 == "2 25338 098.7340 012.5392 0011411 075.8229 284.4218 14.25943731122932"


def test_tle_parse():

    x = tle("1 25338U 98030A   19351.71640046 +.00000015 +00000-0 +24973-4 0  9993",
        "2 25338 098.7340 012.5392 0011411 075.8229 284.4218 14.25943731122932",
        "NOAA-15")

    assert x.norad == 25338