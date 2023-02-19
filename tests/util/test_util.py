# coding:utf-8
import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../src'))
from util import util


def test_changeTimeZone():
    input = "2023-01-07T08:12:27+00:00"
    success = "2023年1月7日 17:12:27"
    assert success == util.changeTimeZone(input)

def test_changeTimeZone2():
    input = "2023-01-07T21:09:01+00:00"
    success = "2023年1月8日 06:09:01"
    assert success == util.changeTimeZone(input)

def test_changeTimeZone2():
    input = "2023-01-0721:09:01+00:00"
    
    with pytest.raises(ValueError) as e:
        util.changeTimeZone(input)

if __name__ == "__main__":
    unittest.main()
