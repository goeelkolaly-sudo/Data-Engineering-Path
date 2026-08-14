import numpy as np

# Data setup
scores = np.array([
    [85, 90, 78, 92],
    [60, 75, 68, 70],
    [95, 88, 91, 97],
    [55, 65, 58, 62],
    [72, 80, 75, 85],
    [88, 92, 84, 90]
])
subjects = np.array(["Python", "SQL", "Statistics", "NumPy"])
students = np.array(["Ahmed", "Mona", "Omar", "Sara", "Ali", "Youssef"])


# Part 1 — Indexing & Slicing

# 1. Print the scores of Omar
print("1. Omar's scores:", scores[2])

# 2. Print the score of Mona in SQL
print("2. Mona's score in SQL:", scores[1, 1])

# 3. Print the scores of the first 3 students
print("3. Scores of the first 3 students:\n", scores[:3])

# 4. Print the scores of the last 2 students
print("4. Scores of the last 2 students:\n", scores[-2:])

# 5. Print the scores of all students in Python
print("5. Python scores for all students:", scores[:, 0])

# 6. Print the scores of Statistics and NumPy for the first 4 students
print("6. Stats & NumPy for the first 4 students:\n", scores[:4, 2:])


# Part 2 — Element-wise Operations

# 7. Create a new array where 5 points are added to every Python score
python_bonus = scores[:, 0] + 5
print("7. Python scores with 5-point bonus:", python_bonus)

# 8. Increase the scores in SQL by 10%
sql_increased = scores[:, 1] * 1.10
print("8. SQL scores increased by 10%:", sql_increased)

# 9. Calculate the total score for every student
total_scores = scores.sum(axis=1)
print("9. Total score for each student:", total_scores)

# 10. Calculate the average score for every student
average_scores = scores.mean(axis=1)
print("10. Average score for each student:", average_scores)


# Part 3 — Logical Operations & Boolean Masking

# 11. Find all students whose average score is >= 80
avg_mask = average_scores >= 80
print("11. Students with average >= 80:", students[avg_mask])

# 12. Find students who scored less than 60 in at least one subject
low_score_mask = (scores < 60).any(axis=1)
print("12. Students with < 60 in any subject:", students[low_score_mask])

# 13. Find students who scored >= 90 in Python AND >= 90 in NumPy
python_numpy_mask = (scores[:, 0] >= 90) & (scores[:, 3] >= 90)
print("13. Students with >= 90 in Python and NumPy:", students[python_numpy_mask])

# 14. Create a boolean array that tells whether each student passed (average >= 70)
passed_array = average_scores >= 70
print("14. Pass status boolean array:", passed_array)


# Part 4 — Conditions with np.where()

# 15. Create a status array based on average scores
status_array = np.where(
    average_scores >= 85, "Excellent",
    np.where(average_scores >= 70, "Passed", "Failed")
)
print("15. Student status array:", status_array)


# Bonus / Challenge Question

# Students who satisfy: Average >= 80 AND No subject score is below 70
challenge_mask = (average_scores >= 80) & (scores >= 70).all(axis=1)
print("Bonus Solution - Students names:", students[challenge_mask])