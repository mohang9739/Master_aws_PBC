"""
PYTHON BASICS - WEEK 1: SETUP & SYNTAX
Learn: Variables, Data Types, Operators, First Program
"""

# ============================================
# EXERCISE 1: Hello World
# ============================================
print("Hello, Platform Engineer!")
print("Starting AWS DevOps journey...")

# ============================================
# EXERCISE 2: Variables & Data Types
# ============================================

# Strings
name = "Your Name"
title = "Platform Engineer"
print(f"My name is {name} and I want to be a {title}")

# Numbers
age = 25
salary = 85000.50
print(f"Age: {age}, Salary: ${salary:,.2f}")

# Booleans
is_learning = True
is_certified = False
print(f"Learning: {is_learning}, Certified: {is_certified}")

# Lists
skills = ["Python", "AWS", "Docker", "Kubernetes"]
print(f"Skills: {skills}")
print(f"First skill: {skills[0]}")
print(f"Total skills: {len(skills)}")

# Dictionaries
student = {
    "name": "Alex",
    "email": "alex@example.com",
    "year": 1,
    "gpa": 3.8
}
print(f"Student: {student['name']} - Email: {student['email']}")

# ============================================
# EXERCISE 3: Basic Operators
# ============================================

# Arithmetic
num1 = 10
num2 = 3
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} // {num2} = {num1 // num2}")  # Floor division
print(f"{num1} % {num2} = {num1 % num2}")   # Modulo
print(f"{num1} ** {num2} = {num1 ** num2}") # Power

# Comparison
print(f"\n{num1} > {num2}: {num1 > num2}")
print(f"{num1} == {num2}: {num1 == num2}")
print(f"{num1} != {num2}: {num1 != num2}")

# Logical
is_admin = True
is_active = True
print(f"\nBoth admin and active: {is_admin and is_active}")
print(f"Either admin or active: {is_admin or is_active}")
print(f"Not admin: {not is_admin}")

# ============================================
# EXERCISE 4: User Input
# ============================================
# Uncomment to test interactively
# user_name = input("What is your name? ")
# user_age = int(input("How old are you? "))
# print(f"Hello {user_name}! You are {user_age} years old.")

# ============================================
# PRACTICE TASK: Write your own program
# ============================================
# TODO: Create a program that:
# 1. Asks user for their name
# 2. Asks user for their job title
# 3. Calculates years until retirement (67)
# 4. Prints a personalized message

# SOLUTION TEMPLATE:
# name = input("Enter your name: ")
# job = input("Enter your job: ")
# age = int(input("Enter your age: "))
# years_to_retire = 67 - age
# print(f"{name}, you are a {job} and will retire in {years_to_retire} years!")

print("\n✅ Week 1 exercises complete!")
print("📚 Next: Learn control flow (if/else, loops)")
