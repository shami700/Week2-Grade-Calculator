def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent! Keep shining 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up 👍"
    elif marks >= 70:
        return "C", "Good job! You can do better 😊"
    elif marks >= 60:
        return "D", "Work harder! You can improve 💪"
    else:
        return "F", "Don't give up! Try again 🔥"

name = input("Enter student name: ")

while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("❌ Enter marks between 0 and 100")
    except ValueError:
        print("❌ Invalid input! Enter number only")

grade, message = calculate_grade(marks)

print("\n📊 RESULT FOR", name.upper())
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")
