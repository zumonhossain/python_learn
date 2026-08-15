class Employee:
    def __init__(self, name, hours_worked_list):
        self.name = name;
        self.hours_worked_list = hours_worked_list;

    def get_total_hours(self):
        total = 0;
        for hours in self.hours_worked_list:
            total += hours;
        print(f"{self.name} worked a total of {total} hours");

emp1 = Employee("Zumon", [8, 7, 9, 8, 6]);
emp2 = Employee("Shakib", [6, 8, 7, 9, 8]);
emp3 = Employee("Rakib", [9, 9, 8, 7, 6]);
emp4 = Employee("Ikram", [7, 6, 8, 8, 9]);

emp1.get_total_hours();
emp2.get_total_hours();
emp3.get_total_hours();
emp4.get_total_hours();