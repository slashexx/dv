import numpy as np
import matplotlib.pyplot as plt

discount = np.array([10, 20, 30, 40, 50])

sales = np.array([100, 200, 300, 400, 500])

size = discount * 10


plt.scatter(discount, sales, s=size, color="red", linewidths=3, marker="*", edgecolors="blue")

plt.title("Discount vs Sales")

plt.xlabel("Discount")
plt.ylabel("Sales")

plt.show()