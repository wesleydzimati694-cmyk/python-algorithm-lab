def find_top_performer(students):
    top_student = max(students, key=lambda x: x['grade'])
    print(f"Top performer: {top_student['name']} with grade {top_student['grade']}")

# Example data
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]

