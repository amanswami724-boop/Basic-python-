"""
Assignment 1 - Data Science with AIML
B K Birla Institute of Engineering & Technology, Pilani
"""

# Q1
print("Q1. Data Types")
print("int:", 25)
print("float:", 25.5)
print("str:", "Hello")
print("bool:", True)

# Q2
print("\nQ2. Variables")
name = "Aman"
age = 20
city = "Jaipur"
print("Name:", name)
print("Age:", age)
print("City:", city)

# Q3
print("\nQ3. Name Operations")
user_name = input("Enter your name: ")
print("Uppercase:", user_name.upper())
print("Total characters:", len(user_name))

# Q4
print("\nQ4. String Methods")
sample = "python programming"
print(sample.upper())
print(sample.lower())
print(sample.title())
print(sample.replace("python", "Python"))
print(sample.count("m"))

# Q5
print("\nQ5. Fruit List")
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print("Complete list:", fruits)
print("First element:", fruits[0])
print("Last element:", fruits[-1])
print("Total items:", len(fruits))

# Q6
print("\nQ6. List Operations")
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers.remove(20)
print("Updated list:", numbers)

# Q7
print("\nQ7. Artificial Intelligence")
print("AI is the simulation of human intelligence in machines.")
print("Applications: ChatGPT, Self-driving cars, Medical diagnosis, Recommendation systems")

# Q8
print("\nQ8. AI Examples")
examples = {
    "ChatGPT": "AI",
    "Google Maps route prediction": "AI",
    "Calculator": "Not AI",
    "Netflix recommendations": "AI",
    "Alexa/Siri": "AI"
}
for k, v in examples.items():
    print(f"{k}: {v}")
