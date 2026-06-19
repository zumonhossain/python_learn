# marks = []

# while True:
#     mark = input("Enter student mark : ")

#     if mark.lower() == "stop":
#         break

#     marks.append(int(mark))

# total = 0
# i = 0

# while i < len(marks):
#     total = total + marks[i]
#     i = i + 1

# average = total / len(marks)

# print(f"Class Average: {average}")



student_marks = [];
while True:
    input_marks = input("enter student marks or stop:");
    if input_marks == "stop":
        break
    student_marks.append(float(input_marks));
# print(student_marks);
if len(student_marks) > 0:


    while i < len(student_marks):
        total_marks += student_marks[i];
        i += 1;
    average_marks = total_marks / len(student_marks)
    print("class avg:", average_marks);
else:
    print("marks 0");