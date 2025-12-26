import pandas as pd
import matplotlib.pyplot as plt

# Create the DataFrame
data = {
    "customer_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "visits": [8, 2, 6, 1, 9, 4, 7, 3],
    "total_spent": [5200, 900, 3500, 450, 6100, 2200, 4800, 1300],
    "points_redeemed": [200, 0, 120, 0, 300, 80, 180, 40],
    "active": ["Yes", "No", "Yes", "No", "Yes", "Yes", "Yes", "No"]
}

df = pd.DataFrame(data)

# Display data
print("Loyalty Program Data:")
print(df)

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Customer retention analysis
retention_counts = df['active'].value_counts()
print("\nCustomer Retention Counts:")
print(retention_counts)

# Bar chart: Active vs Inactive customers
retention_counts.plot(kind='bar')
plt.title("Customer Retention Status")
plt.xlabel("Customer Status")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

# Average spending by customer status
avg_spending = df.groupby('active')['total_spent'].mean()
print("\nAverage Spending by Customer Status:")
print(avg_spending)

# Bar chart: Average spending comparison
avg_spending.plot(kind='bar')
plt.title("Average Spending: Active vs Inactive Customers")
plt.xlabel("Customer Status")
plt.ylabel("Average Total Spent")
plt.tight_layout()
plt.show()

# Average visits by customer status
avg_visits = df.groupby('active')['visits'].mean()
print("\nAverage Visits by Customer Status:")
print(avg_visits)

# Bar chart: Visit comparison
avg_visits.plot(kind='bar')
plt.title("Average Visits: Active vs Inactive Customers")
plt.xlabel("Customer Status")
plt.ylabel("Average Number of Visits")
plt.tight_layout()
plt.show()

# Correlation analysis
print("\nCorrelation Matrix:")
print(df[['visits', 'total_spent', 'points_redeemed']].corr())

# Key insights
print("\nINSIGHTS:")
print("- Active loyalty members visit more frequently.")
print("- Active members spend more on average.")
print("- Higher engagement leads to better customer retention.")

