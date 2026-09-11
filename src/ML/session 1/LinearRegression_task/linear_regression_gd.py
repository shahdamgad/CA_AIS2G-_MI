import numpy as np
import matplotlib.pyplot as plt


class LinearRegressionGD:

    def __init__(self, learning_rate=0.001, n_iters=100):
        self.learning_rate = learning_rate
        self.n_iters = n_iters

        self.theta_0 = 0
        self.theta_1 = 0

        self.sse_values = []

    def fit(self, X, y):

        n = len(X)

        for i in range(self.n_iters):

            # Predictions
            y_pred = self.theta_0 + self.theta_1 * X

            # Gradients
            theta_0_derv = (2 / n) * np.sum(y_pred - y)
            theta_1_derv = (2 / n) * np.sum((y_pred - y) * X)

            # Update parameters
            self.theta_0 -= self.learning_rate * theta_0_derv
            self.theta_1 -= self.learning_rate * theta_1_derv

            # Calculate SSE
            sse = np.sum((y - y_pred) ** 2)
            self.sse_values.append(sse)

            if (i + 1) % 50 == 0:
                print(f"Iteration {i + 1}, SSE: {sse}")

    def predict(self, X):

        return self.theta_0 + self.theta_1 * X

    def mse(self, y_true, y_pred):
        return np.mean((y_true - y_pred) ** 2)

    def plot_training(self, X, y):

        # SSE over iterations
        plt.figure()
        plt.plot(range(1, self.n_iters + 1), self.sse_values)
        plt.xlabel("Iterations")
        plt.ylabel("SSE")
        plt.title("SSE over Iterations")
        plt.show()

        # Regression line
        plt.figure()
        plt.scatter(X, y)

        y_pred = self.predict(X)

        plt.plot(X, y_pred)

        plt.xlabel("House Size (m²)")
        plt.ylabel("House Price (thousands)")
        plt.title("Linear Regression")
        plt.show()