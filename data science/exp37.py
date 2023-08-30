import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Generate synthetic student data
np.random.seed(0)
num_students = 50
study_time = np.random.uniform(1, 10, num_students)  # Hours
exam_scores = 50 + 10 * study_time + np.random.normal(0, 10, num_students)

# Create a DataFrame with synthetic data
data = {'StudyTime': study_time, 'ExamScore': exam_scores}
student_df = pd.DataFrame(data)

# Calculate correlation coefficient
correlation = student_df['StudyTime'].corr(student_df['ExamScore'])

# Scatter plot with regression line
plt.figure(figsize=(10, 6))
sns.scatterplot(data=student_df, x='StudyTime', y='ExamScore')
sns.regplot(data=student_df, x='StudyTime', y='ExamScore', scatter=False)
plt.title('Study Time vs. Exam Score')
plt.xlabel('Study Time (hours)')
plt.ylabel('Exam Score')
plt.show()

# Print correlation coefficient
print("Correlation Coefficient:", correlation)
