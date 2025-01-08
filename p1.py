import matplotlib.pyplot as plt
import numpy as np

date = ["12/1", "12/2", "12/3", "12/4", "12/5"]
temp = [60, 70, 65, 75, 80]

plt.plot(temp, date, color="brown");
plt.xlabel("Temperature", color="purple")
plt.ylabel("Date", color="purple")

plt.title("Temperature vs date")

plt.grid(True)
plt.show()