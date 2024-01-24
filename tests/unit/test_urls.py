import pytest

from rica_analysis.etl.urls import Urls


class TestUrls:
    """Unit tests"""

    def test_urls(self):
        """Unit test"""

        url_0 = Urls.main
        assert isinstance(url_0, str)

        url_1 = Urls.history    
        assert isinstance(url_1, str)