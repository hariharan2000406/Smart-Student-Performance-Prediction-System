import functions as f

def main():
    student_data = f.get_student_data()
    average = f.calculate_average(student_data["subjects"])
    performance = f.calculate_performance(average)
    f.display_result(student_data, average, performance)

if __name__ == "__main__":
    main()
