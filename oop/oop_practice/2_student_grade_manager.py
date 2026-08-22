class Student:
    def __init__(self, student_id, name, grade, email=None):
        self.student_id = student_id
        self.name = name;
        self.grade = grade;
        self.email = email;

    def __str__(self):
        return f"ID: {self.student_id} | Name: {self.name} | Grade: {self.grade} | Email: {self.email}"

class GradeBook:
    def __init__(self):
        self.students = [];
        self.next_id = 1;

    def add_student(self, name, grade, email=None):
        student = Student(self.next_id, name, grade, email);
        self.students.append(student);
        self.next_id += 1;
        print(f"Student '{name}' added successfully!");

    def view_students(self):
        for student in self.students:
            print(student);

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print(student);
                return
        print(f"Student ID {student_id} not found!");

    def update_grade(self, student_id, new_grade):
        for student in self.students:
            if student.student_id == student_id:
                student.grade = new_grade;
                print(f"Student '{student.name}' grade updated to {new_grade}!");
                return
        print(f"Student ID {student_id} not found!");

    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student);
                print(f"Student '{student.name}' deleted successfully!");
                return
        print(f"Student ID {student_id} not found!");

# Demo
gradebook = GradeBook();
gradebook.add_student("Tanvir", "A", "tanvir@email.com");
gradebook.add_student("Nusrat", "B+");
gradebook.add_student("Rakib", "A-", "rakib@email.com");
gradebook.view_students();
print("\n-- Search --");
gradebook.search_student(2);
print("\n-- Update --");
gradebook.update_grade(3, "A");
print("\n-- Delete --");
gradebook.delete_student(2);
gradebook.view_students();