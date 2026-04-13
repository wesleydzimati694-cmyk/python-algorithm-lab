def print_names_sorted(students):
    sorted_names = sorted(student['name'] for student in students)
    print("Names in alphabetical order:")
    for name in sorted_names:
        print(name)
