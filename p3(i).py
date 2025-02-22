import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_csv("temp.csv", usecols=["ANNUAL - MIN", "ANNUAL - MAX"])

df = pd.DataFrame(data)

df.plot(kind="hist", y ="ANNUAL - MIN", title="Temperature distribution", color="brown")

plt.xlabel("Temperature")
plt.ylabel("Years")

plt.show()
