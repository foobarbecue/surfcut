from unittest.mock import patch

def test_multispeed_strinp(regtest):
    with regtest, patch("sys.argv",["ffmpeg.py", "-text", "0:0 1:0,speed=3 2:0 3:0"]):
        import ffmpeg

def test_multispeed_fileinp(regtest, shared_datadir):
    with patch("sys.argv",["ffmpeg.py", "-file", str(shared_datadir/"trim1.txt")]):
        with regtest:
            import ffmpeg