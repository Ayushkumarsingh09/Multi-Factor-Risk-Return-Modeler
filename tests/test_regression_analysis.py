import unittest
import pandas as pd
from src.regression_analysis import RegressionAnalysis

class TestRegressionAnalysis(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            "Market_Excess": [0.02, 0.03, 0.01],
            "SMB": [0.01, 0.02, 0.01],
            "HML": [0.03, 0.04, 0.02],
            "AssetReturns": [0.04, 0.05, 0.03]
        })

    def test_perform_regression(self):
        regression = RegressionAnalysis(self.data, "AssetReturns", ["Market_Excess", "SMB", "HML"])
        model = regression.perform_regression()
        self.assertIsNotNone(model, "Regression model should not be None")

if __name__ == '__main__':
    unittest.main()
