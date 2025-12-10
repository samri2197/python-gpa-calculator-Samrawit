class GradeReport:
    def __init__(self, student_service, course_service, result_service):
        self.student_service = student_service
        self.course_service = course_service
        self.result_service = result_service
    
    def generate_transcript(self, student_id):
        student = self.student_service.find_student(student_id)
        if not student:
            print("Student not found.")
            return
        
        print(f"\n=== TRANSCRIPT: {student['name']} ({student_id}) ===")
        
        student_results = self.result_service.get_student_results(student_id)
        
        if not student_results:
            print("No results.")
            return
        
        total_points = 0
        total_credits = 0
        
        for result in student_results:
            course = self.course_service.find_course(result["course_code"])
            if course:
                credit = course["credit"]
                grade_point = self.result_service.GRADE_POINTS.get(result["grade"], 0)
                points = grade_point * credit
                
                total_points += points
                total_credits += credit
                
                print(f"{course['code']}: {course['name']} | Credits: {credit} | Grade: {result['grade']}")
        
        if total_credits > 0:
            gpa = total_points / total_credits
            print(f"\nTotal Credits: {total_credits}")
            print(f"GPA: {gpa:.2f}")