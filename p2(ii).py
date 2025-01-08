import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Melasaleswithdays.csv")

df.plot(kind="line", x="Day", color=["red", "blue", "brown"])

plt.xlabel("Days")
plt.ylabel("Sales")

plt.title("Melasales across the weeks per days")
plt.show()
