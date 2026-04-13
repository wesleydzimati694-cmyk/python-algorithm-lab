def score_tracker():
    student_scores = {}

    while True:
        name = input("Enter student's name (or 'done' to quit): ")
        if name.lower() == 'done':
            break
        score = float(input(f"Enter {name}'s score: "))
        student_scores[name] = score

    print("\nClass Report:")
    for name, score in student_scores.items():
        print(f"{name}: {score}")

    if student_scores:
        class_average = sum(student_scores.values()) / len(student_scores)
        print(f"\nClass Average: {class_average:.2f}")
    else:
        print("No scores entered.")

if __name__ == "_main_":
    score_tracker()