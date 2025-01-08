import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Melasales.csv")
df.plot(kind="line", color=["red", "blue", "brown"])

plt.title("Melasales across the weeks")
plt.xlabel("Days")  
plt.ylabel("Sales")

plt.show()