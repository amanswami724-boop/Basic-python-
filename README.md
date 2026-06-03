# Basic-python-# Python and Artificial Intelligence Assignment
This repository contains solutions to the basic Python and Artificial Intelligence assignment questions.
---
## 📑 Table of Contents
1. [Data Types Explanation](#1-data-types-explanation)
2. [Variables and Printing](#2-variables-and-printing)
3. [String Input and Manipulation](#3-string-input-and-manipulation)
4. [Common String Methods](#4-common-string-methods)
5. [List Operations (Fruits)](#5-list-operations-fruits)
6. [List Modification (Numbers)](#6-list-modification-numbers)
7. [Introduction to Artificial Intelligence](#7-introduction-to-artificial-intelligence)
8. [Identifying AI in Real-life Examples](#8-identifying-ai-in-real-life-examples)
---
## 1. Data Types Explanation
Python has several built-in data types. Here is an explanation of the four core basic types:

| Data Type | Description | Example |
| :--- | :--- | :--- |
| **Integer (`int`)** | Whole numbers without decimals. Can be positive, negative, or zero. | `age = 20`, `temperature = -5` |
| **Float (`float`)** | Numbers that contain one or more decimals. | `height = 5.8`, `pi = 3.1415` |
| **String (`str`)** | A sequence of characters wrapped in single, double, or triple quotes. | `name = "Gargi"`, `city = 'Jaipur'` |
| **Boolean (`bool`)** | Represents one of two values: `True` or `False`. Used for logical conditions. | `is_logged_in = True` |

---
## 2. Variables and Printing

```python
# Creating variables and storing details
name = "Gargi"
age = 20
city = "Jaipur"
# Printing the values in the requested format
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
---
## Q4. Explain any five commonly used string methods in Python with examples.

1. **`upper()`**: Converts all lowercase characters in a string into uppercase.
   ```python
   text = "python"
   print(text.upper())  # Output: PYTHON
lower(): Converts all uppercase characters in a string into lowercase.

Python
text = "DATA"
print(text.lower())  # Output: data
strip(): Removes any leading and trailing whitespaces from a string.

Python
text = "  hello  "
print(text.strip())  # Output: "hello"
replace(old, new): Replaces a specified phrase or substring with another specified phrase.

Python
text = "I like Java"
print(text.replace("Java", "Python"))  # Output: I like Python
split(): Splits a string into a list of substrings based on a specified delimiter.

Python
text = "Machine Learning Basics"
print(text.split())  # Output: ['Machine', 'Learning', 'Basics']

Q7. What is Artificial Intelligence (AI)? Explain its importance and mention any four real-life applications of AI.
Definition: Artificial Intelligence (AI) is a domain of computer science focused on building intelligent machines capable of executing tasks that typically demand human intelligence, such as visual perception, decision-making, speech recognition, and language translation.

Importance of AI:
Automation of Repetitive Tasks: It frees human workers from mundane, routine jobs, boosting productivity.

Processing Big Data: AI handles massive datasets efficiently to extract useful insights swiftly.

Error Reduction: AI systems operate continuously without fatigue, reducing human error margins in critical processes.

Four Real-Life Applications:
Virtual Voice Assistants: Systems like Alexa or Siri parse natural language commands to complete actions.

E-Commerce Recommendation Engines: Algorithms deployed by platforms like Amazon or Netflix predict preferences.

Autonomous Vehicles: Self-driving cars utilize AI architectures coupled with computer vision arrays to navigate traffic.

Healthcare & Diagnostics: AI models assist clinicians by parsing radiography reports to flag early-stage anomalies.

Q8. Identify whether the following are examples of AI and explain why: ChatGPT, Google Maps route prediction, Calculator, Netflix recommendations, Voice assistants (Alexa/Siri)
ChatGPT: Yes, it is AI. It relies on complex Large Language Models (LLMs) to process natural language input prompts and generate human-like text responses adaptively.

Google Maps route prediction: Yes, it is AI. It incorporates predictive machine learning algorithms to evaluate real-time traffic information and dynamically calculate optimal route trajectories.

Calculator: No, it is not AI. It runs purely on hard-coded, deterministic mathematical logic rules. It possesses no capacity to adapt or learn through experience.

Netflix recommendations: Yes, it is AI. It employs collaborative filtering algorithms to process specific viewing metrics and personalize recommended watch-lists.

Voice assistants (Alexa/Siri): Yes, it is AI. They depend comprehensively on Natural Language Processing (NLP) models to map out audio waves and isolate linguistic commands.

# Q3. Write a Python program that: Takes a user's name as input,
# prints the name in uppercase, and prints total character length.
# =====================================================================
print("--- Question 3 ---")
user_name = input("Enter your name: ")
print(f"Uppercase Name: {user_name.upper()}")
print(f"Total number of characters: {len(user_name)}")
print("\n" + "="*40 + "\n")


# =====================================================================
# Q5. Create a list containing the names of five fruits.
# - Print the complete list.
# - Print the first and last element.
# - Print the total number of items in the list.
# =====================================================================
print("--- Question 5 ---")
fruits = ["Apple", "Banana", "Cherry", "Mango", "Orange"]
print(f"Complete list: {fruits}")
print(f"First element: {fruits[0]}")
print(f"Last element: {fruits[-1]}")
print(f"Total items in the list: {len(fruits)}")
print("\n" + "="*40 + "\n")


# =====================================================================
# Q6. Write a Python program to:
# - Create a list of numbers [10, 20, 30, 40, 50]
# - Add 60 to the list.
# - Remove 20 from the list.
# - Print the updated list.
# =====================================================================
print("--- Question 6 ---")
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers.remove(20)
print(f"Updated list: {numbers}")
