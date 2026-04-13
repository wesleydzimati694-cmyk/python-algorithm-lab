def get_valid_score():
    while True:
        try:
            score = int(input("Enter a score (0–100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score!")
        except ValueError:
            print("Please enter a numeric value.")

# Usage
score = get_valid_score()
print(f"Valid score entered: {score}")