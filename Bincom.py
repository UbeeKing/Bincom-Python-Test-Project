# Bincom ICT Python Developer Test
# Author: Ubong-Abasi Pius Akpan 
# Date: 29th May, 2026
# Description: Web Scraping and Statistical Analysis Of Dress Colors 

from bs4 import BeautifulSoup

# Import Counter to tally frequency of data items
from collections import Counter
# Used to calculate the statistical variance of the dataset
import statistics
# Generating random numbers
import random


with open("Bincom.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

rows = soup.select("tbody tr")
TYPO_MAP = {
    "BLEW": "BLUE",
    "ARSH": "ASH"
}

all_colors = []

for row in rows:
    cells = row.find_all("td")
    day = cells[0].get_text(strip=True)
    raw_colors = cells[1].get_text(strip=True).split(",")
    
    for raw in raw_colors:
        color = raw.strip().upper()
        if not color:  # skip if empty
            continue
        color = TYPO_MAP.get(color, color)
        all_colors.append(color)
    print(f"Total colors: {len(all_colors)}")

# To find the most common color in the dataset
frequencies = Counter(all_colors)
most_worn = frequencies.most_common(1)

print(f"Most worn color: {most_worn}")

unique_colors = sorted(set(all_colors))

# Assigning numbers to colors
rank_map = {color: i for i, color in enumerate(unique_colors)}
print(rank_map)

ranks = [rank_map[c] for c in all_colors]
mean_rank = round(sum(ranks) / len(ranks))
mean_color = unique_colors[mean_rank]

print(f"Mean color: {mean_color}")

# Calculating the median color
sorted_colors = sorted(all_colors)
middle = len(sorted_colors) // 2
median_color = sorted_colors[middle]

print(f"Median color: {median_color}")

# Calculating the Variance of the colorsets
freq_values = list(frequencies.values())
variance = statistics.variance(freq_values)

print(f"Variance: {variance}")

# Calculating the probability choosing a red color
red_count = all_colors.count("RED")
total_colors = len(all_colors)
probability_red = red_count / total_colors

print(f"Number of times RED appeared: {red_count}")
print(f"Total colors: {total_colors}")
print(f"Probability of RED: {probability_red:.4f}")
print(f"Probability of RED in percentage: {probability_red * 100:.2f}%")

# Q6 - Save to PostgreSQL
# TODO: Implement after learning PostgreSQL
# Will use psycopg2 library to connect and save color frequencies

def binary_search(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)
    
# Q7 - Recursive Binary Search
numbers = sorted([4, 2, 9, 1, 7, 3, 15, 6, 11])
print(f"Sorted list: {numbers}")

target = int(input("Enter a number to search for: "))
result = binary_search(numbers, target, 0, len(numbers) - 1)

if result != -1:
    print(f"Number {target} found at index {result}!")
else:
    print(f"Number {target} was not found in the list.")

# Q8 - Random 4-digit binary to base 10
bits = [random.randint(0, 1) for _ in range(4)]
binary_str = "".join(str(b) for b in bits)
base10 = int(binary_str, 2)

print(f"Random binary number : {binary_str}")
print(f"Base 10 equivalent   : {base10}")


# Q9 - Sum of first 50 Fibonacci numbers
def fibonacci_sum(n):
    total = 0
    a, b = 0, 1
    
    for _ in range(n):
        total += a
        a, b = b, a + b
    
    return total

result = fibonacci_sum(50)
print(f"Sum of first 50 Fibonacci numbers: {result}")