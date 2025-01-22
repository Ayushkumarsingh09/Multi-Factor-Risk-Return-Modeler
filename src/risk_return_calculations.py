import numpy as np

class RiskReturnCalculations:
    @staticmethod
    def calculate_annualized_return(returns):
        """Calculate annualized return."""
        return np.mean(returns) * 252

    @staticmethod
    def calculate_volatility(returns):
        """Calculate annualized volatility."""
        return np.std(returns) * np.sqrt(252)

    @staticmethod
    def calculate_sharpe_ratio(returns, risk_free_rate):
        """Calculate Sharpe Ratio."""
        excess_returns = returns - risk_free_rate
        return np.mean(excess_returns) / np.std(excess_returns)
