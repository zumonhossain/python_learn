
print("-------- four step of python ---------")

def greet(name): # 1. def + fun name + parameter
    message = "Hello " +  name; # body
    return message # output return 
result = greet("Python"); # call
print(result);


print("-------- multiple function call ---------")
def my_function():
  print("Hello from a function");

my_function();
my_function();
my_function();


print("-------- without parameter function ---------")
def hello1():
    print("Without parameter function");
hello1();

print("-------- with parameter function ---------")
def hello2(name):
    print("Parameter with", name);
hello2("Python");
hello2("function");


print("-------- return with parameter function ---------")
def add(a, b):
    return a + b;
total = add(5, 10);
print("Total =", total);


print("-------- Default Parameter function ---------")
def default_parameter(name = "Zumon"):
    print("Hello", name);
default_parameter("Python");
default_parameter();
default_parameter("Rakib");


print("-------- multiple value return ---------")
def min_max(numbers):
    return min(numbers), max(numbers);

low, high = min_max([4, 8, 15, 16, 23, 42]);
print("Min:", low);
print("Max:", high);


print("-------- loop ---------")
def print_table(number):
    for i in range(1, 6):
        print(number, "*", i, "=", number * i);
print_table(5);




print("-------- fahrenheit to celsius ---------")
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9;

print(fahrenheit_to_celsius(77));
print(fahrenheit_to_celsius(95));
print(fahrenheit_to_celsius(50));



print("--------  return value directly ---------")
def get_greeting():
  return "Hello from a function";

print(get_greeting());


print("--------  return value directly ---------")

