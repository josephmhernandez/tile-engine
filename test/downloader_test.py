import pytest   

# Note: Test Classes must start with "Test"
# Note: Test Functions must start with "test"

from engine.downloader import Downloader

class TestDowloader:
    
    def test_simple(self):
        assert (2 + 2 != 1)
