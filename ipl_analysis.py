import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
file_path = "C:/Users/HP/Downloads/ipl analysis/deliveries.csv"
deliveries = pd.read_csv(file_path)

# Clean column names (remove extra spaces)
deliveries.columns = deliveries.columns.str.strip()

# Detect correct columns automatically
if 'batsman' in deliveries.columns:
    player_col = 'batsman'
elif 'batter' in deliveries.columns:
    player_col = 'batter'
else:
    raise Exception("Player column not found")

if 'batsman_runs' in deliveries.columns:
    runs_col = 'batsman_runs'
elif 'total_runs' in deliveries.columns:
    runs_col = 'total_runs'
elif 'runs_off_bat' in deliveries.columns:
    runs_col = 'runs_off_bat'
else:
    raise Exception("Runs column not found")

# Calculate total runs
runs = deliveries.groupby(player_col)[runs_col].sum()

# Sort runs
runs = runs.sort_values(ascending=False)

# Print Top 10 players
print("\n🏏 Top 10 IPL Run Scorers:\n")
print(runs.head(10))

# -----------------------------
# 📊 Visualization (Bar Graph)
# -----------------------------
top10 = runs.head(10)

top10.plot(kind='bar')
plt.title("Top 10 IPL Run Scorers")
plt.xlabel("Players")
plt.ylabel("Runs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
