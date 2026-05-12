"""
PYTHON BASICS - WEEK 2: CONTROL FLOW
Learn: if/else, for loops, while loops, break, continue
"""

# ============================================
# EXERCISE 1: if/elif/else Statements
# ============================================

print("=== IF/ELIF/ELSE EXAMPLES ===\n")

# Simple if/else
age = 25
if age >= 18:
    print(f"✅ Age {age}: You are an adult")
else:
    print(f"❌ Age {age}: You are a minor")

# if/elif/else chain
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Score: {score} → Grade: {grade}")

# Nested if
is_employed = True
salary = 50000
if is_employed:
    if salary > 40000:
        print("✅ Employed with good salary")
    else:
        print("⚠️ Employed but low salary")
else:
    print("❌ Not employed")

# ============================================
# EXERCISE 2: for Loops
# ============================================

print("\n=== FOR LOOP EXAMPLES ===\n")

# Loop through range
print("Numbers 1-5:")
for i in range(1, 6):
    print(i, end=" ")
print()

# Loop through list
print("\nSkills:")
skills = ["Python", "AWS", "Docker", "Kubernetes"]
for skill in skills:
    print(f"  • {skill}")

# Loop with index
print("\nSkills with index:")
for index, skill in enumerate(skills):
    print(f"  {index + 1}. {skill}")

# Nested loops (multiplication table)
print("\n2x2 Multiplication Table:")
for i in range(1, 3):
    for j in range(1, 3):
        print(f"{i}×{j}={i*j}", end="  ")
    print()

# ============================================
# EXERCISE 3: while Loops
# ============================================

print("\n=== WHILE LOOP EXAMPLES ===\n")

# Simple while
count = 1
while count <= 3:
    print(f"Count: {count}")
    count += 1

# while with break
print("\nFinding number 5:")
num = 1
while True:
    if num == 5:
        print(f"Found {num}! Breaking...")
        break
    num += 1

# while with continue
print("\nSkipping even numbers:")
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue  # Skip this iteration
    print(num, end=" ")
print()

# ============================================
# EXERCISE 4: break and continue
# ============================================

print("\n=== BREAK & CONTINUE ===\n")

# Find first number divisible by 7
print("Find first number divisible by 7:")
for num in range(1, 100):
    if num % 7 == 0:
        print(f"Found: {num}")
        break

# Skip multiples of 3
print("\nNumbers 1-10 (skip multiples of 3):")
for num in range(1, 11):
    if num % 3 == 0:
        continue
    print(num, end=" ")
print()

# ============================================
# EXERCISE 5: List Comprehension
# ============================================

print("\n=== LIST COMPREHENSION ===\n")

# Traditional way
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(f"Squares (traditional): {squares}")

# Using list comprehension
squares = [i ** 2 for i in range(1, 6)]
print(f"Squares (comprehension): {squares}")

# With condition
even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(f"Even numbers 1-10: {even_numbers}")

# ============================================
# PRACTICE TASKS
# ============================================

print("\n=== PRACTICE CHALLENGES ===\n")

# Challenge 1: Print multiplication table for 7
print("Challenge 1: 7x Multiplication Table")
for i in range(1, 11):
    print(f"7 × {i} = {7 * i}")

# Challenge 2: Find sum of numbers 1-100
print("\nChallenge 2: Sum of 1-100")
total = sum(range(1, 101))
print(f"Sum: {total}")

# Challenge 3: Factorial of 5
print("\nChallenge 3: Factorial of 5")
factorial = 1
for i in range(1, 6):
    factorial *= i
print(f"5! = {factorial}")

print("\n✅ Week 2 exercises complete!")
print("📚 Next: Learn functions and modules")
