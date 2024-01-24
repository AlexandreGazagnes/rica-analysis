import pytest

from rica_analysis.core import RicaAnalysis




class TestCore:
    """Unit tests"""

    def test_core(self):
        """Unit test"""

        rica_analysis = RicaAnalysis()
        assert isinstance(rica_analysis, RicaAnalysis)  