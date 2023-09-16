import pytest
from unittest.mock import patch

@patch("sys.argv",["ffmpeg.py", "-text", "0:0 1:0,speed=3 2:0 3:0"])
def test_multispeed(regtest):
    with regtest:
        import ffmpeg