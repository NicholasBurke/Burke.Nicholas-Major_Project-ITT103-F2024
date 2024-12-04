# Course class is for the courses with an ID, name, and fee.
class Course:
    def __init__(self, course_id, name, fee):
        self.course_id = course_id  
        self.name = name            
        self.fee = fee              


# Student class is for the students with an ID, name, email, courses, and balance.
class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id  
        self.name = name              
        self.email = email            
        self.courses = []             
        self.balance = 0              

    # Used to enroll the student in a course if they have enough money
    def enroll(self, course, payment):
        # Check if the student is already in the course
        if course in self.courses:
            print("Already enrolled in this course.")
        else:
            # Check if the payment is at least 40% of the course fee
            if payment >= 0.4 * course.fee:
                # Ensure the student has enough to pay
                if payment > self.balance:
                    print(f"Insufficient funds. Current balance: ${self.balance:.2f}")
                else:
                    self.courses.append(course)  
                    self.balance -= payment     
                    print(f"Enrolled in {course.name} with payment of ${payment:.2f}. Remaining balance: ${self.balance:.2f}")
            else:
                print(f"Minimum payment of 40% required to enroll in {course.name}.")

    # Calculating the total fee of all courses the student is in
    def get_total_fee(self):
        return sum(course.fee for course in self.courses)


# Manages courses, students, enrollments, and payments
class RegistrationSystem:
    def __init__(self):
        self.courses = []           
        self.students = {}          

    # Used to add a new course to the system
    def add_course(self, course_id, name, fee):
        # Check if a course with the same ID already exists
        if any(course.course_id == course_id for course in self.courses):
            print("Course ID already exists.")
        else:
            self.courses.append(Course(course_id, name, fee))  
            print("Course added successfully.")

    # register a new student in the system
    def register_student(self, student_id, name, email):
        # Check if a student with the same ID already exists
        if student_id in self.students:
            print("Student ID already exists.")
        else:
            self.students[student_id] = Student(student_id, name, email)  
            print("Student registered successfully.")

    # Enroll a student in a course
    def enroll_in_course(self, student_id, course_id):
        student = self.students.get(student_id)  
        if student is None:
            print("Student not found.")
        else:
            course = next((course for course in self.courses if course.course_id == course_id), None)  
            if course is None:
                print("Course not found.")
            else:
                # Ask the user to enter the payment amount
                payment = float(input(f"Enter the payment amount for {course.name} (at least 40% of ${course.fee}): "))
                student.enroll(course, payment)  

    # Make a payment to reduce the student's balance
    def calculate_payment(self, student_id, payment):
        student = self.students.get(student_id)  
        if student is None:
            print("Student not found.")
        elif payment <= 0:  
            print("Payment amount must be positive.")
        else:
            student.balance -= payment  
            print(f"Payment accepted. New balance: ${student.balance:.2f}")

    # Used to add money to the student's balance
    def add_money_to_balance(self, student_id, amount):
        student = self.students.get(student_id)  
        if student is None:
            print("Student not found.")
        elif amount <= 0:  
            print("Amount to add must be positive.")
        else:
            student.balance += amount  
            print(f"Added ${amount:.2f} to balance. New balance: ${student.balance:.2f}")

    # Check a student's balance
    def check_student_balance(self, student_id):
        student = self.students.get(student_id)  
        if student is None:
            print("Student not found.")
        else:
            print(f"Student balance: ${student.balance:.2f}")

    # Used to display all available courses
    def show_courses(self):
        if not self.courses:
            print("No courses available.")
        else:
            for course in self.courses:
                print(f"Course ID: {course.course_id}, Name: {course.name}, Fee: ${course.fee}")

    # Used to display all registered students
    def show_registered_students(self):
        if not self.students:
            print("No students registered.")
        else:
            for student_id, student in self.students.items():
                print(f"Student ID: {student.student_id}, Name: {student.name}, Email: {student.email}, Balance: ${student.balance}")

    # Used to display all students enrolled in a specific course
    def show_students_in_course(self, course_id):
        # Find all students who are enrolled in thecourse
        students_in_course = [student for student in self.students.values() if any(course.course_id == course_id for course in student.courses)]
        if not students_in_course:
            print("No students enrolled in this course.")
        else:
            for student in students_in_course:
                print(f"Student ID: {student.student_id}, Name: {student.name}, Email: {student.email}, Balance: ${student.balance}")

    # Function to make a payment or add money
    def make_payment(self, student_id):
        student = self.students.get(student_id)  
        if student is None:
            print("Student not found.")
        else:
            print("Choose an option:")
            print("1. Add money to account")
            print("2. Pay for a course")
            choice = input("Enter your choice: ")

            if choice == '1':
                amount = float(input("Enter the amount to add: "))
                self.add_money_to_balance(student_id, amount)
            elif choice == '2':
                if not student.courses:
                    print("No enrolled courses found.")
                else:
                    print("Enrolled courses:")
                    for i, course in enumerate(student.courses, start=1):
                        print(f"{i}. {course.name} (Fee: ${course.fee})")
                    course_choice = int(input("Enter the course number to pay for: ")) - 1
                    if 0 <= course_choice < len(student.courses):
                        course = student.courses[course_choice]
                        payment = float(input(f"Enter payment amount for {course.name}: "))
                        self.calculate_payment(student_id, payment)
                    else:
                        print("Invalid course selection.")
            else:
                print("Invalid choice.")

# Function to handle the registration system
def main():
    system = RegistrationSystem()  # Create a new registration system

    while True:
        # Show teh menu and options for the user
        print("\n1. Register Student")
        print("2. Add Course")
        print("3. Enroll in Course")
        print("4. Make a Payment")
        print("5. Check Student Balance")
        print("6. Show Courses")
        print("7. Show Registered Students")
        print("8. Show Students in a Course")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter name: ")
            email = input("Enter email: ")
            system.register_student(student_id, name, email)
        elif choice == '2':
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            fee = float(input("Enter course fee: "))
            system.add_course(course_id, name, fee)
        elif choice == '3':
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            system.enroll_in_course(student_id, course_id)
        elif choice == '4':
            student_id = input("Enter student ID: ")
            system.make_payment(student_id)
        elif choice == '5':
            student_id = input("Enter student ID: ")
            system.check_student_balance(student_id)
        elif choice == '6':
            system.show_courses()
        elif choice == '7':
            system.show_registered_students()
        elif choice == '8':
            course_id = input("Enter course ID: ")
            system.show_students_in_course(course_id)
        elif choice == '9':
            break  
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()


# I CERTIFY THAT I HAVE NOT GIVEN OR RECEIVED ANY UNAUTHORIZED ASSISTANCE ON THIS ASSIGNMENT