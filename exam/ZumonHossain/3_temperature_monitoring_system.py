temperature_list = [];

while True:
    temperature = input("Enter temperature in C (or 'stop': ");

    if temperature == "stop":
        break;

    temperature_list.append(int(temperature));

highest = temperature_list[0];
lowest = temperature_list[0];
heat_warning = 0;

i = 0

while i < len(temperature_list):

    if temperature_list[i] > highest:
        highest = temperature_list[i];

    if temperature_list[i] < lowest:
        lowest = temperature_list[i];

    if temperature_list[i] > 35:
        heat_warning = heat_warning + 1;

    i = i + 1

print("Highest:", highest);
print("Lowest:", lowest);
print("Heat warnings (>35C):", heat_warning);