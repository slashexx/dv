import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("hotelsales.csv")
df = pd.DataFrame(data)

df.plot(kind="box", title="Hotel sales distribution", x="Year")

plt.xlabel("Resorts")
plt.ylabel("Rating")

plt.show()