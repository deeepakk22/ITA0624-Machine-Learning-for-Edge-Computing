import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

X = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([1,4,9,16,25])

lin = LinearRegression().fit(X, y)

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
poly_reg = LinearRegression().fit(X_poly, y)

plt.scatter(X, y)
plt.plot(X, lin.predict(X), label="Linear")
plt.plot(X, poly_reg.predict(X_poly), label="Polynomial")
plt.legend()
plt.show()
