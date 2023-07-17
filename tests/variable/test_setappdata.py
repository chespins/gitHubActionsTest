# coding:utf-8
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '../../src'))
from variable.setappdata import AppCommonData


def test_checkVersion():
    test_obj = AppCommonData()
    test_obj.dbFileVersion = "v0.8"
    assert test_obj.checkRankingData()

