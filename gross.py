import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\acer\Documents\MEGA\Programming\ASPIRE\Python\Economics\debt\nominal_gdp_usd_1960-2025.csv")

japan = (df.iloc[0])
x = []
y = []
for i, m in japan.items():
    x.append(i)
    y.append((m))
x = x[1:]
y = y[1:]

chian = (df.iloc[1])
m = []
t = []
for h, u in chian.items():
    m.append(h)
    t.append((u))
m = m[1:]
t = t[1:]

usa = (df.iloc[2])
p = []
o = []
for w, d in usa.items():
    p.append(w)
    o.append((d))
p = p[1:]
o =o[1:]

plt.plot(m, t, color='green', label='United States')
plt.plot(x, y, color='blue', label='Japan')
plt.plot(p, o, color='red', label='China')
plt.xticks(rotation =45)
plt.grid(axis="y", alpha = 0.3)
plt.title("Gross domestic product calculated at current market prices", fontweight ="bold")
plt.xlabel("Years", fontweight = "bold")
plt.ylabel("Trillions USD", fontweight ="bold")
plt.legend()
plt.show()     
