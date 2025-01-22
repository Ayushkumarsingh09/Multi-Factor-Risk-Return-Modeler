class Utils:
    @staticmethod
    def calculate_excess_returns(data, market_col, risk_free_col):
        """Utility function to calculate excess returns."""
        data['Excess_Returns'] = data[market_col] - data[risk_free_col]
        return data
