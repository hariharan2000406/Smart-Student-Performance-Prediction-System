def get_student_data():
    student_id = input("Enter Student ID: ")
    student_name = input("Enter Student Name: ")

    num_subjects = int(input("Enter number of subjects: "))

    subjects = {}

    for i in range(num_subjects):
        subject = input(f"Enter Subject {i + 1} Name: ")
        mark = float(input(f"Enter marks for {subject}: "))
        subjects[subject] = mark

    attendance = float(input("Enter Attendance Percentage: "))
    study_hours = float(input("Enter Study Hours per Day: "))
    assignment_completion = float(
        input("Enter Assignment Completion Percentage: ")
    )
    previous_performance = float(
        input("Enter Previous Academic Performance: ")
    )

    student_data = {
        "student_id": student_id,
        "student_name": student_name,
        "subjects": subjects,
        "attendance": attendance,
        "study_hours": study_hours,
        "assignment_completion": assignment_completion,
        "previous_performance": previous_performance
    }

    return student_data


def calculate_average(subjects):
    if len(subjects) == 0:
        return 0

    total_marks = sum(subjects.values())
    average = total_marks / len(subjects)

    return average


def calculate_performance(average):
    if average >= 85:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 50:
        return "Average"
    else:
        return "At Risk"


def display_result(student_data, average, performance):
    print("\n" + "=" * 50)
    print("       SMART STUDENT PERFORMANCE RESULT")
    print("=" * 50)

    print(f"Student ID       : {student_data['student_id']}")
    print(f"Student Name     : {student_data['student_name']}")

    print("\nSubject Marks:")
    for subject, mark in student_data["subjects"].items():
        print(f"{subject:<20}: {mark}")

    print("\nAverage Marks    :", round(average, 2))
    print("Attendance       :", student_data["attendance"], "%")
    print("Study Hours/Day  :", student_data["study_hours"])
    print(
        "Assignment       :",
        student_data["assignment_completion"],
        "%"
    )
    print(
        "Previous Performance :",
        student_data["previous_performance"],
        "%"
    )

    print("\nPerformance      :", performance)

    if performance == "Excellent":
        print("Risk Level       : Low")
        print("Recommendation   : Maintain your current study pattern.")

    elif performance == "Good":
        print("Risk Level       : Low")
        print("Recommendation   : Maintain current study pattern and attendance.")

    elif performance == "Average":
        print("Risk Level       : Medium")
        print("Recommendation   : Increase study hours and improve subject preparation.")

    else:
        print("Risk Level       : High")
        print("Recommendation   : Increase study hours, attendance and assignment completion.")

    print("=" * 50)
