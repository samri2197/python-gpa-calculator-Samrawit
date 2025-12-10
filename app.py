from StudentService import StudentService
from CourseService import CourseService
from ResultService import ResultService
from GradeReport import GradeReport
import os

class GPACalculator:
    def __init__(self):
        self.student_service = StudentService()
        self.course_service = CourseService()
        self.result_service = ResultService()
        self.grade_report = GradeReport(
            self.student_service, 
            self.course_service, 
            self.result_service
        )
    
    def students_menu(self):
        while True:
            print("\n=== STUDENTS ===")
            print("1. Add Student")
            print("2. View Students")
            print("3. Back")
            
            choice = input("Choose: ").strip()
            
            if choice == "1":
                print("\nAdd Student:")
                sid = input("Student ID: ").strip()
                name = input("Name: ").strip()
                
                if sid and name:
                    success, msg = self.student_service.add_student(sid, name)
                    print(msg)
                else:
                    print("ID and Name required!")
                    
            elif choice == "2":
                self.student_service.print_students()
            elif choice == "3":
                break
            else:
                print("Invalid choice.")
    
    def courses_menu(self):
        while True:
            print("\n=== COURSES ===")
            print("1. Add Course")
            print("2. View Courses")
            print("3. Back")
            
            choice = input("Choose: ").strip()
            
            if choice == "1":
                print("\nAdd Course:")
                code = input("Course Code: ").strip().upper()
                name = input("Course Name: ").strip()
                credit = input("Credits: ").strip()
                
                if code and name and credit.isdigit():
                    success, msg = self.course_service.add_course(code, name, int(credit))
                    print(msg)
                else:
                    print("All fields required!")
                    
            elif choice == "2":
                self.course_service.print_courses()
            elif choice == "3":
                break
            else:
                print("Invalid choice.")
    
    def results_menu(self):
        while True:
            print("\n=== RESULTS ===")
            print("1. Add Result")
            print("2. View GPA")
            print("3. Back")
            
            choice = input("Choose: ").strip()
            
            if choice == "1":
                print("\nAdd Result:")
                
                # Show students
                students = self.student_service.get_all_students()
                if not students:
                    print("No students. Add students first.")
                    continue
                
                print("Students:")
                for s in students:
                    print(f"  {s['id']}: {s['name']}")
                
                sid = input("\nStudent ID: ").strip()
                
                # Show courses
                courses = self.course_service.get_all_courses()
                if not courses:
                    print("No courses. Add courses first.")
                    continue
                
                print("\nCourses:")
                for c in courses:
                    print(f"  {c['code']}: {c['name']}")
                
                code = input("\nCourse Code: ").strip().upper()
                grade = input("Grade (A, B+, etc): ").strip().upper()
                
                success, msg = self.result_service.add_result(
                    sid, code, grade, 
                    self.student_service, self.course_service
                )
                print(msg)
                
            elif choice == "2":
                print("\nCalculate GPA:")
                
                students = self.student_service.get_all_students()
                if not students:
                    print("No students.")
                    continue
                
                for s in students:
                    gpa = self.result_service.calculate_gpa(s["id"], self.course_service)
                    gpa_display = f"{gpa:.2f}" if gpa else "No results"
                    print(f"{s['id']}: {s['name']} - GPA: {gpa_display}")
                
                sid = input("\nEnter Student ID for transcript: ").strip()
                self.grade_report.generate_transcript(sid)
                
            elif choice == "3":
                break
            else:
                print("Invalid choice.")
    
    def run(self):
        print("=== GPA CALCULATOR ===")
        
        while True:
            print("\n=== MAIN MENU ===")
            print("1. Students")
            print("2. Courses")
            print("3. Results")
            print("4. Exit")
            
            choice = input("Choose: ").strip()
            
            if choice == "1":
                self.students_menu()
            elif choice == "2":
                self.courses_menu()
            elif choice == "3":
                self.results_menu()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    app = GPACalculator()
    app.run()