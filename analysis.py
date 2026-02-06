"""
Bincom ICT Python Developer Test
Author: ADELU DANIEL

This script extracts shirt color data from an HTML table,
cleans the data, analyzes frequencies, and answers
basic statistical questions.
"""

import re
from collections import Counter
import random

print(">>> analysis.py started running <<<")

# -------------------------------
# STEP 1: Read HTML file
# -------------------------------
with open("colors.html", "r") as file:
    html = file.read()

# -------------------------------
# STEP 2: Extract table data
# -------------------------------
rows = re.findall(r"<td>(.*?)</td>", html, re.DOTALL)

# Remove day names (MONDAY, TUESDAY, etc.)
rows = rows[1:]

# -------------------------------
# STEP 3: Extract and clean colors
# -------------------------------
colors = []
for row in rows:
    colors.extend([c.strip().upper() for c in row.split(",")])

cleaned_colors = []
for color in colors:
    if color == "BLEW":   # fix typo
        color = "BLUE"
    cleaned_colors.append(color)

# -------------------------------
# STEP 4: Frequency analysis
# -------------------------------
color_count = Counter(cleaned_colors)

print("\nColor Frequencies:")
for color, count in color_count.items():
    print(f"{color}: {count}")

total_colors = sum(color_count.values())

# -------------------------------
# 1. Most worn color
# -------------------------------
most_worn = color_count.most_common(1)[0]
print("\nMost worn color:", most_worn)

# -------------------------------
# 2. Mean color
# -------------------------------
mean_frequency = total_colors / len(color_count)
mean_color = min(
    color_count.items(),
    key=lambda x: abs(x[1] - mean_frequency)
)
print("Mean color:", mean_color)

# -------------------------------
# 3. Median color
# -------------------------------
sorted_colors = sorted(color_count.items(), key=lambda x: x[1])
median_color = sorted_colors[len(sorted_colors) // 2]
print("Median color:", median_color)

# -------------------------------
# 4. BONUS: Variance
# -------------------------------
variance = sum(
    (count - mean_frequency) ** 2
    for count in color_count.values()
) / len(color_count)

print("Variance:", variance)

# -------------------------------
# 5. BONUS: Probability of RED
# -------------------------------
prob_red = color_count.get("RED", 0) / total_colors
print("Probability of RED:", prob_red)

# -------------------------------
# 6. BONUS: Recursive search
# -------------------------------
def recursive_search(lst, target, index=0):
    if index >= len(lst):
        return False
    if lst[index] == target:
        return True
    return recursive_search(lst, target, index + 1)

# Example usage
numbers = [1, 3, 5, 7, 9, 11]
print("Recursive search for 7:", recursive_search(numbers, 7))

# -------------------------------
# 7. BONUS: Binary to base 10
# -------------------------------
binary = "".join(str(random.randint(0, 1)) for _ in range(4))
decimal = int(binary, 2)

print("Random binary:", binary)
print("Converted to base 10:", decimal)

# -------------------------------
# 8. BONUS: Sum of first 50 Fibonacci numbers
# -------------------------------
def fibonacci_sum(n):
    a, b = 0, 1
    total = 0
    for _ in range(n):
        total += a
        a, b = b, a + b
    return total

print("Sum of first 50 Fibonacci numbers:", fibonacci_sum(50))

