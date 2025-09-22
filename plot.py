import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv("tourists.csv")
df["time"] = pd.to_datetime(df["time"], format="%m/%Y")
df["tourists"] = pd.to_numeric(df["tourists"])

plt.figure(figsize=(12,6))
plt.bar(df["time"], df["tourists"])

plt.title("Khách quốc tế đến Việt Nam theo tháng")
plt.xlabel("Thời gian (tháng/năm)")
plt.ylabel("Số lượng khách")

# Hiển thị nhãn theo tháng/năm
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%m/%Y"))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))  # hiển thị mỗi 3 tháng một tick

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
