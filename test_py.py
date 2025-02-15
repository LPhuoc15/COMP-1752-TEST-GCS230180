from abc import ABC, abstractmethod

class Student(ABC):
    def __init__(self, name, major, student_id):
        self.name = name
        self.major = major
        self.student_id = student_id

    @abstractmethod
    def get_profile(self):
        pass

class PartTimeStudent(Student):
    count = 0  
    def __init__(self, name, major, student_id, min_hour=0, max_hour=0):
        super().__init__(name, major, student_id)
        self.min_hour = min_hour
        self.max_hour = max_hour
        PartTimeStudent.count += 1  

    @staticmethod
    def get_count():
        """Returns the number of PartTimeStudent instances created"""
        return PartTimeStudent.count

    def get_profile(self):
        return f"Part-Time Student: {self.name}, Major: {self.major}, ID: {self.student_id}"

class FullTimeStudent(Student):
    def __init__(self, name, major, student_id, joined_project=None, research_profile=""):
        super().__init__(name, major, student_id)
        self.joined_project = joined_project
        self.research_profile = research_profile

    def get_profile(self):
        return f"Full-Time Student: {self.name}, Major: {self.major}, ID: {self.student_id}"

class Lecturer:
    def __init__(self, lecturer_id, name, rank, research_profile=""):
        self.lecturer_id = lecturer_id
        self.name = name
        self.rank = rank
        self.research_profile = research_profile

    def get_profile(self):
        return f"Lecturer: {self.name}, Rank: {self.rank}, ID: {self.lecturer_id}"

class Project:
    def __init__(self, name, budget, leader=None):
        self.name = name
        self.budget = budget
        self.leader = leader
        self.members = []

    def assign_leader(self, lecturer):
        self.leader = lecturer

    def add_member(self, researcher):
        self.members.append(researcher)

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.lecturers = []
        self.projects = []

    def add_student(self, student):
        if len(self.students) < 10:
            self.students.append(student)
        else:
            print("Student limit reached!")

    def add_lecturer(self, lecturer):
        if len(self.lecturers) < 10:
            self.lecturers.append(lecturer)
        else:
            print("Lecturer limit reached!")

    def add_project(self, project):
        if len(self.projects) < 10:
            self.projects.append(project)
        else:
            print("Project limit reached!")

    def display_info(self):
        print("\n--- School System Info ---")
        print(f"Total Part-Time Students: {PartTimeStudent.get_count()}")
        print(f"Students: {[s.get_profile() for s in self.students]}")
        print(f"Lecturers: {[l.get_profile() for l in self.lecturers]}")
        print(f"Projects: {[p.name for p in self.projects]}")
        print("-------------------------\n")

school = SchoolSystem()

s1 = PartTimeStudent("Alice", "CS", "S001", 5, 20)
s2 = PartTimeStudent("Bob", "Math", "S002", 10, 25)
s3 = FullTimeStudent("Charlie", "Physics", "S003")

school.add_student(s1)
school.add_student(s2)
school.add_student(s3)

lecturer1 = Lecturer("L001", "Dr. Smith", "Professor")
school.add_lecturer(lecturer1)
project1 = Project("AI Research", 50000)
school.add_project(project1)
school.display_info()
