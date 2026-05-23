students = [];

input1 = input("Enter name 1:");
students.append(input1.title());

input2 = input("Enter name 2:");
students.append(input2.title());

input3 = input("Enter name 3:");
students.append(input3.title());

print("Students", students);
print("Total students:", len(students));