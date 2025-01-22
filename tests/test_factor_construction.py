import unittest
import pandas as pd
from src.factor_construction import FactorConstruction

class TestFactorConstruction(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            "MarketIndex": [0.02, 0.03, 0.01],
            "RiskFree": [0.01, 0.01, 0.01],
            "SmallCap": [0.03, 0.04, 0.02],
            "LargeCap": [0.02, 0.03, 0.01],
            "Value": [0.05, 0.06, 0.04],
            "Growth": [0.02, 0.03, 0.01]
        })

    def test_construct_market_factor(self):
        constructor = FactorConstruction(self.data)
        result = constructor.construct_market_factor("MarketIndex")
        self.assertIn("Market_Excess", result.columns)

    def test_construct_smb_hml(self):
        constructor = FactorConstruction(self.data)
        result = constructor.construct_smb_hml()
        self.assertIn("SMB", result.columns)
        self.assertIn("HML", result.columns)

if __name__ == '__main__':
    unittest.main()
