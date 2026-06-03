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
### Python Code
```python
# Creating variables and storing details
name = "Gargi"
age = 20
city = "Jaipur"
# Printing the values in the requested format
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")


## Q3 print("\nQ3. Name Operations")
user_name = input("Enter your name: ")
print("Uppercase:", user_name.upper())
print("Total characters:", len(user_name))

## Q4 print("\nQ4. String Methods")
sample = "python programming"
print(sample.upper())
print(sample.lower())
print(sample.title())
print(sample.replace("python", "Python"))
print(sample.count("m"))

## Q5 print("\nQ5. Fruit List")
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print("Complete list:", fruits)
print("First element:", fruits[0])
print("Last element:", fruits[-1])
print("Total items:", len(fruits))

## Q6 print("\nQ6. List Operations")
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers.remove(20)
print("Updated list:", numbers)

## Q7 print("\nQ7. Artificial Intelligence")
print("AI is the simulation of human intelligence in machines.")
print("Applications: ChatGPT, Self-driving cars, Medical diagnosis, Recommendation systems")

## Q8 print("\nQ8. AI Examples")
examples = {
    "ChatGPT": "AI",
    "Google Maps route prediction": "AI",
    "Calculator": "Not AI",
    "Netflix recommendations": "AI",
    "Alexa/Siri": "AI"
}
for k, v in examples.items():
    print(f"{k}: {v}")
