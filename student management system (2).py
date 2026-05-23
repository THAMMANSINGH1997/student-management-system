#make a constractor for programing
class student:
    all_student =[]
    def __init__ (self,name,roll_no, age,marks):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.marks = marks

    def update_marks(self,new_marks):
        self.marks = new_marks

    def show_details(self):
        print(f"\nstudent datails:")
        print(f"name:{self.name}")
        print(f"roll number: {self.roll_no}") 
        print(f"Roll Number: {self.roll_no}") 
        print(f"marks:{self.marks}") 
@classmethod
def find_student_by_roll(cls,roll):
    for student in cls.all_student:
        if student.roll_no == roll:
            return student
    return None
@classmethod
def Add_Student(cls):
    name = input("Enter student name:  ")
    roll = input("Enter student roll number: ")
    age = input("Enter your age:  ")
    marks =int(input("Enter student marks:  "))
    student= cls(name,roll, marks)
    cls.all_student.append(student)
    print(f"student{name} added successfully!")

@classmethod
def update_student_marks(cls):
    roll = input("Enter student roll number to update marks: ")
    student = cls.find_student_by_roll(roll)
    if student:
        new_marks = int(input("Enter new marks: "))
        student.update_marks(new_marks)

@classmethod
def show_all_students(cls):
    if not cls.all_student:
        print("no student found")
        return
    for student in cls.all_student:
        student.show_details()



#make a display for the student
def menu():
    while True:
        print("\n=============student mgnt system=========")  
        print("1.Add Student")
        print("2.Update marks") 
        print("3.Show All Student")
        print("4.Exit")     

        choice = input("Enter your option(1-4):   ")
        if  choice == '1':
            student.add_student()
        elif choice == '2':
            student.update_student_marks()
        elif choice == '3':
            student.show_all_students()
        elif choice == '4':
            print("Exitting Student management system, Goodbye")
            break
        else:
            print("please try again")


if __name__ =="__main__":
    menu()  





