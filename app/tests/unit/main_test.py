# coding=utf-8

import pytest

from backend.main import get_root

class TestMain:

  def test_get_root(self):

    resp = get_root()

    assert resp == {"Hello":"World"}
