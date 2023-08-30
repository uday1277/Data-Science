import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a synthetic dataset
data = {
    'Name': ['Player A', 'Player B', 'Player C', 'Player D', 'Player E', 'Player F', 'Player G'],
    'Age': [25, 28, 22, 30, 24, 27, 29],
    'Position': ['Forward', 'Midfielder', 'Forward', 'Defender', 'Midfielder', 'Forward', 'Defender'],
    'GoalsScored': [15, 10, 12, 5, 8, 7, 3],
    'WeeklySalary': [100000, 90000, 75000, 80000, 85000, 95000, 70000]
}

# Create a DataFrame from the data
soccer_df = pd.DataFrame(data)

# Find the top 5 players with the highest number of goals scored
top_goals_players = soccer_df.nlargest(5, 'GoalsScored')

# Find the top 5 players with the highest salaries
top_salary_players = soccer_df.nlargest(5, 'WeeklySalary')

# Calculate the average age of players
average_age = soccer_df['Age'].mean()

# Display players above the average age
above_average_age_players = soccer_df[soccer_df['Age'] > average_age]

# Visualize the distribution of players based on their positions using a bar chart
position_counts = soccer_df['Position'].value_counts()
plt.bar(position_counts.index, position_counts.values)
plt.xlabel('Position')
plt.ylabel('Number of Players')
plt.title('Player Distribution by Position')
plt.show()

# Display results
print("Top 5 Players with Highest Goals Scored:\n", top_goals_players)
print("\nTop 5 Players with Highest Salaries:\n", top_salary_players)
print("\nAverage Age of Players:", average_age)
print("\nPlayers Above Average Age:\n", above_average_age_players)
