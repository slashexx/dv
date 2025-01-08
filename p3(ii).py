import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("temp.csv", usecols=["ANNUAL - MIN", "ANNUAL - MAX"])

df = pd.DataFrame(data)

df.plot(kind="hist", title="Temperature distribution", color=["yellow", "red"])

plt.xlabel("Temperature")
plt.ylabel("Years")

plt.show()