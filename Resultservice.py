from data_store import load, save

GRADE_POINTS = {
    "A+": 4.00, "A": 4.00, "A-": 3.75,
    "B+": 3.50, "B": 3.00, "B-": 2.75,
    "C+": 2.50, "C": 2.00, "C-": 1.75,
    "D": 1.00, "F": 0.00
}

class ResultService:
    def __init__(self, data_path="data/results.json"):
        self.data_path = data_path
        self.results = load(data_path, [])
    
    def add_result(self, student_id, course_code, grade, student_service, course_service):
        if not student_service.find_student(student_id):
            return False, "Student not found"
        
        if not course_service.find_course(course_code):
            return False, "Course not found"
        
        if grade not in GRADE_POINTS:
            return False, "Invalid grade"
        
        self.results.append({
            "student_id": student_id,
            "course_code": course_code,
            "grade": grade
        })
        save(self.data_path, self.results)
        return True, "Result added"
    
    def get_all_results(self):
        return self.results
    
    def get_student_results(self, student_id):
        return [r for r in self.results if r["student_id"] == student_id]
    
    def calculate_gpa(self, student_id, course_service):
        student_results = self.get_student_results(student_id)
        
        if not student_results:
            return None
        
        total_points = 0
        total_credits = 0
        
        for result in student_results:
            grade = result["grade"]
            course_code = result["course_code"]
            
            course = course_service.find_course(course_code)
            if not course:
                continue
            
            credit = course["credit"]
            grade_point = GRADE_POINTS.get(grade, 0)
            
            total_points += grade_point * credit
            total_credits += credit
        
        if total_credits == 0:
            return None
        
        return total_points / total_credits