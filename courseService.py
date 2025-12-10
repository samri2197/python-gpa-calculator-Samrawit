from data_store import load, save

class CourseService:
    def __init__(self, data_path="data/courses.json"):
        self.data_path = data_path
        self.courses = load(data_path, [])
    
    def add_course(self, code, name, credit):
        for course in self.courses:
            if course["code"] == code:
                return False, "Course exists"
        
        self.courses.append({"code": code, "name": name, "credit": credit})
        save(self.data_path, self.courses)
        return True, "Course added"
    
    def get_all_courses(self):
        return self.courses
    
    def find_course(self, course_code):
        for course in self.courses:
            if course["code"] == course_code:
                return course
        return None
    
    def print_courses(self):
        if not self.courses:
            print("No courses.")
            return
        
        print("\n=== COURSES ===")
        for course in self.courses:
            print(f"Code: {course['code']} | {course['name']} | Credits: {course['credit']}")