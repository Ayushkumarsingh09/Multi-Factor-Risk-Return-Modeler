import statsmodels.api as sm

class RegressionAnalysis:
    def __init__(self, data, dependent_var, independent_vars):
        self.data = data
        self.dependent_var = dependent_var
        self.independent_vars = independent_vars

    def perform_regression(self):
        """Performs multi-factor regression."""
        X = self.data[self.independent_vars]
        y = self.data[self.dependent_var]
        X = sm.add_constant(X)  # Add intercept
        model = sm.OLS(y, X).fit()
        print(model.summary())
        return model
