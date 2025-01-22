import unittest
import numpy as np
from src.risk_return_calculations import RiskReturnCalculations

class TestRiskReturnCalculations(unittest.TestCase):
    def setUp(self):
        self.returns = np.array([0.01, 0.02, 0.015])
        self.risk_free = 0.005

    def test_calculate_annualized_return(self):
        result = RiskReturnCalculations.calculate_annualized_return(self.returns)
        self.assertGreater(result, 0, "Annualized return should be positive")

    def test_calculate_volatility(self):
        result = RiskReturnCalculations.calculate_volatility(self.returns)
        self.assertGreater(result, 0, "Volatility should be positive")

    def test_calculate_sharpe_ratio(self):
        result = RiskReturnCalculations.calculate_sharpe_ratio(self.returns, self.risk_free)
        self.assertGreater(result, 0, "Sharpe ratio should be positive")

if __name__ == '__main__':
    unittest.main()
