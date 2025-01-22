import matplotlib.pyplot as plt

class Visualization:
    @staticmethod
    def plot_factor_exposures(factor_loadings):
        """Plots factor exposures as a bar chart."""
        factor_loadings.plot(kind='bar', figsize=(10, 6))
        plt.title("Factor Exposures")
        plt.xlabel("Factors")
        plt.ylabel("Loadings")
        plt.show()

    @staticmethod
    def plot_portfolio_risk_return(risks, returns):
        """Plots portfolio risk vs return."""
        plt.scatter(risks, returns, alpha=0.7)
        plt.title("Portfolio Risk vs Return")
        plt.xlabel("Risk (Volatility)")
        plt.ylabel("Return")
        plt.show()
