import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv(
 r"C:\C++ vs code\.vscode\Sample - Superstore.csv",
 encoding="latin1"
)

# -----------------------------
# KPI VALUES
# -----------------------------
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
avg_sales = df["Sales"].mean()
total_orders = df["Order ID"].nunique()

# -----------------------------
# OUTLIER REMOVE
# -----------------------------
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)
IQR = Q3 - Q1

df_clean = df[
(df["Sales"] >= Q1 - 1.5 * IQR) &
(df["Sales"] <= Q3 + 1.5 * IQR)
]

# -----------------------------
# LINEAR REGRESSION
# -----------------------------
X = df_clean[["Sales"]]
y = df_clean["Profit"]

X_train,X_test,y_train,y_test = train_test_split(
X,y,test_size=0.2,random_state=42
)

model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print("R2 Score:", r2_score(y_test,y_pred))
print("MSE:", mean_squared_error(y_test,y_pred))


# -----------------------------
# DASHBOARD
# -----------------------------
plt.figure(figsize=(18,12))

# ===== KPI CARDS =====
plt.subplot(4,4,1)
plt.text(0.5,0.5,f"Total Sales\n{total_sales:,.0f}",
fontsize=14,ha='center')
plt.axis('off')

plt.subplot(4,4,2)
plt.text(0.5,0.5,f"Total Profit\n{total_profit:,.0f}",
fontsize=14,ha='center')
plt.axis('off')

plt.subplot(4,4,3)
plt.text(0.5,0.5,f"Avg Sales\n{avg_sales:,.2f}",
fontsize=14,ha='center')
plt.axis('off')

plt.subplot(4,4,4)
plt.text(0.5,0.5,f"Orders\n{total_orders}",
fontsize=14,ha='center')
plt.axis('off')


# ===== Histogram =====
plt.subplot(4,4,5)
sns.histplot(df["Sales"], kde=True)
plt.title("Sales Distribution")

# ===== Category Sales =====
plt.subplot(4,4,6)
sns.barplot(x="Category", y="Sales", data=df)
plt.xticks(rotation=20)
plt.title("Category Sales")

# ===== Region Sales =====
plt.subplot(4,4,7)
sns.barplot(x="Region", y="Sales", data=df)
plt.xticks(rotation=30)
plt.title("Region Sales")

# ===== Outlier Boxplot =====
plt.subplot(4,4,8)
sns.boxplot(x=df["Sales"])
plt.title("Outlier Detection")


# ===== Linear Regression =====
plt.subplot(4,4,9)
sns.regplot(x="Sales", y="Profit", data=df_clean)
plt.title("Linear Regression")

# ===== Scatter =====
plt.subplot(4,4,10)
sns.scatterplot(x="Sales", y="Profit",
hue="Category", data=df)
plt.title("Sales vs Profit")

# ===== Heatmap =====
plt.subplot(4,4,11)
sns.heatmap(
df[["Sales","Profit","Quantity","Discount"]].corr(),
annot=True,
cmap="coolwarm"
)
plt.title("Correlation Heatmap")


# ===== Profit by Segment =====
plt.subplot(4,4,13)
sns.barplot(x="Segment", y="Profit", data=df)
plt.xticks(rotation=20)
plt.title("Segment Profit")

# ===== Pie Chart =====
plt.subplot(4,4,14)
df["Category"].value_counts().plot.pie(autopct='%1.1f%%')
plt.title("Category Share")

# ===== KDE Plot =====
plt.subplot(4,4,15)
sns.kdeplot(df["Profit"], fill=True)
plt.title("Profit Density")


plt.tight_layout()
plt.suptitle("SUPERSTORE  DASHBOARD 2026", fontsize=18)

plt.show()










