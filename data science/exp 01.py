import numpy as np

student_scores = np.array([
    [85, 90, 78, 88],
    [70, 65, 80, 75],
    [92, 88, 95, 90],
    [60, 75, 70, 68],
    
])

average_scores = np.mean(student_scores, axis=0)
subject_with_highest_avg = np.argmax(average_scores)

subjects = ['Math', 'Science', 'English', 'History']

for i, subject in enumerate(subjects):
    print(f"Average score in {subject}: {average_scores[i]}")

print(f"The subject with the highest average score is: {subjects[subject_with_highest_avg]}")

