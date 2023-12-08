import pytest
from backend.main import _get_detail

class TestCase:

  @pytest.mark.asyncio
  async def test__get_detail(self) :
    detail = await _get_detail()
    assert detail == "detail-info"
