
# Function to calculate average
def calculate_average(total):
    return total / 5


# Function to determine grade
def determine_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "Fail"


# Main program
try:
    students = int(input("Enter number of students: "))
    
    for student in range(1, students + 1):
        studentsName = str(input("Enter Name of student: "))
        print("\nStudents : ", student ," : ", studentsName)
        subjects = ["Tamil", "English", "Maths", "Physics", "Chemistry"]
        marks = []

        # Accept marks for five subjects
        
        for subject in subjects:
            mark = float(input(f"Enter marks for {subject}: "))

            # Validate marks
            if mark < 0 or mark > 100:
                raise ValueError("Marks must be between 0 and 100.")

            marks.append(mark)

        # Calculate total and average
        total = sum(marks)
        average = calculate_average(total)

        # Determine grade
        grade = determine_grade(average)

        # Check pass or fail
        if any(mark < 35 for mark in marks):
            result = "Fail"
        else:
            result = "Pass"

        

        # Display subject-wise marks
        print("\n----- Subject Marks -----")

        for subject, mark in zip(subjects, marks):
            print(f"{subject}: {mark}")     
            # Display output
        print("\n----- Student Result -----")
        print("Total:", total)
        print("Average:", average)
        print("Grade:", grade)
        print("Result:", result)
        print("\n----- END -----")


except ValueError as e:
    print("Invalid Input:", e)

except Exception as e:
    print("An error occurred:", e)
