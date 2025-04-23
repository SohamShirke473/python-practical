student1={"name":"soham",
          "roll.no":69,
          "marks":100,
          "attendence":98}
student2={"name":"yash",
          "roll.no":62,
          "marks":40,
          "attendence":75}
student3={"name":"kyra",
          "roll.no":47,
          "marks":90,
          "attendence":75}
for k,v in student1.items():
    print("key={},value={}".format(k,v))
for k,v in student2.items():
    print("key={},value={}".format(k,v))
for k,v in student2.items():
    print("key={},value={}".format(k,v))
students = {"Student 1": student1, "Student 2": student2, "Student 3": student3}

name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance: "))

new_student = {"name": name, "roll.no": roll_no, "marks": marks, "attendance": attendance}
students[f"Student {len(students) + 1}"] = new_student
for student_name, student_info in students.items():
    print(f"\n{student_name} Record:")
    for key, value in student_info.items():
        print(f"{key} = {value}")
del students["Student 1"]
print(students)
student2["attendence"]+=1
for student_name, student_info in students.items():
    print(f"\n{student_name} Record:")
    for key, value in student_info.items():
        print(f"{key} = {value}")





