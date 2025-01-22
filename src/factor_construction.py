import pandas as pd

class FactorConstruction:
    def __init__(self, data):
        self.data = data

    def construct_market_factor(self, market_index_col):
        """Construct market excess returns factor."""
        self.data['Market_Excess'] = self.data[market_index_col] - self.data['RiskFree']
        return self.data

    def construct_smb_hml(self):
        """Construct SMB (Small Minus Big) and HML (High Minus Low) factors."""
        self.data['SMB'] = (self.data['SmallCap'] - self.data['LargeCap']) / 2
        self.data['HML'] = (self.data['Value'] - self.data['Growth']) / 2
        return self.data
