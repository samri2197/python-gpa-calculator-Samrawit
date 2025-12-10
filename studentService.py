from data_store import load, save

class StudentService:
    def __init__(self, data_path="data/students.json"):
        self.data_path = data_path
        self.students = load(data_path, [])
    
    def add_student(self, student_id, name):
        for student in self.students:
            if student["id"] == student_id:
                return False, "Student ID exists"
        
        self.students.append({"id": student_id, "name": name})
        save(self.data_path, self.students)
        return True, "Student added"
    
    def get_all_students(self):
        return self.students
    
    def find_student(self, student_id):
        for student in self.students:
            if student["id"] == student_id:
                return student
        return None
    
    def print_students(self):
        if not self.students:
            print("No students.")
            return
        
        print("\n=== STUDENTS ===")
        for student in self.students:
            print(f"ID: {student['id']} | Name: {student['name']}")